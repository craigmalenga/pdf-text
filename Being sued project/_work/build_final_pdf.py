#!/usr/bin/env python3
"""Build the final legal analysis PDF combining facts, analysis, critiques, and email draft."""

import os
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
        content: "Naissance v. Curatela Gavioli — Legal Analysis";
        font-family: Calibri, sans-serif;
        font-size: 9pt;
        color: #666;
    }
}
body {
    font-family: Calibri, Arial, sans-serif;
    font-size: 11pt;
    line-height: 1.4;
    color: #202020;
}
h1 {
    color: #1a365d;
    border-bottom: 2px solid #1a365d;
    padding-bottom: 6px;
    font-size: 18pt;
    page-break-before: always;
}
h1:first-of-type {
    page-break-before: avoid;
}
h2 {
    color: #2c5282;
    font-size: 14pt;
    margin-top: 1em;
}
h3 {
    color: #2c5282;
    font-size: 12pt;
}
table {
    border-collapse: collapse;
    width: 100%;
    margin: 1em 0;
    font-size: 10pt;
}
th, td {
    border: 1px solid #ccc;
    padding: 6px 8px;
    text-align: left;
    vertical-align: top;
}
th {
    background-color: #e6eef7;
    font-weight: bold;
}
code {
    background-color: #f4f4f4;
    padding: 1px 4px;
    border-radius: 2px;
    font-family: Consolas, monospace;
    font-size: 10pt;
}
blockquote {
    border-left: 4px solid #2c5282;
    margin: 1em 0;
    padding-left: 12px;
    color: #333;
    font-style: italic;
}
ul, ol {
    margin-left: 1em;
}
strong, b {
    color: #1a365d;
}
hr {
    border: none;
    border-top: 1px solid #ccc;
    margin: 1em 0;
}
.cover {
    text-align: center;
    margin-top: 4cm;
}
.cover h1 {
    border: none;
    font-size: 24pt;
}
.cover .subtitle {
    font-size: 14pt;
    color: #666;
    margin-top: 1em;
}
.cover .meta {
    margin-top: 3em;
    font-size: 11pt;
}
.warning {
    background-color: #fff3cd;
    border: 1px solid #ffc107;
    padding: 10px;
    margin: 1em 0;
}
"""

COVER_HTML = """
<div class="cover">
<h1>Legal Analysis &amp; Recommended Strategy</h1>
<div class="subtitle">Curatela Fallimento Agricola Gavioli S.r.l. v. Naissance (UK) Limited</div>
<div class="subtitle">Case 2505/2025 R.G. &mdash; Tribunale di Siena</div>
<div class="meta">
<p><b>Prepared for:</b> Grahame McGirr, Director, Naissance UK Limited</p>
<p><b>Amount in dispute:</b> EUR 57,536.75 + legal interest + costs</p>
<p><b>Hearing:</b> 14 May 2026 at 10:00 (Judge Marianna Serrao)</p>
<p><b>Costituzione deadline:</b> 04 May 2026</p>
<p><b>Prepared by:</b> AI analysis with 5 independent critique agents</p>
</div>
</div>
"""

TABLE_OF_CONTENTS = """
<h1>Contents</h1>
<ol>
<li>Part 1 &mdash; The Facts</li>
<li>Part 2 &mdash; Strategic Options (Approaches 1-4)</li>
<li>Part 3 &mdash; Critique Summary (5 Independent Agents)</li>
<li>Part 4 &mdash; Final Recommended Approach</li>
<li>Part 5 &mdash; Draft Email to Avv. Belardi (Italian)</li>
<li>Appendix A &mdash; Key Case Law References</li>
<li>Appendix B &mdash; Evidentiary Gaps to Close</li>
</ol>
"""


def read_md(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()


def md_to_html(md):
    return markdown.markdown(md, extensions=['tables', 'fenced_code', 'toc'])


def build_pdf():
    parts = []

    parts.append(COVER_HTML)
    parts.append(TABLE_OF_CONTENTS)

    # Main analysis
    analysis = read_md(BASE / "_work" / "FINAL_ANALYSIS.md")
    parts.append(md_to_html(analysis))

    # Critiques
    parts.append("<h1>Part 3 (Extended) — Full Critique Reports</h1>")
    parts.append("<p><i>Below are the full reports from the 5 independent critique agents who reviewed the first-draft analysis. Their feedback drove the revisions in Part 4.</i></p>")
    critiques = read_md(BASE / "_work" / "CRITIQUES.md")
    parts.append(md_to_html(critiques))

    # Draft email
    parts.append("<h1>Part 5 — Draft Email to Avv. Belardi (Italian)</h1>")
    parts.append("<p><i>A copy of this email is also provided as an Outlook-compatible <code>.eml</code> file in the output folder. Subject: \"Re: Procedimento Curatela Fallimento Agricola Gavioli — Istruzioni difensive e linea strategica\".</i></p>")
    email_md = read_md(BASE / "_work" / "draft_email_to_belardi.md")
    parts.append(md_to_html(email_md))

    # Appendix A
    parts.append("""
<h1>Appendix A — Key Case Law References</h1>

