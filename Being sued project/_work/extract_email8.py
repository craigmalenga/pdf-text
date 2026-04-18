#!/usr/bin/env python3
"""email 8 part N.pdf files are actually raw RFC 822 emails mislabelled
with .pdf. Parse them as emails, extract headers + text body + attachment
list, and write to the late_additions folder alongside the other
extractions."""

from pathlib import Path
from email import policy
from email.parser import BytesParser

BASE = Path("/home/user/pdf-text/Being sued project")
SRC = BASE / "Late additions"
OUT = BASE / "_work" / "late_additions"


def parse_one(pdf: Path) -> str:
    raw = pdf.read_bytes()
    msg = BytesParser(policy=policy.default).parsebytes(raw)
    out = []
    out.append(f"=== HEADERS ===")
    for h in ("From", "To", "Cc", "Subject", "Date", "Message-ID"):
        v = msg.get(h)
        if v:
            out.append(f"{h}: {v}")
    out.append("")
    out.append("=== BODY (text/plain) ===")
    text_part = None
    attachments = []
    if msg.is_multipart():
        for part in msg.walk():
            ctype = part.get_content_type()
            disp = part.get_content_disposition()
            if disp == "attachment":
                attachments.append(
                    f"  - {part.get_filename()} ({ctype}, {len(part.get_payload(decode=True) or b'')} bytes)"
                )
                continue
            if ctype == "text/plain" and text_part is None:
                try:
                    text_part = part.get_content()
                except Exception:
                    text_part = part.get_payload(decode=True).decode(
                        "utf-8", "replace"
                    )
    else:
        try:
            text_part = msg.get_content()
        except Exception:
            text_part = msg.get_payload()
    out.append(text_part or "(no text/plain body)")
    if attachments:
        out.append("")
        out.append("=== ATTACHMENTS ===")
        out.extend(attachments)
    return "\n".join(out)


def main():
    targets = sorted(SRC.glob("email 8 part *.pdf"))
    for pdf in targets:
        slug = pdf.stem.replace(" ", "_")
        print(f"=== {pdf.name} ===")
        try:
            parsed = parse_one(pdf)
        except Exception as e:
            parsed = f"PARSE ERROR: {e}\n\nRAW FIRST 4000 CHARS:\n{pdf.read_text(errors='replace')[:4000]}"
        (OUT / f"{slug}.raw.txt").write_text(parsed, encoding="utf-8")
        print(f"  wrote {len(parsed)} chars")


if __name__ == "__main__":
    main()
