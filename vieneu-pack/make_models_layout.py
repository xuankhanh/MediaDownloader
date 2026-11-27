"""
Puts the files VieNeu-TTS v3 Turbo needs for one precision into a Hugging Face cache layout under <folder>/hub, so that the runner reads them offline
(HF_HOME=<folder>, HF_HUB_OFFLINE=1):  hub/models--<org>--<name>/refs/main  and  hub/models--<org>--<name>/snapshots/<revision>/<files>.
Downloads what is missing (into HF_HOME of the caller), then copies the files as they are (no links: they are zipped).

    python make_models_layout.py <folder> int8|fp32
"""
import fnmatch
import os
import shutil
import sys

from huggingface_hub import snapshot_download

folder, precision = sys.argv[1], sys.argv[2]
subfolder = {"int8": "onnx_int8", "fp32": "onnx_update"}[precision]

REPOS = {
    # The model, its speaker encoder and denoiser, and the graphs of the precision (about 165 MB int8, 475 MB fp32)
    "pnnbao-ump/VieNeu-TTS-v3-Turbo": ["config.json", "denoiser.onnx", "speaker_encoder.onnx", f"{subfolder}/*"],
    # The codec that turns the model's tokens into sound and the speaker's voice into tokens (about 90 MB)
    "OpenMOSS-Team/MOSS-Audio-Tokenizer-Nano-ONNX": ["*.onnx", "*.data", "*.json"],
}

# The revision of each repository the pack is made from (checked 2026-11-27): a pack made later is of the same files, not of whatever the authors have changed since.
# A newer model is taken by changing these on purpose, then making a pack and listening to it
REVISIONS = {
    "pnnbao-ump/VieNeu-TTS-v3-Turbo": "61b85e3d937fbbacb387714180e8182823512523",
    "OpenMOSS-Team/MOSS-Audio-Tokenizer-Nano-ONNX": "ceff0d0749bfb3fa2d61149794ec6feef0d1e1ae",
}

for repo, patterns in REPOS.items():
    source = snapshot_download(repo, revision=REVISIONS[repo], allow_patterns=patterns)
    revision = os.path.basename(source)
    root = os.path.join(folder, "hub", "models--" + repo.replace("/", "--"))
    target = os.path.join(root, "snapshots", revision)
    for current, _, files in os.walk(source):
        for name in files:
            path = os.path.join(current, name)
            relative = os.path.relpath(path, source)
            # Only what this precision needs: the snapshot of the cache may hold the other one's files too (downloaded before)
            if not any(fnmatch.fnmatch(relative.replace(os.sep, "/"), pattern) for pattern in patterns):
                continue
            destination = os.path.join(target, relative)
            os.makedirs(os.path.dirname(destination), exist_ok=True)
            # A cache entry may be a link to a blob: its content is what is copied
            shutil.copyfile(os.path.realpath(path), destination)
    os.makedirs(os.path.join(root, "refs"), exist_ok=True)
    with open(os.path.join(root, "refs", "main"), "w", encoding="ascii") as f:
        f.write(revision)
    print(f"{repo}: {revision}")
