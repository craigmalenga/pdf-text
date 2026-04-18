#!/usr/bin/env python3
"""Build the FINAL_REPORT PDF from markdown - journey narrative for Grahame."""

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
        content: "Naissance UK Ltd - Defence Strategy";
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
h2 { color: #2c5282; font-size: 13pt; margin-top: 1em; }
h3 { color: #2c5282; font-size: 11.5pt; }
table {
    border-collapse: collapse;
    width: 100%;
    margin: 0.8em 0;
    font-size: 10pt;
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
blockquote {
    border-left: 3px solid #2c5282;
    margin: 0.8em 0;
    padding-left: 10px;
    color: #444;
    font-style: italic;
}
.cover {
    text-align: center;
    margin-top: 3cm;
    margin-bottom: 2cm;
    padding: 2em 1em;
    border-top: 3px solid #1a365d;
    border-bottom: 3px solid #1a365d;
}
.cover .title {
    color: #1a365d;
    font-size: 22pt;
    font-weight: bold;
    margin-bottom: 0.5em;
}
.cover .subtitle {
    font-size: 13pt;
    color: #444;
    margin-top: 0.5em;
}
.cover .meta {
    margin-top: 2.5em;
    font-size: 11pt;
}
.callout {
    background-color: #fff8e1;
    border-left: 4px solid #f0a500;
    padding: 10px 14px;
    margin: 1em 0;
}
"""

COVER_HTML = """
<div class="cover">
<div class="title">Defence Strategy Report</div>
<div class="subtitle">Naissance UK Ltd v. Curatela Fallimento<br>Societa' Agricola Gavioli S.r.l.</div>
<div class="subtitle" style="margin-top:1.2em;font-size:11pt;">Tribunale di Siena &mdash; Fallimento n. 18/2018</div>
<div class="meta">
<p><b>Prepared for:</b> Grahame McGirr</p>
<p><b>Amount in dispute:</b> EUR 57,536.75 + interest + costs</p>
<p><b>Response deadline:</b> 04 May 2026</p>
<p><b>Date of report:</b> 18 April 2026</p>
</div>
</div>
"""


def build():
    md_text = (OUT / "FINAL_REPORT.md").read_text(encoding="utf-8")
    html_body = markdown.markdown(md_text, extensions=["tables", "fenced_code"])
    full_html = (
        "<!DOCTYPE html><html><head><meta charset='utf-8'>"
        "<title>Defence Strategy Report</title></head><body>"
        + COVER_HTML + html_body + "</body></html>"
    )
    out_path = OUT / "10_FINAL_REPORT.pdf"
    HTML(string=full_html).write_pdf(out_path, stylesheets=[CSS(string=CSS_STYLE)])
    print(f"Saved: {out_path}")


if __name__ == "__main__":
    build()
