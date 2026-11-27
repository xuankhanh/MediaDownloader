"""
Makes presets.json of the voice pack: the voices VieNeu-TTS has of its own, as the model's list (assets/voices_v3_turbo.json of the vieneu package) gives them, in the
words Media Downloader's Dub window lists them with. The app reads it from the installed pack, so a newer VieNeu's new voices are listed with no change in the app
(the app has its own copy of the list for before the pack is downloaded).

    python make_presets.py <voices_v3_turbo.json> <presets.json>

presets.json:  {"default": "Hai Dang", "voices": [{"name": ..., "male": true, "region": "North", "style": "natural"}, ...]}
region is North, Central or South; style is natural, story, news or audiobook; one the model has that isn't one of these is passed on as it is.
"""
import json
import sys

# -I of the way it is run ignores PYTHONUTF8, and the console of Windows knows no Vietnamese letters
sys.stdout.reconfigure(encoding="utf-8")

REGIONS = {"Bắc": "North", "Trung": "Central", "Nam": "South"}
ORDER = {"North": 0, "Central": 1, "South": 2}


def style_of(description):
    if "kể chuyện" in description:
        return "story"
    if "tin tức" in description:
        return "news"
    if "đọc truyện" in description:
        return "audiobook"
    return "natural"


def main():
    with open(sys.argv[1], encoding="utf-8") as f:
        data = json.load(f)
    voices = []
    for name, v in data["presets"].items():
        region = REGIONS.get(v.get("region", ""), v.get("region", ""))
        voices.append({"name": name, "male": v.get("gender") == "male", "region": region, "style": style_of(v.get("description", ""))})
    # By region, women first, then by name
    voices.sort(key=lambda v: (ORDER.get(v["region"], 9), v["male"], v["name"]))
    if not voices:
        raise SystemExit("the model's list has no voices")
    default = data.get("default_voice") or voices[0]["name"]
    with open(sys.argv[2], "w", encoding="utf-8") as f:
        json.dump({"default": default, "voices": voices}, f, ensure_ascii=False, indent=1)
    print(f"{len(voices)} voices, default {default}")


main()
