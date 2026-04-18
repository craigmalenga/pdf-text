#!/usr/bin/env python3
"""Extract text from all PDFs in Late additions/. Uses pdftotext first
(for text-layer PDFs), then falls back to Tesseract OCR (English + Italian)
for image-based PDFs.

Writes two files per source PDF:
  - <name>.raw.txt       : extracted text (best available)
  - <name>.meta.txt      : extraction metadata + first 50 lines preview
"""

from pathlib import Path
import subprocess
import shutil
import sys

BASE = Path("/home/user/pdf-text/Being sued project")
SRC = BASE / "Late additions"
OUT = BASE / "_work" / "late_additions"
OUT.mkdir(parents=True, exist_ok=True)


def run(cmd, **kw):
    return subprocess.run(cmd, capture_output=True, text=True, **kw)


def extract_text_layer(pdf: Path) -> str:
    """Try pdftotext first (fast, accurate for text-layer PDFs)."""
    proc = run(["pdftotext", "-layout", "-enc", "UTF-8", str(pdf), "-"])
    if proc.returncode == 0:
        return proc.stdout
    return ""


def ocr_pdf(pdf: Path) -> str:
    """OCR each page via pdftoppm + tesseract (eng+ita)."""
    tmp = OUT / f".tmp_{pdf.stem}"
    tmp.mkdir(exist_ok=True)
    try:
        run(["pdftoppm", "-r", "200", "-png", str(pdf), str(tmp / "pg")])
        pages = sorted(tmp.glob("pg-*.png"))
        out = []
        for i, p in enumerate(pages, 1):
            proc = run(["tesseract", str(p), "-", "-l", "eng+ita", "--psm", "3"])
            out.append(f"\n\n===== [OCR page {i}] =====\n\n{proc.stdout}")
        return "".join(out)
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def main():
    pdfs = sorted(SRC.glob("*.pdf"))
    print(f"Found {len(pdfs)} PDFs in {SRC}")
    for pdf in pdfs:
        slug = pdf.stem.replace(" ", "_")
        print(f"\n=== {pdf.name} ===")
        txt = extract_text_layer(pdf)
        method = "pdftotext"
        stripped = txt.strip()
        # If text layer is empty or very thin, fall back to OCR
        if len(stripped) < 80:
            print(f"  text-layer thin ({len(stripped)} chars) - running OCR...")
            txt = ocr_pdf(pdf)
            method = "tesseract OCR (eng+ita)"
        (OUT / f"{slug}.raw.txt").write_text(txt, encoding="utf-8")
        lines = txt.splitlines()
        preview = "\n".join(lines[:50])
        meta = (
            f"SOURCE: {pdf.name}\n"
            f"METHOD: {method}\n"
            f"CHARS:  {len(txt)}\n"
            f"LINES:  {len(lines)}\n"
            f"PAGES (approx): {txt.count(chr(12)) + 1}\n"
            f"---PREVIEW (first 50 lines)---\n{preview}\n"
        )
        (OUT / f"{slug}.meta.txt").write_text(meta, encoding="utf-8")
        print(f"  done: {method}, {len(txt)} chars")


if __name__ == "__main__":
    main()