<h3>Cited by trustee (against us)</h3>
<ul>
<li><b>Cass. 28.09.2018 n. 23482</b> — surplus from individual foreclosure is provisional, subject to bankruptcy restitution</li>
<li><b>Cass. 20.04.2022 n. 12673</b> — reinforces the same principle; restitution operates ex lege</li>
</ul>

<h3>Additional authorities (identified via critique)</h3>
<ul>
<li><b>Cass. SS.UU. 22.12.2015 n. 25749</b> — bankruptcy supersedes individual enforcement for final ranking</li>
<li><b>Cass. 09.07.2014 n. 15724</b> — restitution of spese anticipate rientranti nell'attivo</li>
<li><b>Cass. SS.UU. 23.02.2010 n. 4309</b> — exclusivity of accertamento del passivo; admission decrees cannot be collaterally attacked</li>
<li><b>Cass. 19.11.2018 n. 29849</b> — irreversibility of the admitted passivo</li>
<li><b>Trib. Milano 14.03.2019</b> — distribution plan subordinate to concorso</li>
</ul>

<h3>Primary legislation</h3>
<ul>
<li><b>Art. 41 TUB</b> (D. Lgs. 385/1993) — credit fondiario creditor's right to foreclose during bankruptcy</li>
<li><b>Art. 52 Legge Fallimentare</b> (now CCII art. 151) — concorso formale</li>
<li><b>Art. 96 L.F.</b> — admission of credits</li>
<li><b>Art. 98-99 L.F.</b> — opposition to state of liabilities (30-day window)</li>
<li><b>Art. 110 L.F.</b> — formation of distribution plan</li>
<li><b>Art. 111 L.F.</b> (now CCII art. 221) — prededuzioni and privilegi</li>
<li><b>Art. 281-decies c.p.c.</b> — simplified procedure (requested conversion to ordinary)</li>
<li><b>Art. 281-undecies c.p.c.</b> — 10-day pre-hearing costituzione deadline</li>
<li><b>Art. 512 c.p.c.</b> — contestation of distribution plan</li>
<li><b>Art. 1284 co. 4 c.c.</b> — commercial interest rate</li>
<li><b>Art. 2770 c.c.</b> — privilegi for procedural expenses</li>
<li><b>Art. 2855 c.c.</b> — limits on mortgage ranking for interest</li>
</ul>
""")

    # Appendix B
    parts.append("""
<h1>Appendix B — Evidentiary Gaps to Close Before Hearing</h1>

<table>
<tr><th>Factual assertion</th><th>Current evidence</th><th>Gap</th><th>How to close</th></tr>
<tr>
<td>Naissance paid €130,000+ in costs</td>
<td>5 Thomas Exchange emails showing €77,000 (€57k on 26.04.2018 + €20k on 01.05.2018)</td>
<td>€53,000 unsupported</td>
<td>Produce cheque images, clearing bank statements, or counterparty receipts for the €30k + €45k second tranche; or accept the figure cannot be proved</td>
</tr>
<tr>
<td>The €30,000 was a cost paid, not a refund</td>
<td>Trustee's own ricorso says it was a refund of procedural advance</td>
<td>Internally contradicts the €130k narrative</td>
<td>Reconcile Grahame's own records; if it was a refund, remove from "costs paid" total</td>
</tr>
<tr>
<td>Market-value offers at €550k, €620k, €630k</td>
<td>None in file — only mentioned in Grahame's email to Belardi</td>
<td>Hearsay unless produced</td>
<td>Locate original written offers with dates, signatures, counterparties</td>
</tr>
<tr>
<td>04.04.2019 distribution plan final, unchallenged</td>
<td>Trustee's ricorso refers to the plan but not the verbale</td>
<td>Procedural record not in our file</td>
<td>Demand production under art. 210 c.p.c.: verbale, attendance list, curator observations, art. 512 c.p.c. deadline computation</td>
</tr>
<tr>
<td>Credit was genuinely €1,188,438.29</td>
<td>Credit cession contracts (Banca CRAS → Argo → Naissance)</td>
<td>Trustee already concedes — less critical than it feels</td>
<td>Keep documents available but do NOT lead with this argument</td>
</tr>
<tr>
<td>Steve McGirr's position is not adverse</td>
<td>Unclear from the file</td>
<td>Potential conflict of interest or witness issue</td>
<td>Obtain written confirmation of Steve's role vs Naissance UK; consider privilege/conflict</td>
</tr>
<tr>
<td>Reason for not responding to 02.05.2025 and 03.06.2025 diffide</td>
<td>None on file</td>
<td>Court will infer bad faith / acquiescence</td>
<td>Document what happened — was it service defect, misrouting via Fiorilli, internal oversight? Have a clear explanation</td>
</tr>
</table>
""")

    html_body = "".join(parts)
    full_html = f"<!DOCTYPE html><html><head><meta charset='utf-8'><title>Legal Analysis — Naissance v. Curatela Gavioli</title></head><body>{html_body}</body></html>"

    OUT.mkdir(parents=True, exist_ok=True)
    out_path = OUT / "06_Legal_Analysis_and_Strategy.pdf"
    HTML(string=full_html).write_pdf(out_path, stylesheets=[CSS(string=CSS_STYLE)])
    print(f"Saved: {out_path}")


if __name__ == '__main__':
    build_pdf()
