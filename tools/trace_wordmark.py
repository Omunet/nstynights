#!/usr/bin/env python3
"""Trace the lower NSTY mark from the supplied profile JPEG. LX is cropped out."""

import subprocess
from pathlib import Path

import numpy as np
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "sources" / "incoming" / "logo" / "lx-nsty-profile-1.jpg"
OUT = ROOT / "deploy" / "assets" / "img" / "nsty-wordmark.svg"
CROP = ROOT / "sources" / "logo" / "nsty-lower-crop.jpg"


def mask_from_profile():
    image = Image.open(SOURCE).convert("L")
    pixels = np.asarray(image)
    # Extent uses a low cutoff so the tips stay in frame. The stroke cutoff
    # stays high enough that the dark letter interiors remain holes.
    extent = pixels > 40
    stroke = pixels > 50
    lower = extent[65:, :]
    ys, xs = np.where(lower)
    y0, y1 = int(ys.min()), int(ys.max())
    x0, x1 = int(xs.min()), int(xs.max())
    crop_box = (x0, 65 + y0, x1 + 1, 65 + y1 + 1)
    color = Image.open(SOURCE).convert("RGB").crop(crop_box)
    CROP.parent.mkdir(parents=True, exist_ok=True)
    color.save(CROP, quality=90)
    glyph = stroke[65 + y0 : 65 + y1 + 1, x0 : x1 + 1]
    pad = 2
    canvas = np.full((glyph.shape[0] + pad * 2, glyph.shape[1] + pad * 2), 255, dtype=np.uint8)
    canvas[pad : pad + glyph.shape[0], pad : pad + glyph.shape[1]] = np.where(glyph, 0, 255)
    pbm = Path("/tmp/nsty-trace.pbm")
    # Potrace traces black. Avoid Pillow's dither, which can flip the plate.
    image = Image.fromarray(canvas, mode="L")
    image = image.point(lambda value: 0 if value < 128 else 255, mode="1")
    image.save(pbm)
    return pbm, canvas.shape[1], canvas.shape[0]


def main():
    pbm, width, height = mask_from_profile()
    raw = Path("/tmp/nsty-trace.svg")
    subprocess.check_call(
        ["potrace", "-s", "--flat", "-t", "2", "-a", "0.45", "-O", "0.35", "-o", str(raw), str(pbm)]
    )
    text = raw.read_text(encoding="utf-8")
    start = text.index("<g ")
    end = text.index("</g>") + 4
    group = text[start:end]
    group = group.replace(
        'fill="#000000"',
        'fill="url(#metal)" fill-rule="evenodd"',
    )
    svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" role="img">
  <title>NSTY</title>
  <defs>
    <linearGradient id="metal" x1="0" y1="0" x2="0.35" y2="1">
      <stop offset="0" stop-color="#ffffff"/>
      <stop offset="0.16" stop-color="#9aa6b2"/>
      <stop offset="0.34" stop-color="#f4f6f8"/>
      <stop offset="0.5" stop-color="#4e5862"/>
      <stop offset="0.68" stop-color="#e7ebf0"/>
      <stop offset="0.84" stop-color="#6a737d"/>
      <stop offset="1" stop-color="#c5ced6"/>
    </linearGradient>
  </defs>
  {group}
</svg>
'''
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(svg, encoding="utf-8")
    OUT.with_name("favicon.svg").write_text(svg, encoding="utf-8")
    print(f"{OUT} viewBox 0 0 {width} {height}")
    print(CROP)


if __name__ == "__main__":
    main()
