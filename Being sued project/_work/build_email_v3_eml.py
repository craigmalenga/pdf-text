#!/usr/bin/env python3
"""Build 19_Draft_email_to_Belardi_v3.eml from draft_email_to_belardi_v3.md."""

from email.message import EmailMessage
from email.utils import formatdate
from pathlib import Path
import re

BASE = Path("/home/user/pdf-text/Being sued project")
OUT = BASE / "_output"
SRC_MD = BASE / "_work" / "draft_email_to_belardi_v3.md"


def md_to_plain(md: str) -> str:
    """Strip minimal markdown so the plain-text body is readable."""
    text = md
    # remove front matter and title
    text = re.sub(r"^# .*?\n\n", "", text, count=1, flags=re.DOTALL)
    text = re.sub(r"^\*\*.*?\*\*.*?\n", "", text, count=4, flags=re.MULTILINE)
    # horizontal rules
    text = re.sub(r"^---+\n", "", text, flags=re.MULTILINE)
    # bold / italic
    text = re.sub(r"\*\*(.+?)\*\*", r"\1", text)
    text = re.sub(r"\*(.+?)\*", r"\1", text)
    # headings
    text = re.sub(r"^### (.+)$", r"\1\n", text, flags=re.MULTILINE)
    text = re.sub(r"^## (.+)$", r"\1\n", text, flags=re.MULTILINE)
    return text.strip() + "\n"


def md_to_html(md: str) -> str:
    """Minimal markdown -> HTML for the Outlook body."""
    text = md
    text = re.sub(r"^# .*?\n\n", "", text, count=1, flags=re.DOTALL)
    text = re.sub(r"^\*\*From:\*\*.*?\n", "", text, count=1, flags=re.MULTILINE)
    text = re.sub(r"^\*\*To:\*\*.*?\n", "", text, count=1, flags=re.MULTILINE)
    text = re.sub(r"^\*\*Subject:\*\*.*?\n", "", text, count=1, flags=re.MULTILINE)
    text = re.sub(r"^---+\n", "<hr>\n", text, flags=re.MULTILINE)
    text = re.sub(r"^### (.+)$", r"<h3>\1</h3>", text, flags=re.MULTILINE)
    text = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", text)
    text = re.sub(r"(?<!\*)\*([^*\n]+?)\*(?!\*)", r"<i>\1</i>", text)
    # Convert list items
    text = re.sub(r"^\- (.+)$", r"<li>\1</li>", text, flags=re.MULTILINE)
    # Wrap consecutive <li> in <ul>
    text = re.sub(r"((?:<li>.*?</li>\n?)+)", r"<ul>\n\1</ul>\n", text, flags=re.DOTALL)
    # Paragraphs
    blocks = text.split("\n\n")
    html_blocks = []
    for b in blocks:
        b = b.strip()
        if not b:
            continue
        if b.startswith("<") or b.startswith("- "):
            html_blocks.append(b)
        else:
            html_blocks.append("<p>" + b.replace("\n", "<br>") + "</p>")
    return "\n".join(html_blocks)


BODY_HTML_TEMPLATE = """<html>
<head><meta charset="utf-8"></head>
<body style="font-family: Calibri, Arial, sans-serif; font-size: 11pt; color: #202020;">
{content}
<hr>
<p style="font-size: 9pt; color: #808080;"><i>If you have received this message in error, please notify the sender and immediately delete this message and any attachment hereto and/or copy hereof, as such message contains confidential information intended solely for the individual or entity to whom it is addressed. The use or disclosure of such information to third parties is prohibited by law and may give rise to civil or criminal liability. This e-mail and any attached files are confidential and may be legally privileged or otherwise protected.</i></p>
</body>
</html>
"""


def main():
    md = SRC_MD.read_text(encoding="utf-8")
    plain = md_to_plain(md)
    html = BODY_HTML_TEMPLATE.format(content=md_to_html(md))

    msg = EmailMessage()
    msg["From"] = "Grahame McGirr <gmcgirr@naissance.co.uk>"
    msg["To"] = "Primo Belardi <avv.primobelardi@gmail.com>"
    msg["Subject"] = (
        "Re: Naissance UK Ltd / Curatela Fallimento Agricola Gavioli — "
        "Conferma linea difensiva e integrazioni"
    )
    msg["Date"] = formatdate(localtime=True)
    msg["X-Unsent"] = "1"
    msg.set_content(plain)
    msg.add_alternative(html, subtype="html")

    out_path = OUT / "19_Draft_email_to_Belardi_v3.eml"
    with open(out_path, "wb") as f:
        f.write(bytes(msg))
    print(f"Saved: {out_path}")


if __name__ == "__main__":
    main()
