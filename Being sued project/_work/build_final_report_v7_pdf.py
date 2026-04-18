#!/usr/bin/env python3
"""Build 24_FINAL_REPORT_v7.pdf from FINAL_REPORT_v7.md - the
standalone fresh report for Grahame."""

from pathlib import Path
import markdown
from weasyprint import HTML, CSS

BASE = Path("/home/user/pdf-text/Being sued project")
OUT = BASE / "_output"

CSS_STYLE = """
@page {
    size: A4;
    margin: 2cm 2cm 2.5cm 2cm;
    @bottom-right {
        content: "Page " counter(page) " of " counter(pages);
        font-family: Calibri, sans-serif;
        font-size: 9pt;
        color: #666;
    }
    @bottom-left {
        content: "Naissance UK Ltd - Defence Strategy Report";
        font-family: Calibri, sans-serif;
        font-size: 9pt;
        color: #666;
    }
}
@page landscape {
    size: A4 landscape;
    margin: 1.2cm 1.5cm 1.8cm 1.5cm;
    @bottom-right {
        content: "Page " counter(page) " of " counter(pages);
        font-family: Calibri, sans-serif;
        font-size: 9pt;
        color: #666;
    }
    @bottom-left {
        content: "Naissance UK Ltd - Defence Strategy Report";
        font-family: Calibri, sans-serif;
        font-size: 9pt;
        color: #666;
    }
}
body {
    font-family: Calibri, Arial, sans-serif;
    font-size: 11pt;
    line-height: 1.45;
    color: #202020;
}
h1 {
    color: #1a365d;
    border-bottom: 2px solid #1a365d;
    padding-bottom: 6px;
    font-size: 17pt;
    margin-top: 1.2em;
}
h1:first-of-type { margin-top: 0; }
h2 { color: #2c5282; font-size: 13pt; margin-top: 1em; page-break-after: avoid; }
h3 { color: #2c5282; font-size: 11.5pt; page-break-after: avoid; }
table {
    border-collapse: collapse;
    width: 100%;
    margin: 0.8em 0;
    font-size: 10pt;
    page-break-inside: avoid;
}
th, td {
    border: 1px solid #bbb;
    padding: 6px 8px;
    text-align: left;
    vertical-align: top;
}
th { background-color: #e6eef7; font-weight: bold; }
strong, b { color: #1a365d; }
hr { border: none; border-top: 1px solid #ccc; margin: 1em 0; }
.cover {
    text-align: center;
    margin-top: 3cm;
    margin-bottom: 2cm;
    padding: 2em 1em;
    border-top: 3px solid #1a365d;
    border-bottom: 3px solid #1a365d;
}
.cover .title { color: #1a365d; font-size: 22pt; font-weight: bold; margin-bottom: 0.5em; }
.cover .subtitle { font-size: 13pt; color: #444; margin-top: 0.5em; }
.cover .meta { margin-top: 2.5em; font-size: 11pt; }
.page-break { page-break-before: always; }

section.landscape-section {
    page: landscape;
    page-break-before: always;
    page-break-after: always;
}
section.landscape-section h3 { margin: 0 0 0.4em 0; page-break-after: avoid; }

table.compare {
    border-collapse: collapse;
    width: 100%;
    font-size: 7.5pt;
    page-break-inside: avoid;
}
table.compare th, table.compare td {
    border: 1px solid #8a9bb3;
    padding: 4px 6px;
    vertical-align: top;
    line-height: 1.25;
}
table.compare th {
    background-color: #1a365d;
    color: white;
    font-weight: bold;
    text-align: left;
    font-size: 8.5pt;
}
table.compare td:first-child {
    text-align: center;
    font-weight: bold;
    font-size: 11pt;
    color: #1a365d;
}
table.compare ul { margin: 0; padding-left: 12px; }
table.compare li { margin-bottom: 2px; }
table.compare tr.recommended { background-color: #e8f4e8; }
table.compare tr.recommended td { border-color: #2f7a2f; }
"""

COVER_HTML = """
<div class="cover">
<div class="title">Defence Strategy Report</div>
<div class="subtitle">Curatela Fallimento Agricola Gavioli S.r.l.<br>v. Naissance (UK) Ltd</div>
<div class="subtitle" style="margin-top:1.2em;font-size:11pt;">Tribunale di Siena, Sezione Unica Civile &mdash; R.G. 2505/2025</div>
<div class="meta">
<p><b>Prepared for:</b> Grahame McGirr</p>
<p><b>Amount in dispute:</b> EUR 57,536.75 + interest from 01.07.2025 + costs</p>
<p><b>Costituzione deadline:</b> 04 May 2026</p>
<p><b>Hearing:</b> 14 May 2026, Judge Marianna Serrao</p>
<p><b>Date of report:</b> 18 April 2026</p>
</div>
</div>
"""


def wrap_landscape_section(html: str) -> str:
    marker_div = '<div class="landscape-page"></div>'
    if marker_div not in html:
        return html
    before, after = html.split(marker_div, 1)
    end_idx = after.find("</table>")
    if end_idx == -1:
        return html
    end_idx += len("</table>")
    return (
        before
        + '<section class="landscape-section">'
        + after[:end_idx]
        + "</section>"
        + after[end_idx:]
    )


def build():
    md_text = (OUT / "FINAL_REPORT_v7.md").read_text(encoding="utf-8")
    html_body = markdown.markdown(
        md_text, extensions=["tables", "fenced_code", "md_in_html"]
    )
    html_body = wrap_landscape_section(html_body)
    full_html = (
        "<!DOCTYPE html><html><head><meta charset='utf-8'>"
        "<title>Defence Strategy Report</title></head><body>"
        + COVER_HTML + html_body + "</body></html>"
    )
    out_path = OUT / "24_FINAL_REPORT_v7.pdf"
    HTML(string=full_html).write_pdf(out_path, stylesheets=[CSS(string=CSS_STYLE)])
    print(f"Saved: {out_path}")


if __name__ == "__main__":
    build()
