# Makes SoundSeparator's model, bandit-v2-multi.onnx, from BandIt v2's multilingual checkpoint, and checks it.
#
#   git clone https://github.com/kwatcharasupat/bandit-v2
#   curl -L -o checkpoint-multi.ckpt "https://zenodo.org/records/12701995/files/checkpoint-multi.ckpt?download=1"
#       (MD5 fea2868787551b0cff36cfcf7c3622a3)
#   python -m venv venv && venv\Scripts\pip install torch torchaudio numpy onnx onnxscript tqdm onnxruntime==1.24.4
#       (torch and torchaudio from https://download.pytorch.org/whl/cpu: no graphics card needed)
#   venv\Scripts\python -I bandit_export.py --repo bandit-v2 --ckpt checkpoint-multi.ckpt --out bandit-v2-multi.onnx --check-onnx
#
# It prints how far the exported core is from the model itself on random sound (about 1e-7 at most), writes the ONNX
# (about 149 MB), and with --check-onnx runs it with onnxruntime (the version the app downloads) against PyTorch; it
# stops with an error when any of it is off. The ONNX goes on the MediaDownloader repository's separator-models-v1
# release (SoundSeparator.Install.cs: ModelUrl, ModelSize), which its "Sound separator model" workflow
# (separator-model.yml) makes. The weights are CC BY-SA 4.0, as the checkpoint's.
#
# The core: the normalized complex STFT of a mono 48 kHz piece as real/imaginary -> the three complex masks (speech,
# music, sfx) as real/imaginary. The STFT, the masking and the inverse STFT are SoundSeparator's, in C#.
import argparse, os, sys, types
import numpy as np
import torch
from torch import nn
import torch.nn.functional as F

p = argparse.ArgumentParser()
p.add_argument("--repo", required=True)
p.add_argument("--ckpt", required=True)
p.add_argument("--out", required=True)
p.add_argument("--frames", type=int, default=751)  # 8 s at 48 kHz, hop 512, centered
p.add_argument("--wav-in")   # optional: 48 kHz mono float32 .npy to separate with the reference model
p.add_argument("--wav-out")  # folder for the reference stems (.npy)
p.add_argument("--check-onnx", action="store_true")  # run the ONNX with onnxruntime and compare it with PyTorch
args = p.parse_args()

sys.path.insert(0, args.repo)
# Only the model's code is needed: Lightning's base class and torchaudio's StreamReader (gone from newer torchaudio) stubbed
pl = types.ModuleType("pytorch_lightning"); pl.LightningModule = nn.Module; sys.modules["pytorch_lightning"] = pl
_tio = types.ModuleType("torchaudio.io"); _tio.StreamReader = object; sys.modules["torchaudio.io"] = _tio
# librosa's two conversions the band split uses, as librosa has them
_lr = types.ModuleType("librosa")
_lr.hz_to_midi = lambda f: 12 * (np.log2(np.asanyarray(f)) - np.log2(440.0)) + 69
_lr.midi_to_hz = lambda n: 440.0 * (2.0 ** ((np.asanyarray(n) - 69.0) / 12.0))
sys.modules["librosa"] = _lr
from src.models.bandit.bandit import Bandit  # noqa: E402

model = Bandit(in_channels=1, stems=["speech", "music", "sfx"], band_type="musical", n_bands=64,
               normalize_channel_independently=False, treat_channel_as_feature=True, n_sqm_modules=8,
               emb_dim=128, rnn_dim=256, bidirectional=True, rnn_type="GRU", mlp_dim=512,
               hidden_activation="Tanh", complex_mask=True, use_freq_weights=True, n_fft=2048,
               win_length=2048, hop_length=512, window_fn="hann_window", power=None, center=True,
               normalized=True, pad_mode="reflect", onesided=True, fs=48000)
state = torch.load(args.ckpt, map_location="cpu", weights_only=False)["state_dict"]
state = {k[len("model."):]: v for k, v in state.items() if k.startswith("model.")}
missing, unexpected = model.load_state_dict(state, strict=False)
missing = [m for m in missing if "freq_weights" not in m]
print("missing", missing[:10], "unexpected", unexpected[:10])
if missing or unexpected:
    sys.exit("The checkpoint doesn't fit the model")
