# OCR Pipeline: 20 Hornton Street Lease Documents → Word

## Goal

Take 4 scanned-PDF lease documents, run image preprocessing + OCR on each page, and produce 4 `.docx` files containing the cleaned-up text. One `.docx` per input PDF, same stem name.

## Inputs

Place the 4 PDFs in `./input/`:

```
input/
├── 20_Hornton_Street_Flat_1_License_for_Consulting_--_1973.pdf       (4 pages)
├── 20_Hornton_Street_Flat_1_License_for_Consulting_--b_1973.pdf      (4 pages)
├── 20_Hornton_Street_Flat_1_Sublease_to_Newnhams_--_1973.pdf         (26 pages)
└── 20_Hornton_Street_License_for_Conversion_--_1972.pdf              (11 pages)
```

These are 1972/73 photocopied/typewritten English property-law deeds. Heavy black scan borders, faint ink in places, marginal annotations, and lots of `OCR-confusable` letter pairs (rn↔m, l↔1, 0↔O). Single-column body text on every page except the floor-plan page (page 26 of the sublease) which is a hand-annotated architectural drawing — OCR will be near-useless on that page; just emit a `[Architectural floor plan — see original PDF page 26]` placeholder for it.

## Outputs

```
output/
├── 20_Hornton_Street_Flat_1_License_for_Consulting_--_1973.docx
├── 20_Hornton_Street_Flat_1_License_for_Consulting_--b_1973.docx
├── 20_Hornton_Street_Flat_1_Sublease_to_Newnhams_--_1973.docx
└── 20_Hornton_Street_License_for_Conversion_--_1972.docx
```

## System dependencies

```bash
sudo apt-get install -y tesseract-ocr poppler-utils
pip install pillow pytesseract python-docx
```

(On macOS: `brew install tesseract poppler`)

## Project layout

```
.
├── input/                              # PDFs (read-only)
├── output/                             # Final .docx files
├── work/
│   ├── images/<pdf_stem>/page_NNN_pp.png   # preprocessed page images (debug)
│   └── ocr/<pdf_stem>/page_NNN.txt          # per-page OCR text (checkpoints)
├── ocr_pipeline.py
├── build_docx.py
└── run.py
```

The `work/ocr/` directory is the **checkpoint store**. Both scripts are idempotent — if `page_NNN.txt` already exists and is non-empty, it's reused. Safe to interrupt and restart.

## `ocr_pipeline.py` — preprocessing + OCR for one page

Implementation that has been validated on these specific scans. **Use these exact parameters** — they were tuned on these PDFs and other settings produced significantly worse output.

```python
#!/usr/bin/env python3
"""Preprocess + OCR one page of a PDF. Idempotent."""
import sys, subprocess
from pathlib import Path
from PIL import Image, ImageOps, ImageFilter
import pytesseract

DPI = 350  # high-res needed for these photocopies
DARK_BORDER_THRESHOLD = 40
BINARIZATION_THRESHOLD = 165


def trim_dark_border(img: Image.Image) -> Image.Image:
    """Crop away the heavy black scan border."""
    g = img.convert("L")
    mask = g.point(lambda p: 255 if p > DARK_BORDER_THRESHOLD else 0)
    bbox = mask.getbbox()
    if not bbox:
        return img
    pad = 20
    l, t, r, b = bbox
    l = max(0, l - pad); t = max(0, t - pad)
    r = min(img.size[0], r + pad); b = min(img.size[1], b + pad)
    return img.crop((l, t, r, b))


def preprocess(img: Image.Image) -> Image.Image:
    g = img.convert("L")
    g = trim_dark_border(g)
    g = ImageOps.autocontrast(g, cutoff=2)
    g = g.filter(ImageFilter.MedianFilter(size=3))      # despeckle
    g = g.filter(ImageFilter.UnsharpMask(radius=1.2, percent=130, threshold=2))
    return g.point(lambda p: 255 if p > BINARIZATION_THRESHOLD else 0, mode="1")


def ocr_page(pdf_path: str, page_num: int, work_dir: str) -> str:
    work = Path(work_dir)
    stem = Path(pdf_path).stem
    img_dir = work / "images" / stem
    txt_dir = work / "ocr" / stem
    img_dir.mkdir(parents=True, exist_ok=True)
    txt_dir.mkdir(parents=True, exist_ok=True)

    txt_path = txt_dir / f"page_{page_num:03d}.txt"
    if txt_path.exists() and txt_path.stat().st_size > 0:
        return txt_path.read_text(encoding="utf-8")

    out_prefix = img_dir / f"page_{page_num:03d}"
    subprocess.run(
        ["pdftoppm", "-png", "-gray", "-r", str(DPI),
         "-f", str(page_num), "-l", str(page_num),
         pdf_path, str(out_prefix)],
        check=True, capture_output=True,
    )
    raw = sorted(img_dir.glob(f"page_{page_num:03d}*.png"))[0]

    img = preprocess(Image.open(raw))
    pp_path = img_dir / f"page_{page_num:03d}_pp.png"
    img.save(pp_path)

    # PSM 4 = "single column of variable-sized text" — best fit for these
    # legal pages with marginal annotations. OEM 1 = LSTM only.
    config = "--oem 1 --psm 4"
    text = pytesseract.image_to_string(str(pp_path), lang="eng", config=config)

    # Drop pure-noise lines (1-2 isolated punctuation chars); keep paragraph structure
    cleaned_lines = []
    for line in text.splitlines():
        s = line.rstrip()
        stripped = s.strip()
        if len(stripped) <= 2 and not any(c.isalnum() for c in stripped):
            continue
        cleaned_lines.append(s)
    cleaned = "\n".join(cleaned_lines)

    txt_path.write_text(cleaned, encoding="utf-8")
    raw.unlink(missing_ok=True)  # keep only preprocessed image
    return cleaned


if __name__ == "__main__":
    pdf_path, page, work_dir = sys.argv[1], int(sys.argv[2]), sys.argv[3]
    text = ocr_page(pdf_path, page, work_dir)
    print(f"OK {Path(pdf_path).stem} p{page}: {len(text)} chars")
```

