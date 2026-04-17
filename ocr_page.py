#!/usr/bin/env python3
"""Process a single page: preprocess image then OCR with Tesseract."""

import sys
import os
from PIL import Image, ImageFilter, ImageOps, ImageEnhance
import pytesseract

def preprocess_image(img_path, save_preprocessed=True):
    """Apply image preprocessing pipeline optimized for scanned typewritten documents."""
    img = Image.open(img_path)

    # 1. Convert to grayscale
    gray = img.convert('L')

    # 2. Trim dark borders (scanners often leave dark edges)
    import numpy as np
    arr = np.array(gray)
    threshold = 40
    mask = arr > threshold
    rows = np.any(mask, axis=1)
    cols = np.any(mask, axis=0)
    if rows.any() and cols.any():
        rmin, rmax = np.where(rows)[0][[0, -1]]
        cmin, cmax = np.where(cols)[0][[0, -1]]
        gray = gray.crop((cmin, rmin, cmax + 1, rmax + 1))

    # 3. Auto-contrast to normalize intensity range
    gray = ImageOps.autocontrast(gray, cutoff=1)

    # 4. Slight median filter to reduce noise while preserving edges
    gray = gray.filter(ImageFilter.MedianFilter(size=3))

    # 5. Sharpen to recover any lost detail
    gray = gray.filter(ImageFilter.UnsharpMask(radius=2, percent=150, threshold=3))

    # 6. Enhance contrast
    enhancer = ImageEnhance.Contrast(gray)
    gray = enhancer.enhance(1.5)

    # 7. Binarize with adaptive-like thresholding
    arr = np.array(gray)
    binary_threshold = 165
    arr = ((arr > binary_threshold) * 255).astype(np.uint8)
    result = Image.fromarray(arr)

    if save_preprocessed:
        preproc_dir = os.path.dirname(img_path).replace('/images/', '/preprocessed/')
        os.makedirs(preproc_dir, exist_ok=True)
        basename = os.path.basename(img_path)
        result.save(os.path.join(preproc_dir, basename))

    return result


def clean_ocr_text(raw_text):
    """Clean OCR output: remove noise lines, normalize whitespace."""
    lines = raw_text.split('\n')
    cleaned = []

    for line in lines:
        stripped = line.strip()

        # Remove lines that are just 1-2 random characters (OCR noise)
        if len(stripped) <= 2 and not stripped.isalnum():
            continue

        # Remove lines that are just punctuation/symbols
        if stripped and all(c in '.,;:!?|\\/-_=+*#@~`^&()[]{}"\'' for c in stripped):
            continue

        # Remove lines that are just repeated characters (e.g., "-----", "=====")
        if stripped and len(set(stripped.replace(' ', ''))) <= 1 and len(stripped) > 3:
            continue

        cleaned.append(line.rstrip())

    # Collapse multiple blank lines to max 2
    result = []
    blank_count = 0
    for line in cleaned:
        if line.strip() == '':
            blank_count += 1
            if blank_count <= 2:
                result.append('')
        else:
            blank_count = 0
            result.append(line)

    return '\n'.join(result).strip()


def ocr_page(img_path, output_path=None):
    """Preprocess and OCR a single page."""
    preprocessed = preprocess_image(img_path)

    # Tesseract config: PSM 4 = single column of variable text, OEM 1 = LSTM
    custom_config = r'--oem 1 --psm 4 -l eng'
    raw_text = pytesseract.image_to_string(preprocessed, config=custom_config)

    cleaned = clean_ocr_text(raw_text)

    if output_path:
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(cleaned)

    return cleaned


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: ocr_page.py <image_path> [output_path]")
        sys.exit(1)

    img_path = sys.argv[1]
    output_path = sys.argv[2] if len(sys.argv) > 2 else None

    text = ocr_page(img_path, output_path)
    if not output_path:
        print(text)