model.eval()


class Core(nn.Module):
    def __init__(self, m: Bandit):
        super().__init__()
        self.m = m
        self.specs = m.band_specs.get_band_specs()
        self.n_freq = 1025

    def forward(self, spec):  # spec (B, 1025, T, 2)
        m = self.m
        B, _, T, _ = spec.shape
        x = spec.permute(0, 2, 1, 3)  # (B, T, F, 2)
        z = torch.stack([nfm.combined(x[:, :, fs:fe, :].reshape(B, T, -1))
                         for (fs, fe), nfm in zip(self.specs, m.band_split.norm_fc_modules)], dim=1)
        for layer in m.tf_model.seqband:
            z = layer(z)
        outs = []
        for stem in m.stems:
            mem = m.mask_estim[stem]
            total = None
            for b, (fs, fe) in enumerate(self.specs):
                mb = mem.norm_mlp[b].combined(z[:, b])  # (B, T, bw*2)
                mb = mb.reshape(B, T, fe - fs, 2)
                fw = mem.get_buffer(f"freq_weights/{b}").float()  # stored as float64
                mb = mb * fw[None, None, :, None]
                mb = F.pad(mb, (0, 0, fs, self.n_freq - fe))
                total = mb if total is None else total + mb
            outs.append(total.permute(0, 2, 1, 3))  # (B, F, T, 2)
        return torch.stack(outs, dim=1)  # (B, 3, F, T, 2)


core = Core(model).eval()

with torch.no_grad():
    audio = torch.randn(2, 1, 8 * 48000) * 0.1
    x = model.stft(audio)  # (B, 1, F, T) complex
    batch = {"mixture": {"audio": audio, "spectrogram": x}}
    ref = model.separate(batch)
    spec = torch.view_as_real(x[:, 0])
    masks = core(spec)
    for i, stem in enumerate(model.stems):
        mask = torch.view_as_complex(masks[:, i].contiguous())
        est = model.istft(x[:, 0] * mask, audio.shape[-1])
        diff = (est - ref["estimates"][stem]["audio"][:, 0]).abs().max().item()
        print(stem, "core vs model, max abs diff", diff)
        if diff > 1e-4:
            sys.exit(f"The core's {stem} isn't the model's")
    print("frames", x.shape[-1])

    if args.wav_in:
        from src.system.inference_handler import StandardTensorChunkedInferenceHandler
        handler = StandardTensorChunkedInferenceHandler(chunk_size_seconds=8.0, hop_size_seconds=4.0,
                                                        inference_batch_size=4, fs=48000)
        mix = torch.from_numpy(np.load(args.wav_in)).float()[None, None, :]
        out = handler(mix, model)
        os.makedirs(args.wav_out, exist_ok=True)
        for stem in model.stems:
            np.save(os.path.join(args.wav_out, stem + ".npy"), out["estimates"][stem]["audio"][0, 0].numpy())
        print("reference stems written")

    torch.onnx.export(core, (spec[:1, :, : args.frames],), args.out, input_names=["spec"], output_names=["masks"],
                      dynamic_axes={"spec": {0: "batch", 2: "frames"}, "masks": {0: "batch", 3: "frames"}},
                      opset_version=17, dynamo=False)
    print("exported", args.out, os.path.getsize(args.out))

    if args.check_onnx:
        # The ONNX as the app runs it (ONNX Runtime, on the processor), on a whole piece of 751 frames, against PyTorch
        import onnxruntime as ort
        session = ort.InferenceSession(args.out, providers=["CPUExecutionProvider"])
        piece = spec[:, :, : args.frames].contiguous()
        got = session.run(["masks"], {"spec": piece.numpy()})[0]
        want = core(piece).numpy()
        diff = float(np.abs(got - want).max())
        print("onnxruntime", ort.__version__, "vs PyTorch, max abs diff", diff, "of masks up to", float(np.abs(want).max()))
        if got.dtype != np.float32 or got.shape != want.shape or diff > 1e-3:
            sys.exit("The ONNX doesn't give PyTorch's masks")
