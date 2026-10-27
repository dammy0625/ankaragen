import json
from pathlib import Path

dataset = Path("dataset")
rows = []
problems = []

with open("captions.txt", encoding="utf-8") as f:
    for line_no, line in enumerate(f, start=1):
        line = line.strip()
        if not line:
            continue
        if "|" not in line:
            problems.append(f"line {line_no}: no '|' found")
            continue
        name, caption = line.split("|", 1)
        name = name.strip()
        caption = " ".join(caption.split())  # cleans up extra spaces
        if not (dataset / name).exists():
            problems.append(f"{name}: image not found in dataset folder")
            continue
        if caption.lower().rstrip(", ") == "ankara print":
            problems.append(f"{name}: caption not written yet")
            continue
        rows.append({"file_name": name, "text": caption})

if problems:
    print("Fix these first, nothing was written:")
    for p in problems:
        print("  -", p)
else:
    with open(dataset / "metadata.jsonl", "w", encoding="utf-8") as f:
        for r in rows:
            f.write(json.dumps(r) + "\n")
    print(f"Done: wrote {len(rows)} captions to dataset/metadata.jsonl")






    41020261024100556770149