### Things that were tried and rejected

- **`preserve_interword_spaces=1`** — preserves layout but propagates the noisy whitespace from the scan into the output. Drop it.
- **PSM 6 (uniform block)** — slightly worse on pages with marginal text/annotations.
- **No binarisation** — works but is ~15% slower and gives no quality improvement on these scans.
- **Higher threshold (e.g. 200)** — eats faint strokes in the typewritten text.

## `build_docx.py` — assemble per-page text into one Word file

Use `python-docx` (not docx-js — Python is enough here and avoids the Node dependency). Each PDF becomes one `.docx`. Each page becomes a heading (`Page N`) followed by the OCR text as paragraphs, with a page break between pages so the structure mirrors the original.

```python
#!/usr/bin/env python3
"""Build one .docx per PDF from per-page OCR text files."""
from pathlib import Path
from docx import Document
from docx.shared import Pt, Inches
from docx.enum.text import WD_BREAK


def build_docx(pdf_stem: str, ocr_dir: Path, out_path: Path,
               total_pages: int, special_pages: dict[int, str] | None = None):
    """special_pages: page number -> placeholder text (e.g. for a floor plan)."""
    special_pages = special_pages or {}
    doc = Document()

    # Page setup: A4 with 1" margins (these are UK deeds)
    for section in doc.sections:
        section.page_height = Inches(11.69)
        section.page_width = Inches(8.27)
        section.top_margin = Inches(1)
        section.bottom_margin = Inches(1)
        section.left_margin = Inches(1)
        section.right_margin = Inches(1)

    # Default body font
    style = doc.styles["Normal"]
    style.font.name = "Georgia"
    style.font.size = Pt(11)

    # Title
    title = doc.add_heading(pdf_stem.replace("_", " "), level=1)

    for page_num in range(1, total_pages + 1):
        if page_num > 1:
            # Page break before every page after the first
            run = doc.add_paragraph().add_run()
            run.add_break(WD_BREAK.PAGE)

        doc.add_heading(f"Page {page_num}", level=2)

        if page_num in special_pages:
            p = doc.add_paragraph()
            r = p.add_run(special_pages[page_num])
            r.italic = True
            continue

        txt_path = ocr_dir / pdf_stem / f"page_{page_num:03d}.txt"
        if not txt_path.exists():
            doc.add_paragraph(f"[OCR missing for page {page_num}]")
            continue

        text = txt_path.read_text(encoding="utf-8")
        # Split into paragraphs on blank lines; collapse single newlines to spaces
        # within a paragraph (typewritten lines often wrap mid-sentence).
        paragraphs = []
        buf = []
        for line in text.splitlines():
            if line.strip() == "":
                if buf:
                    paragraphs.append(" ".join(buf))
                    buf = []
            else:
                buf.append(line.strip())
        if buf:
            paragraphs.append(" ".join(buf))

        for para in paragraphs:
            doc.add_paragraph(para)

    out_path.parent.mkdir(parents=True, exist_ok=True)
    doc.save(out_path)
    print(f"Wrote {out_path} ({total_pages} pages)")
```

## `run.py` — orchestrator

