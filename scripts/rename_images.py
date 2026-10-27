import csv
from pathlib import Path

dataset = Path("dataset")
files = sorted(p for p in dataset.glob("*.jpg"))

# Pass 1: move everything to temporary names so new names can't collide with old ones
temp = []
for i, p in enumerate(files, start=1):
    t = dataset / f"tmp_{i:03d}.jpg"
    p.rename(t)
    temp.append((p.name, t))

# Pass 2: give each file its final name and record old -> new
with open("rename_map.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["old_name", "new_name"])
    for i, (old_name, t) in enumerate(temp, start=1):
        new_name = f"ankara_{i:03d}.jpg"
        t.rename(dataset / new_name)
        writer.writerow([old_name, new_name])
        print(f"{old_name} -> {new_name}")