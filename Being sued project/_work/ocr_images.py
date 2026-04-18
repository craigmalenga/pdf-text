#!/usr/bin/env python3
"""OCR for photo/screenshot JPGs in the Being sued project folders.

Uses both English and Italian Tesseract models. Applies preprocessing
tuned for phone screenshots (which are usually high-quality digital images,
not scanned typewritten docs).
"""

import os
import sys
from pathlib import Path
from PIL import Image, ImageFilter, ImageOps, ImageEnhance
import numpy as np
import pytesseract

BASE = Path("/home/user/pdf-text/Being sued project")
OCR_DIR = BASE / "_work" / "ocr"


def preprocess_screenshot(img_path):
    """Light preprocessing for digital screenshots/photos.
    These are typically high-quality - minimal processing needed.
    """
    img = Image.open(img_path)

    if img.mode != 'RGB':
        img = img.convert('RGB')

    gray = img.convert('L')

    w, h = gray.size
    if max(w, h) < 2000:
        scale = 2000 / max(w, h)
        new_size = (int(w * scale), int(h * scale))
        gray = gray.resize(new_size, Image.LANCZOS)

    gray = ImageOps.autocontrast(gray, cutoff=1)
    enhancer = ImageEnhance.Contrast(gray)
    gray = enhancer.enhance(1.3)

    return gray


def ocr_image(img_path, lang='eng+ita'):
    """OCR an image with both English and Italian support."""
    processed = preprocess_screenshot(img_path)

    # PSM 6 = assume uniform block of text (good for screenshots/receipts)
    config = r'--oem 1 --psm 6'
    text = pytesseract.image_to_string(processed, lang=lang, config=config)

    return text.strip()


def process_folder(folder_name, out_prefix, lang='eng+ita'):
    """OCR all JPG images in a folder, save to ocr dir with prefix."""
    folder = BASE / folder_name
    if not folder.exists():
        print(f"Folder not found: {folder}")
        return []

    OCR_DIR.mkdir(parents=True, exist_ok=True)

    results = []
    for img_path in sorted(folder.glob("*.jpg")):
        out_name = f"{out_prefix}_{img_path.stem.replace(' ', '_').replace('(', '').replace(')', '')}.txt"
        out_path = OCR_DIR / out_name

        if out_path.exists() and out_path.stat().st_size > 0:
            print(f"  [skip existing] {out_path.name}")
            with open(out_path) as f:
                results.append((img_path.name, f.read()))
            continue

        print(f"  OCR {img_path.name}...")
        text = ocr_image(img_path, lang=lang)
        with open(out_path, 'w', encoding='utf-8') as f:
            f.write(text)
        print(f"    → {out_path.name} ({len(text)} chars)")
        results.append((img_path.name, text))

    return results


if __name__ == '__main__':
    folders = {
        "Advice": ("advice", "eng+ita"),
        "Other AI": ("otherai", "eng"),
        "Receiived": ("receipt", "eng+ita"),
    }

    if len(sys.argv) > 1:
        only = sys.argv[1]
        if only in folders:
            prefix, lang = folders[only]
            print(f"=== Processing {only} ===")
            process_folder(only, prefix, lang)
        else:
            print(f"Unknown folder: {only}")
            sys.exit(1)
    else:
        for folder_name, (prefix, lang) in folders.items():
            print(f"\n=== Processing {folder_name} ===")
            process_folder(folder_name, prefix, lang)