```python
#!/usr/bin/env python3
"""Run OCR for all pages of all PDFs in parallel, then build the .docx files."""
import subprocess
from pathlib import Path
from concurrent.futures import ProcessPoolExecutor, as_completed
import os

from build_docx import build_docx

ROOT = Path(__file__).parent
INPUT = ROOT / "input"
OUTPUT = ROOT / "output"
WORK = ROOT / "work"
PIPELINE = ROOT / "ocr_pipeline.py"

# Page 26 of the sublease is a floor plan — don't try to OCR it as text.
SPECIAL = {
    "20_Hornton_Street_Flat_1_Sublease_to_Newnhams_--_1973": {
        26: "[Architectural floor plan — basement and ground floor of "
            "Flat 1, 20 Hornton Street. See original PDF page 26 for the drawing.]",
    },
}


def page_count(pdf: Path) -> int:
    out = subprocess.check_output(["pdfinfo", str(pdf)], text=True)
    for line in out.splitlines():
        if line.startswith("Pages:"):
            return int(line.split(":", 1)[1].strip())
    raise RuntimeError(f"Could not get page count for {pdf}")


def run_one(pdf_path: str, page: int) -> tuple[str, int, bool, str]:
    try:
        r = subprocess.run(
            ["python3", str(PIPELINE), pdf_path, str(page), str(WORK)],
            capture_output=True, text=True, timeout=180,
        )
        return (pdf_path, page, r.returncode == 0,
                (r.stderr or r.stdout)[-200:])
    except Exception as e:
        return (pdf_path, page, False, str(e)[-200:])


def main():
    pdfs = sorted(INPUT.glob("*.pdf"))
    if not pdfs:
        raise SystemExit("No PDFs found in ./input/")

    # Build job list, skipping pages already OCR'd (idempotent restart)
    jobs = []
    for pdf in pdfs:
        n = page_count(pdf)
        for p in range(1, n + 1):
            # Skip the floor plan page entirely
            if (pdf.stem in SPECIAL) and (p in SPECIAL[pdf.stem]):
                continue
            txt = WORK / "ocr" / pdf.stem / f"page_{p:03d}.txt"
            if txt.exists() and txt.stat().st_size > 0:
                continue
            jobs.append((str(pdf), p))

    print(f"OCR jobs to run: {len(jobs)}")
    workers = max(1, (os.cpu_count() or 2))
    print(f"Using {workers} parallel workers")

    failures = []
    with ProcessPoolExecutor(max_workers=workers) as ex:
        futures = {ex.submit(run_one, pdf, p): (pdf, p) for pdf, p in jobs}
        done = 0
        for fut in as_completed(futures):
            pdf, p, ok, msg = fut.result()
            done += 1
            status = "OK" if ok else "FAIL"
            print(f"  [{done}/{len(jobs)}] {status} {Path(pdf).name} p{p}")
            if not ok:
                failures.append((pdf, p, msg))

    if failures:
        print(f"\n{len(failures)} OCR failures — see messages above. "
              f"Re-run to retry only the failed pages.")

    print("\nBuilding .docx files...")
    for pdf in pdfs:
        n = page_count(pdf)
        build_docx(
            pdf_stem=pdf.stem,
            ocr_dir=WORK / "ocr",
            out_path=OUTPUT / f"{pdf.stem}.docx",
            total_pages=n,
            special_pages=SPECIAL.get(pdf.stem),
        )

    print("\nDone.")


if __name__ == "__main__":
    main()
```

## How to run

```bash
mkdir -p input output work
# place the 4 PDFs in input/
python3 run.py
```

Expected runtime: ~30s/page sequentially. With N CPU cores, roughly `45 × 30 / N` seconds. On a 4-core laptop ≈ 6 minutes, on an 8-core ≈ 3 minutes.

## Acceptance criteria

1. `output/` contains exactly 4 `.docx` files, one per input PDF, named with the same stem.
2. Each .docx opens cleanly in Word and has page-break separation between original PDF pages.
3. Page 26 of the sublease docx contains the floor-plan placeholder (not garbage OCR).
4. Spot-check page 1 of the consulting licence — it should clearly contain `JOHN GORE PHILLIMORE`, `RIENZI FELIZ MORITZ FERNANDO`, `CLAUDE TRISTRAM NEWNHAM`, `EVELYN MARY CORNWALL NEWNHAM`, and the date `13th day of April 1973`. If any of those names are mangled beyond recognition, OCR has regressed — re-check preprocessing parameters.
5. Re-running `python3 run.py` after success should be a near-instant no-op (idempotent).

## Optional post-processing (nice-to-have, not required)

Old typewritten English property documents have very predictable OCR errors. After the basic build works, consider a pass that fixes the most common ones across all `.docx` files:

| OCR | Should be |
|-----|-----------|
| `Phillinore`, `PHILLINORE`, `PHILLIMHORE` | `Phillimore`, `PHILLIMORE` |
| `Newnean`, `NEWNEAM`, `NEUNHAM` | `Newnham`, `NEWNHAM` |
| `Coonwall`, `COONWALL` | `Cornwall`, `CORNWALL` |
| `Underlessoes` | `Underlessees` |
| `Licensoo`, `Licensoe` | `Licensee` |
| `Hornton Streot` | `Hornton Street` |
| `12G Stuart Tower` | `12C Stuart Tower` (verify against original) |

Apply these as global find/replace, then leave anything ambiguous to a human reader. Don't try to "fix" OCR by guessing — flag uncertain corrections in a separate `corrections.log` instead.
