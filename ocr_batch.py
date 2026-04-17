#!/usr/bin/env python3
"""Process a batch of pages for a given document. Called by agents."""

import sys
import os
import json
import glob

sys.path.insert(0, os.path.dirname(__file__))
from ocr_page import ocr_page

def process_batch(doc_stem, start_page, end_page):
    """Process pages start_page through end_page (inclusive) for the given document."""
    img_dir = f"work/images/{doc_stem}"
    ocr_dir = f"work/ocr/{doc_stem}"
    os.makedirs(ocr_dir, exist_ok=True)

    results = {}
    for page_num in range(start_page, end_page + 1):
        img_path = os.path.join(img_dir, f"page_{page_num:03d}.png")
        if not os.path.exists(img_path):
            print(f"  Skipping page {page_num} - image not found")
            continue

        ocr_path = os.path.join(ocr_dir, f"page_{page_num:03d}.txt")

        # Skip if already processed (idempotent)
        if os.path.exists(ocr_path) and os.path.getsize(ocr_path) > 0:
            print(f"  Page {page_num} already processed, reading existing")
            with open(ocr_path, 'r') as f:
                results[page_num] = f.read()
            continue

        print(f"  Processing page {page_num}...")
        text = ocr_page(img_path, ocr_path)
        results[page_num] = text
        print(f"  Page {page_num} done ({len(text)} chars)")

    return results


if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Usage: ocr_batch.py <doc_stem> <start_page> <end_page>")
        sys.exit(1)

    doc_stem = sys.argv[1]
    start = int(sys.argv[2])
    end = int(sys.argv[3])

    print(f"Processing {doc_stem} pages {start}-{end}")
    results = process_batch(doc_stem, start, end)

    # Print summary
    for page_num in sorted(results.keys()):
        text = results[page_num]
        preview = text[:100].replace('\n', ' ') if text else "(empty)"
        print(f"\n--- Page {page_num} preview ---")
        print(preview + "...")
