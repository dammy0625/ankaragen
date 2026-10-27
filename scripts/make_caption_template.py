from pathlib import Path

files = sorted(Path("dataset").glob("*.jpg"))

with open("captions.txt", "w", encoding="utf-8") as f:
    for p in files:
        f.write(f"{p.name} | ankara print, \n")

print(f"Template created for {len(files)} images")