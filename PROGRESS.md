# PDF-to-Word Conversion Progress

## Target: 3 Word Documents
1. `20 Hornton Street Flat 1 License for Consulting -- 1973.docx` (4 pages)
2. `20 Hornton Street Flat 1 Sublease to Newnhams -- 1973.docx` (26 pages, page 26 = floor plan)
3. `20 Hornton Street License for Conversion -- 1972.docx` (11 pages, page 10 = blank)

Note: The two "Consulting" PDFs are identical (same MD5 hash), so only 3 unique documents.

## Pipeline
1. [DONE] PDF → Images at 350 DPI (work/images/)
2. [DONE] Image preprocessing: grayscale → border trim → auto-contrast → median filter → sharpen → binarize (work/preprocessed/)
3. [DONE] Tesseract OCR with PSM 4, OEM 1 (work/ocr/)
4. [DONE] Review & cleanup of OCR text (fix known names, remove noise)
5. [DONE] Build Word documents with cleaned text (output/)

## Key Names (for OCR correction)
- Phillimore (not PHILLINORE, PHILLIMORE)
- Newnham (not NEWNEAN)
- Cornwall (not COOMWALL, CORWIALL)
- Fernando / Rienzi Felix Moritz Fernando (not RIZNZI, RTENZI, KELIZ, FELIZ)
- Mosley / Simon James Mosley

## Files
- ocr_page.py - Single page preprocessing + OCR
- ocr_batch.py - Batch processing script
- build_docx.py - Word document assembly (to be created)
- work/ocr/{doc_stem}/page_NNN.txt - Raw OCR output per page
- output/*.docx - Final Word documents (to be created)

## Completed Output
All 3 Word documents in output/:
- 20 Hornton Street Flat 1 License for Consulting -- 1973.docx (39 KB)
- 20 Hornton Street Flat 1 Sublease to Newnhams -- 1973.docx (51 KB)
- 20 Hornton Street License for Conversion -- 1972.docx (41 KB)

## Quality Notes
- Pages 21, 23, 25 of sublease had very poor scan quality - some sections marked [ILLEGIBLE]
- Page 26 of sublease = architectural floor plan (placeholder text only)
- Page 10 of conversion = blank page
- All proper names corrected to verified spellings
- Legal clause numbering and structure preserved throughout
