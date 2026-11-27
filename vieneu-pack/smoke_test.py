"""
Looks at a voice pack made by build-pack.ps1 before it is released, as Media Downloader would take it:
  1. manifest.json: the pack's number and contract, and each zip's size and SHA-256 against its file;
  2. the runtime zip has what the app runs and what Apache-2.0 asks to go with it, and not what was cut out;
  3. each zip is unpacked as the app unpacks it, and vieneu_runner.py reads a line with the model's own voice, in fp32 and in int8 (the runner of the job file the app writes);
  4. a voice is copied from a recording (the first reading is the recording) and reads a line: the voice cloning of the Dub window and Tools > Record my voice.
The runner has no CPU with VNNI to count on, so int8 is only looked at for reading something (not for how clean it sounds). Exits with 1 and says what failed.

    python -I smoke_test.py <folder with the pack> <pack number> <contract>
"""
import hashlib
import json
import os
import shutil
import subprocess
import sys
import tempfile
import time
import wave
import zipfile

# The Python of the GitHub runner writes to a pipe in the Windows code page, which has no Vietnamese letters (voices are called "Hải Đăng"): UTF-8, whatever is set
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

failed = []


def check(ok, what, detail=""):
    print(("ok    " if ok else "FAIL  ") + what + ((" - " + str(detail)) if detail else ""), flush=True)
    if not ok:
        failed.append(what)
    return ok


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for block in iter(lambda: f.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def unpack(zip_path, target):
    # As the app does: an entry's name may use "\" (what Windows PowerShell 5.1 writes), and nothing may go outside the folder
    root = os.path.abspath(target) + os.sep
    with zipfile.ZipFile(zip_path) as z:
        for entry in z.infolist():
            name = entry.filename.replace("\\", "/")
            if name.endswith("/"):
                continue
            path = os.path.abspath(os.path.join(target, name))
            if not path.startswith(root):
                continue
            os.makedirs(os.path.dirname(path), exist_ok=True)
            with z.open(entry) as source, open(path, "wb") as out:
                shutil.copyfileobj(source, out)


def read_wav(path):
    with wave.open(path, "rb") as w:
        frames = w.readframes(w.getnframes())
        samples = [int.from_bytes(frames[i:i + 2], "little", signed=True) for i in range(0, len(frames) - 1, 2)]
        return w.getnchannels(), w.getsampwidth(), w.getframerate(), w.getnframes() / w.getframerate(), samples


def read_line(runtime, models, precision, voice, text, out_dir):
    """Runs the runner as the app does (a job file, then the lines of JSON on its standard output); returns (events, wav path or None)."""
    job = {
        "site_packages": os.path.join(runtime, "site-packages"),
        "models_dir": models,
        "precision": precision,
        "threads": 0,
        "out_dir": out_dir,
        "voice": voice,
        "texts": [text],
    }
    os.makedirs(out_dir, exist_ok=True)
    job_path = os.path.join(out_dir, "job.json")
    with open(job_path, "w", encoding="utf-8") as f:
        json.dump(job, f, ensure_ascii=False)
    started = time.time()
    run = subprocess.run([os.path.join(runtime, "python", "python.exe"), "-I", "-X", "utf8", os.path.join(runtime, "vieneu_runner.py"), job_path],
                         capture_output=True, text=True, encoding="utf-8", cwd=runtime, timeout=900)
    events = []
    for line in run.stdout.splitlines():
        if line.startswith("{"):
            try:
                events.append(json.loads(line))
            except ValueError:
                pass
    kinds = [e.get("event") for e in events]
    check(run.returncode == 0, f"[{precision}/{voice['kind']}] the runner ends well", f"exit {run.returncode}, {time.time() - started:.0f} s" + ("" if run.returncode == 0 else "\n" + run.stderr[-1500:] + "\n" + run.stdout[-800:]))
    check("loaded" in kinds and "clip" in kinds and kinds[-1] == "done", f"[{precision}/{voice['kind']}] it says loaded, clip, done", kinds)
    wav = os.path.join(out_dir, "00000.wav")
    return events, wav if os.path.exists(wav) else None


def check_clip(label, wav, low, high):
    if not check(wav is not None, f"{label}: a clip was written"):
        return
    channels, width, rate, seconds, samples = read_wav(wav)
    check(channels == 1 and width == 2 and rate == 48000, f"{label}: 16-bit mono at 48 kHz (what the app reads)", f"{channels} ch, {width * 8}-bit, {rate} Hz")
    check(low <= seconds <= high, f"{label}: a plausible length for the line", f"{seconds:.1f} s")
    peak = max((abs(s) for s in samples), default=0)
    check(peak > 2000, f"{label}: there is sound in it, not silence", f"peak {peak} of 32767")
    check(len(set(samples[::50])) > 100, f"{label}: it is not a constant tone or noise-free silence", f"{len(set(samples[::50]))} distinct levels")


def main():
    pack, number, contract = sys.argv[1], sys.argv[2], sys.argv[3]
    work = tempfile.mkdtemp(prefix="vieneu-smoke-")

    # 1. the manifest
    with open(os.path.join(pack, "manifest.json"), encoding="utf-8") as f:
        raw = f.read()
    check(not raw.startswith("﻿"), "manifest.json has no byte order mark (the app reads it as it comes over the network)")
    manifest = json.loads(raw)
    check(str(manifest.get("version")) == number, "the manifest's number is the one asked for", f"{manifest.get('version')} / {number}")
    check(str(manifest.get("contract")) == contract, "it says the contract the app keeps to", f"{manifest.get('contract')} / {contract}")
    check(bool(manifest.get("vieneu")), "it says which VieNeu is inside", manifest.get("vieneu"))
    for part in ("runtime", "int8", "fp32"):
        entry = manifest[part]
        path = os.path.join(pack, entry["file"])
        check(entry["file"].endswith(f"-{number}.zip"), f"{part}: its name carries the number", entry["file"])
        if check(os.path.exists(path), f"{part}: the file is there"):
            check(os.path.getsize(path) == entry["size"], f"{part}: the size is the manifest's", f"{os.path.getsize(path):,} bytes")
            check(sha256(path) == entry["sha256"], f"{part}: the SHA-256 is the manifest's")
    sizes = {p: manifest[p]["size"] / 1e6 for p in ("runtime", "int8", "fp32")}
    check(40 < sizes["runtime"] < 120 and 150 < sizes["int8"] < 400 and 250 < sizes["fp32"] < 500, "the sizes are about what they were when the pack was tried",
          ", ".join(f"{p} {v:.0f} MB" for p, v in sizes.items()))

    # 2. what the runtime zip holds
    with zipfile.ZipFile(os.path.join(pack, manifest["runtime"]["file"])) as z:
        names = {n.replace("\\", "/") for n in z.namelist()}
    for must in ("python/python.exe", "vieneu_runner.py", "version.txt", "presets.json", "licenses/Apache-2.0.txt", "licenses/THIRD-PARTY.txt", "site-packages/vieneu/assets/voices_v3_turbo.json"):
        check(must in names, f"the runtime has {must}")
    check(not any(n.startswith("python/tcl/") or n.startswith("python/Lib/site-packages/pip") for n in names), "what was cut out (tcl/tk, pip) is not there")

    # 3. unpacked as the app does, and reading
    runtime = os.path.join(work, "runtime")
    unpack(os.path.join(pack, manifest["runtime"]["file"]), runtime)
    check(open(os.path.join(runtime, "version.txt"), encoding="ascii").read().strip() == number, "version.txt of the runtime is the number")
    with open(os.path.join(runtime, "presets.json"), encoding="utf-8") as f:
        presets = json.load(f)
    voices = presets.get("voices", [])
    check(len(voices) >= 10 and all(v.get("name") and v.get("region") and v.get("style") and "male" in v for v in voices), "presets.json lists the model's voices, each with its name, sex, region and style", f"{len(voices)} voices")
    check(any(v["name"] == presets.get("default") for v in voices), "its default voice is one of them", presets.get("default"))
    clone_source = None
    for precision in ("fp32", "int8"):
        models = os.path.join(work, "models-" + precision)
        unpack(os.path.join(pack, manifest[precision]["file"]), models)
        # the model's own voice, the first one it has: no recording
        events, wav = read_line(runtime, models, precision, {"kind": "preset", "name": ""}, "Xin chào các bạn, hôm nay trời đẹp, chúng ta cùng đi dạo nhé.", os.path.join(work, "out-" + precision))
        check_clip(f"[{precision}/preset]", wav, 1.5, 12)
        if precision == "fp32" and wav:
            clone_source = wav
        shutil.rmtree(models, ignore_errors=True)
        if precision == "fp32":
            # 4. a voice copied from a recording: the clip just read is the recording (3 to 12 s of a voice)
            if clone_source:
                models = os.path.join(work, "models-fp32-clone")
                unpack(os.path.join(pack, manifest["fp32"]["file"]), models)
                events, wav = read_line(runtime, models, "fp32", {"kind": "clone", "wav": clone_source}, "Đây là giọng được nhân bản từ một bản thu.", os.path.join(work, "out-clone"))
                check_clip("[fp32/clone]", wav, 1.0, 12)
                shutil.rmtree(models, ignore_errors=True)

    shutil.rmtree(work, ignore_errors=True)
    print()
    if failed:
        print(f"{len(failed)} CHECK(S) FAILED:")
        for what in failed:
            print("  - " + what)
        return 1
    print("ALL CHECKS PASSED")
    return 0


if __name__ == "__main__":
    sys.exit(main())
