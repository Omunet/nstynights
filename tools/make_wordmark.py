#!/usr/bin/env python3
"""Build the NSTY-only wordmark as filled SVG paths.

The upper LX line and the peak above it are omitted. Paths are constructed
geometry, not a font and not an embedded raster. Chrome is a shared gradient.
"""

from pathlib import Path

OUT = Path(__file__).resolve().parents[1] / "deploy" / "assets" / "img" / "nsty-wordmark.svg"


def thick_line(x1, y1, x2, y2, thickness):
    dx, dy = x2 - x1, y2 - y1
    length = (dx * dx + dy * dy) ** 0.5
    nx, ny = -dy / length * thickness / 2, dx / length * thickness / 2
    return [
        (x1 + nx, y1 + ny),
        (x2 + nx, y2 + ny),
        (x2 - nx, y2 - ny),
        (x1 - nx, y1 - ny),
    ]


def rect(x, y, w, h):
    return [(x, y), (x + w, y), (x + w, y + h), (x, y + h)]


def d(points):
    return "M " + " L ".join(f"{x:.2f} {y:.2f}" for x, y in points) + " Z"


def letters():
    shapes = []
    stem = 56
    # N: full-height stems and a diagonal that overlaps both of them.
    shapes.append(rect(48, 36, stem, 220))
    shapes.append(rect(196, 36, stem, 220))
    shapes.append(thick_line(76, 42, 224, 248, 58))
    # S: upper bowl closes on the left, lower bowl closes on the right.
    shapes.append(rect(286, 36, 168, stem))
    shapes.append(rect(286, 36, stem, 128))
    shapes.append(rect(286, 118, 168, stem))
    shapes.append(rect(398, 118, stem, 138))
    shapes.append(rect(286, 200, 168, stem))
    # T
    shapes.append(rect(488, 36, 176, stem))
    shapes.append(rect(547, 84, stem, 172))
    # Y
    shapes.append(thick_line(696, 36, 786, 146, 52))
    shapes.append(thick_line(876, 36, 786, 146, 52))
    shapes.append(rect(758, 128, stem, 128))
    return shapes


def svg():
    paths = "\n".join(f'    <path d="{d(shape)}"/>' for shape in letters())
    # Lower chevron only. The upper peak belonged to the LX line and is absent.
    chevron = "M 36 286 L 462 378 L 888 286 L 820 286 L 462 344 L 104 286 Z"
    return f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 930 420" role="img" aria-labelledby="title desc">
  <title id="title">NSTY</title>
  <desc id="desc">Angular NSTY wordmark. The upper line of the source mark is not included.</desc>
  <defs>
    <linearGradient id="metal" gradientUnits="userSpaceOnUse" x1="0" y1="20" x2="40" y2="400">
      <stop offset="0" stop-color="#f7f8fa"/>
      <stop offset="0.18" stop-color="#c5ced8"/>
      <stop offset="0.36" stop-color="#8d98a4"/>
      <stop offset="0.48" stop-color="#f3f5f7"/>
      <stop offset="0.62" stop-color="#5d6670"/>
      <stop offset="0.78" stop-color="#d5dbe2"/>
      <stop offset="1" stop-color="#9aa3ad"/>
    </linearGradient>
    <filter id="plate" x="-8%" y="-8%" width="120%" height="130%">
      <feOffset dx="0" dy="5" in="SourceAlpha" result="off"/>
      <feFlood flood-color="#2a3036" result="ink"/>
      <feComposite in="ink" in2="off" operator="in" result="shadow"/>
      <feMerge>
        <feMergeNode in="shadow"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
  </defs>
  <g fill="url(#metal)" stroke="#121416" stroke-width="3" stroke-linejoin="miter" filter="url(#plate)">
{paths}
    <path d="{chevron}"/>
  </g>
</svg>
'''


def main():
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(svg(), encoding="utf-8")
    fav = OUT.with_name("favicon.svg")
    fav.write_text(svg(), encoding="utf-8")
    print(OUT)


if __name__ == "__main__":
    main()
