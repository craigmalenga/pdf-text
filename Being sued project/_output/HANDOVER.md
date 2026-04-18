# Session handover — resume-from-scratch brief

**Purpose.** If this session times out or the user opens a fresh session,
this document contains everything needed to resume the work without
re-reading the conversation history. Keep it up to date.

**Repo.** `craigmalenga/pdf-text`
**Working branch.** `claude/commit-critique-feedback-0RJTx`
**Project root.** `/home/user/pdf-text/Being sued project/`

---

## What the case is (one paragraph)

Curatela Fallimento Agricola Gavioli S.r.l. v. Naissance (UK) Ltd at
Tribunale di Siena (R.G. **2505/2025**; Fallimento **35/2018 R.G.**;
hearing **14.05.2026** at 10:00, Judge Marianna Serrao; costituzione
deadline **04.05.2026**). The trustee seeks **€57,536.75** plus
interest from 01.07.2025 plus costs. Arithmetic: Naissance received
**€629,975.04** via foreclosure minus **€572,438.29** admitted at
passivo = **€57,536.75** difference. Legal basis: art. 110 L.F. +
Cass. 23482/2018 + Cass. 12673/2022 + art. 41 TUB. Defendant is
**Naissance UK Ltd**, not Grahame personally. Naissance's current
Italian lawyer is Avv. Primo Belardi. The 2018 Istanza was drafted by
Avv. Paolo Fiorilli of Rome.

## Cast

- **Grahame McGirr** — director of Naissance UK Ltd; Craig's cousin;
  the ultimate client of this analysis.
- **Craig Malenga** — the user of this session; prepared this report
  for Grahame.
- **Avv. Primo Belardi** — current Italian lawyer, Chianciano.
- **Avv. Paolo Fiorilli** — prior lawyer (Rome) who drafted the
  2018 Istanza. Grahame had **no direct contact with him**;
  instruction ran through Argo Ge.Re.Cre.
- **Avv. Fabio Finetti** — trustee's lawyer.
- **Dott. Stefano Scarpellini** — curator.
- **Dott.ssa Marianna Serrao** — judge (Siena, Sezione Unica Civile).

## Key verified numbers

- €1,188,438.29 — credit acquired by Naissance via 2017 double
  assignment (Banca CRAS → Argo → Naissance)
- €616,000 — property auction-assignment price (26.06.2018 decree)
- €572,438.29 — mortgage claim admitted to passivo (2019)
- €4,761.47 — prededuzione for legal fees; excluded by G.D.
- €577,199.76 — total requested in Istanza (572,438.29 + 4,761.47)
- €13,975.04 — extra sums beyond the auction price:
  - €10,043.04 "higher amount distributed, net of procedural
    expenses advanced"
  - €3,932.00 "legal expenses not admitted to bankruptcy"
- **€629,975.04** — trustee's "received" figure (= 616k + 13,975.04)
- **€57,536.75** — the claim (629,975.04 − 572,438.29)
- Naissance cost outflows documented: €57k wire (26.04.2018) + €20k
  wire (01.05.2018) + €30k cheque/wire (05.06.2018 — same payment) +
  €45k cheque = **€152,000** (≈ the "€132k" Grahame references).
- Pre-auction expressions of interest: €550k (06.09.2017), €620k
  (12.09.2017). The €630k "accepted transaction" never happened —
  Grahame confirmed no evidence.

## The €30k question — now settled

An earlier draft treated the €30k as a "double-count" attack. The
anti-collusion critique (Agents L3 and D5, independently) found that
is a misreading of the Ricorso. v6 reframed it as a factual
challenge. **v7 is to strip it out entirely.** Grahame's WhatsApp
feedback (18.04.2026 20:25, 20:32, 21:19–22) is that the €30k is
"completely irrelevant", "littered" through the report, and if it
is mentioned again he will lose confidence in the analysis. His
commercial framing is: he spent €132k to recover an asset worth at
most €620k on a credit of €1,188,438.29 — so he is ~€700k
underwater. That is the story v7 should centre on.

## What has been produced so far

In `Being sued project/_output/`:

| File | Purpose |
|---|---|
| 01-05 (`*.docx`) | Source evidence bundles (compiled from OCR of screenshots) |
| 06_Legal_Analysis_and_Strategy.pdf | First pass |
| 07/08 | Old email drafts (.eml + English PDF) — SUPERSEDED |
| 09_Revised_Analysis_v2.md | WIP analysis (superseded) |
| 10_FINAL_REPORT.pdf | v1 (superseded; contained drift the first ChatGPT review flagged) |
| 11_CHATGPT_REVIEW_PROMPT.md | v1 review prompt (superseded) |
| 12_PROJECT_PLAN.md | Live project plan |
| 13_Late_Additions_Analysis.md | What the 13 late-addition email PDFs added |
| 14 | (unused) |
| 15_FINAL_REPORT_v2.pdf | Superseded |
| 16_FINAL_REPORT_v3.pdf | Superseded |
| 17_CHATGPT_REVIEW_PROMPT_v3.md | Review prompt (still useful template) |
| 18_FINAL_REPORT_v4.pdf | Superseded |
| 19_Draft_email_to_Belardi_v3.eml | Superseded (to be replaced) |
| 20_Draft_email_to_Belardi_v3_ENGLISH.pdf | Superseded (to be replaced) |
| 21_Stage_6B_Critique_Findings.md | Anti-collusion findings |
| 22_FINAL_REPORT_v5.pdf | Superseded |
| **23_FINAL_REPORT_v6.pdf** | **Current report** (22 pages, landscape on p20). Still contains €30k references. |
| FINAL_REPORT_v6.md | Source markdown for v6 |

