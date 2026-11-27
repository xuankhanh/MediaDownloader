"""
Reads lines aloud with VieNeu-TTS v3 Turbo (Apache-2.0, https://github.com/pnnbao97/VieNeu-TTS) for Media Downloader's Dub window.

It is run by the app (MediaKit's VieNeu class) with the Python it ships, as:   python -I -X utf8 vieneu_runner.py job.json
and tells how it goes with one JSON object a line on its standard output:
    {"event": "loaded", "seconds": 6.1, "sample_rate": 48000}
    {"event": "clip", "i": 0, "seconds": 2.4}            (a clip's WAV is out_dir/00000.wav; none for a line it couldn't read)
    {"event": "warning", "i": 3, "message": "..."}        (the line is left out, the others go on)
    {"event": "done"}                                       or   {"event": "error", "message": "..."} with a non-zero exit code
The job file (UTF-8 JSON):
    site_packages  the folder of the libraries
    models_dir     the Hugging Face cache folder with the model (read offline, never downloaded here)
    precision      "int8" (CPUs with VNNI: smaller and faster) or "fp32"
    threads        0 = the engine's own choice
    voice          {"kind": "clone", "wav": "path"} (a person's own recording)  or  {"kind": "preset", "name": "..."}
    texts          the lines to read
    out_dir        where the clips go
"""
import json
import os
import sys
import time
import traceback


def emit(**fields):
    print(json.dumps(fields, ensure_ascii=False), flush=True)


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    with open(sys.argv[1], encoding="utf-8") as f:
        job = json.load(f)
    sys.path.insert(0, job["site_packages"])
    # Everything is read from the folder the app put there: nothing is fetched (no network, no cache in the user's profile)
    os.environ["HF_HOME"] = job["models_dir"]
    os.environ["HF_HUB_OFFLINE"] = "1"
    os.environ["HF_HUB_DISABLE_TELEMETRY"] = "1"
    os.environ["HF_HUB_DISABLE_SYMLINKS_WARNING"] = "1"
    os.environ["TOKENIZERS_PARALLELISM"] = "false"

    from vieneu import Vieneu

    started = time.time()
    tts = Vieneu(mode="v3turbo", precision=job.get("precision", "int8"), backend="onnx", device="cpu", threads=int(job.get("threads", 0)))
    emit(event="loaded", seconds=round(time.time() - started, 1), sample_rate=tts.sample_rate)

    voice = job["voice"]
    if voice["kind"] == "clone":
        # The recording is cleaned and trimmed to what a copy needs (a few seconds) by the library itself
        tts.add_voice("clone", voice["wav"])
        voice_name = "clone"
    else:
        # "" is the voice the model starts with
        voice_name = voice.get("name") or None

    out_dir = job["out_dir"]
    os.makedirs(out_dir, exist_ok=True)
    # Warms the engine, so the first line isn't the slow one
    def speak(text):
        return tts.infer(text, voice=voice_name) if voice_name else tts.infer(text)

    try:
        speak("Xin chào.")
    except Exception:
        pass
    for i, text in enumerate(job["texts"]):
        try:
            if not any(ch.isalnum() for ch in text):
                continue
            audio = speak(text)
            tts.save(audio, os.path.join(out_dir, f"{i:05d}.wav"))
            emit(event="clip", i=i, seconds=round(len(audio) / tts.sample_rate, 2))
        except Exception as ex:  # a line it can't read must not stop the others
            emit(event="warning", i=i, message=str(ex)[:300])
    emit(event="done")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as ex:
        emit(event="error", message=f"{type(ex).__name__}: {ex}", trace=traceback.format_exc()[-1500:])
        sys.exit(1)
