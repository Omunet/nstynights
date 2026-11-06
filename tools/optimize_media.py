#!/usr/bin/env python3
"""Resize authorised photographs, strip metadata, and write JPEG plus WebP."""

import hashlib
import json
import subprocess
from pathlib import Path

from PIL import Image, ImageOps

ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "deploy" / "test" / "assets" / "media"
META_PATH = ROOT / "sources" / "media" / "derivatives.json"
SEARCH = [
    ROOT / "nsty-assets" / "images",
    ROOT / "sources" / "incoming",
    Path("/home/ubuntu/.cursor/projects/workspace/uploads"),
]
TARGETS = (480, 800, 1200, 1600, 2000)
MAX_EDGE = 2000

ITEMS = [
    ("archive-2025-poster", "nsty-ig-01-DL3a1nkodkW.jpg"),
    ("outdoor-latex", "collab-02-rayn.nyx-DNL0neeiqpj.jpg"),
    ("backstage-latex", "collab-03-rayn.nyx-DKttbxziMY8.jpg"),
    ("monochrome-portrait", "collab-04-artinblack.m-DYFuuUejBmAj.jpg"),
    ("runway", "collab-05-rayn.nyx-DLH8AQbClDA.jpg"),
    ("white-latex", "collab-06-mew_chiel-DLDT0Bos2FG.jpg"),
]


def sha256(path):
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


def find_source(name):
    hits = [base / name for base in SEARCH if (base / name).is_file()]
    if not hits:
        looked = ", ".join(str(base / name) for base in SEARCH)
        raise SystemExit(f"Missing authorised image {name}. Looked in: {looked}")
    return hits[0]


def widths_for(width):
    chosen = [size for size in TARGETS if size < width]
    if width not in chosen:
        chosen.append(width)
    return chosen


def assert_no_metadata(path):
    result = subprocess.run(
        ["exiftool", "-json", "-a", "-G1", str(path)],
        check=True,
        capture_output=True,
        text=True,
    )
    payload = json.loads(result.stdout)[0]
    leftover = [
        key
        for key in payload
        if key not in {"SourceFile", "ExifTool:ExifToolVersion", "File:FileName", "File:Directory", "File:FileSize", "File:FileModifyDate", "File:FileAccessDate", "File:FileInodeChangeDate", "File:FilePermissions", "File:FileType", "File:FileTypeExtension", "File:MIMEType", "File:ImageWidth", "File:ImageHeight", "File:EncodingProcess", "File:BitsPerSample", "File:ColorComponents", "File:YCbCrSubSampling", "JFIF:JFIFVersion", "JFIF:ResolutionUnit", "JFIF:XResolution", "JFIF:YResolution", "Composite:ImageSize", "Composite:Megapixels"}
        and not key.startswith("File:")
        and not key.startswith("Composite:")
        and not key.startswith("JFIF:")
    ]
    # JFIF resolution defaults are not camera EXIF. Reject GPS, camera, and XMP.
    banned_prefixes = ("EXIF:", "GPS:", "IPTC:", "XMP-", "XMP:", "MakerNotes:", "ICC_Profile:")
    serious = [key for key in payload if key.startswith(banned_prefixes)]
    if serious or leftover:
        raise SystemExit(f"Metadata remains on {path}: {serious or leftover}")


def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    META_PATH.parent.mkdir(parents=True, exist_ok=True)
    # Remove previous derivatives so a dropped file cannot linger in the gallery.
    for old in OUT_DIR.iterdir():
        if old.suffix.lower() in {".jpg", ".jpeg", ".webp", ".png"}:
            old.unlink()

    catalog = {}
    for slug, filename in ITEMS:
        source = find_source(filename)
        with Image.open(source) as raw:
            image = ImageOps.exif_transpose(raw)
            if image.mode != "RGB":
                image = image.convert("RGB")
            image = image.copy()
        width, height = image.size
        scale = min(1, MAX_EDGE / max(width, height))
        if scale < 1:
            image = image.resize((round(width * scale), round(height * scale)), Image.Resampling.LANCZOS)
            width, height = image.size

        derivatives = []
        for target in widths_for(width):
            ratio = target / width
            resized = image.resize((target, max(1, round(height * ratio))), Image.Resampling.LANCZOS)
            jpg_name = f"{slug}-{target}.jpg"
            webp_name = f"{slug}-{target}.webp"
            jpg_path = OUT_DIR / jpg_name
            webp_path = OUT_DIR / webp_name
            resized.save(jpg_path, format="JPEG", quality=82, optimize=True, progressive=True)
            subprocess.run(
                ["cwebp", "-quiet", "-q", "78", "-metadata", "none", str(jpg_path), "-o", str(webp_path)],
                check=True,
            )
            assert_no_metadata(jpg_path)
            assert_no_metadata(webp_path)
            derivatives.append(
                {
                    "width": resized.size[0],
                    "height": resized.size[1],
                    "jpg": f"/test/assets/media/{jpg_name}",
                    "webp": f"/test/assets/media/{webp_name}",
                    "jpg_sha256": sha256(jpg_path),
                    "webp_sha256": sha256(webp_path),
                }
            )
        catalog[slug] = {
            "source_filename": filename,
            "source_sha256": sha256(source),
            "source_pixels": list(Image.open(source).size),
            "derivatives": derivatives,
        }
        print(f"{slug}: {width}x{height} from {source.name}")

    META_PATH.write_text(json.dumps(catalog, indent=2) + "\n", encoding="utf-8")
    print(META_PATH)


if __name__ == "__main__":
    main()