## What v7 must do (the remaining work)

1. **Strip the €30k narrative.** Everywhere. The only place it stays
   is a single short note saying "at Grahame's direction, and on a
   proper reading of the Ricorso, the €30,000 argument has not been
   pursued." No §5.3 long treatment, no reference in §6.4, no line
   in the landscape table, no mention in exec summary, no mention in
   §10.
2. **Centre §9 around Grahame's math.** €132k in costs + property
   worth (best offer) €620k = net recovery €488k vs €1,188,438.29
   credit = **~€700k underwater**. This is the commercial reality
   that gets foregrounded. Walkaway / settlement risk math stays
   but is subordinated to this framing.
3. **Update Approach A in §6.1 and the landscape table.** Drop the
   "€1.188m / €572k residual" framing; replace with the cleaner
   €132k/€488k/€700k-underwater version.
4. **Foreground the point that the trustee's €629,975.04 exceeds
   every pre-auction offer (€550k, €620k).** If the asset was
   genuinely worth at most €620k in 2017, the trustee's €629,975.04
   "received" figure includes a non-market-value tail that itself
   is attackable.
5. **Build `24_FINAL_REPORT_v7.pdf`** and commit.
6. **Build `25_Draft_email_to_Belardi_v7_ENGLISH.pdf`**. English only.
   No Italian .eml until Grahame approves the English.
7. **Run a focused anti-collusion review on v7** — 3 lens agents,
   not 8. Each reads source OCR directly, not v7. Focus each one
   specifically to avoid overlap: (a) arithmetic auditor;
   (b) trustee's counsel attacking v7's lines; (c) plain-English
   check — does the report read as coherent and client-safe?

## Tactical guidance for the next session (avoiding timeouts)

- Work in **small, single-purpose edits**; commit between each.
- Do **not** write 500-line markdown files in one Edit call.
- For PDF rebuilds, reuse the v6 build script with a
  filename/version sed; don't rewrite it.
- Avoid cat/tail of the OCR files — use Grep/Read with limits.
- Skip v7 narrative re-write from scratch; it is a **delta** on v6.md.
- If the user asks for "v8" etc., the pattern is:
  `cp FINAL_REPORT_v6.md FINAL_REPORT_vN.md` then small Edits.
- **Commit after every substantive edit** — this file is your
  safety net; so is `git push`. Use the existing branch.
- The English-email builder pattern: one new `build_email_v7_english_pdf.py`
  script modelled on `build_email_v3_english_pdf.py`, with the
  updated body text. No .eml for now.

## Tone guidance

- Grahame is under time pressure and is angry. Keep the report
  tonally neutral but assume he will read it uncharitably if the
  €30k gets mentioned again.
- Do NOT reference his WhatsApp tone in the report itself. Use his
  facts, not his language.
- When in doubt between "legally cautious" and "emotionally
  reassuring", pick legally cautious — the report is a document
  that goes to Belardi, not a hug.

## Project plan for completing v7 (ordered)

| # | Task | Commit after | Expected lines changed |
|---|---|---|---|
| 1 | Write THIS handover file | Yes | n/a |
| 2 | Copy v6.md → v7.md | Yes | 0 |
| 3 | Strip §5.3 €30k content; replace with a 4-line note | Yes | ~80 |
| 4 | Remove €30k from §6.4 (Approach D) Battleground list | Yes | ~25 |
| 5 | Remove €30k from exec summary callout | Yes | ~20 |
| 6 | Remove €30k line from landscape table Approach D | Yes | ~5 |
| 7 | Remove €30k from §10 Grahame's answers | Yes | ~15 |
| 8 | Rewrite §9 around €132k/€488k/€700k-underwater | Yes | ~60 |
| 9 | Update §6.1 Approach A and landscape table Approach A | Yes | ~30 |
| 10 | Sed remaining "€30,000" mentions and adjust text | Yes | variable |
| 11 | Build `24_FINAL_REPORT_v7.pdf` | Yes | n/a |
| 12 | Build `25_Draft_email_to_Belardi_v7_ENGLISH.pdf` | Yes | n/a (new script) |
| 13 | Run 3-agent focused anti-collusion review of v7 | Yes | n/a |
| 14 | Consolidate findings into `26_Stage_6C_Critique_v7.md` | Yes | n/a |
| 15 | If findings require, produce v8 | case by case | — |

## How a fresh session should start

1. Open this file: `Being sued project/_output/HANDOVER.md`.
2. Read `12_PROJECT_PLAN.md` for the full history.
3. Read `21_Stage_6B_Critique_Findings.md` to understand why the
   €30k argument was stripped.
4. Check the latest commit on branch `claude/commit-critique-
   feedback-0RJTx` with `git log --oneline -20`.
5. Resume from the first unchecked item in the project plan above.
6. If in doubt about Grahame's latest position, the canonical
   client instructions are in this handover file (under "The €30k
   question — now settled" and "What v7 must do").

---

*Last updated: 18.04.2026 during the v7 preparation.*
