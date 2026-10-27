from pathlib import Path
from PIL import Image

raw = Path("raw")
out = Path("dataset")
out.mkdir(exist_ok=True)

for p in sorted(raw.glob("*")):
    if p.suffix.lower() not in {".jpg", ".jpeg", ".png", ".webp"}:
        continue
    img = Image.open(p).convert("RGB")
    w, h = img.size
    s = min(w, h)                          # side length of the biggest centered square
    left, top = (w - s) // 2, (h - s) // 2
    img = img.crop((left, top, left + s, top + s)).resize((512, 512), Image.LANCZOS)
    img.save(out / f"{p.stem}.jpg", quality=95)
    print("saved", p.stem, f"(original {w}x{h})")