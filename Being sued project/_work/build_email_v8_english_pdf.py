#!/usr/bin/env python3
"""Build 27_Draft_email_to_Belardi_v8_ENGLISH.pdf -- English draft
aligned with v8 (Grahame's call feedback). No circularity, no 30k,
clean 572+132=700 vs 620 = 80k-short pitch."""

from pathlib import Path
from weasyprint import HTML, CSS

BASE = Path("/home/user/pdf-text/Being sued project")
OUT = BASE / "_output"

CSS_STYLE = """
@page { size: A4; margin: 2cm 2cm 2.5cm 2cm;
  @bottom-right { content: "Page " counter(page) " of " counter(pages);
    font-family: Calibri, sans-serif; font-size: 9pt; color: #666; }
  @bottom-left { content: "Draft email to Belardi - v8 English - for review only";
    font-family: Calibri, sans-serif; font-size: 9pt; color: #666; } }
body { font-family: Calibri, Arial, sans-serif; font-size: 11pt; line-height: 1.45; color: #202020; }
h1 { color: #1a365d; font-size: 17pt; border-bottom: 2px solid #1a365d; padding-bottom: 6px; }
h3 { color: #2c5282; font-size: 11.5pt; margin-top: 0.9em; }
.header-note { background-color: #fff8e1; border-left: 4px solid #f0a500;
  padding: 10px 14px; margin: 1em 0 1.5em 0; font-size: 10pt; }
.metadata { font-size: 10pt; color: #555; margin-bottom: 1.5em;
  border-bottom: 1px solid #ccc; padding-bottom: 0.8em; }
strong, b { color: #1a365d; }
ul { margin: 0.4em 0 0.8em 1.2em; } li { margin-bottom: 0.25em; }
hr { border: none; border-top: 1px solid #ccc; margin: 1em 0; }
table { border-collapse: collapse; margin: 0.6em 0; font-size: 10pt; }
th, td { border: 1px solid #bbb; padding: 6px 8px; text-align: left; vertical-align: top; }
th { background-color: #e6eef7; }
"""

HTML_BODY = """<!DOCTYPE html><html><head><meta charset="utf-8"><title>Draft email to Belardi v8 English</title></head><body>

<h1>Draft email to Avv. Primo Belardi &mdash; English</h1>

<div class="header-note">
<b>Note:</b> This is the English draft of the proposed email to Avv.
Belardi, for Grahame's review. The Italian translation will be
produced once this is approved.
</div>

<div class="metadata">
<b>From:</b> Grahame McGirr &lt;gmcgirr@naissance.co.uk&gt;<br>
<b>To:</b> Primo Belardi &lt;avv.primobelardi@gmail.com&gt;<br>
<b>Subject:</b> Naissance UK Ltd / Curatela Fallimento Agricola Gavioli &mdash; defence instructions
</div>

<p>Dear Avv. Belardi,</p>

<p>Thank you for your email of 17 April and for your strategic
analysis. This message confirms my instructions for the defence
and the parallel settlement channel.</p>

<hr>

<h3>1. The commercial reality of this case &mdash; and the argument I want pleaded</h3>

<p>The trustee's claim rests on a narrow restitution theory. The
commercial reality, stated only on the figures the bankruptcy and
the trustee himself have already accepted, is the following:</p>

<table>
<tr><th>Line</th><th>Amount</th><th>Source</th></tr>
<tr><td>Residual mortgage claim admitted to the passivo</td>
    <td>&euro;572,438.29</td>
    <td>Istanza/decree of admission; conceded in the Ricorso</td></tr>
<tr><td>Out-of-pocket recovery costs paid by Naissance</td>
    <td>&euro;132,000</td>
    <td>FX wires (Thomas Exchange UK) + two UBI cost cheques</td></tr>
<tr><td><b>Total exposure admitted / documented</b></td>
    <td><b>~&euro;700,000</b></td><td></td></tr>
<tr><td>Highest genuine pre-auction offer on the asset</td>
    <td>&euro;620,000</td>
    <td>Marco Gavioli email, 12.09.2017, via Gordana Lupi to Argo Ge.Re.Cre.</td></tr>
<tr><td><b>Shortfall at best market view</b></td>
    <td><b>~&euro;80,000</b></td><td></td></tr>
<tr><td>Further amount the trustee now claims</td>
    <td>&euro;57,536.75</td>
    <td>Ricorso prayer</td></tr>
<tr><td><b>Shortfall if the trustee wins</b></td>
    <td><b>~&euro;140,000</b></td><td></td></tr>
</table>

<p>On these numbers:</p>
<ul>
<li>The bankrupt estate has lost nothing that the judicial
procedure did not itself deliver.</li>
<li>Naissance is the only party out of pocket &mdash; by
approximately &euro;80,000 at best market view, or ~&euro;140,000 if
the trustee wins.</li>
<li>The trustee's &quot;received&quot; figure of &euro;629,975.04
itself exceeds every pre-auction offer ever made on the asset,
which is reason to doubt that the full &euro;629,975.04 reflects
genuine market value Naissance obtained.</li>
</ul>

<p>I would like this pleaded as the <b>equitable frame</b> of the
defence &mdash; both in the comparsa and in the parallel settlement
channel. I understand that art. 56 L.F. blocks a formal set-off and
that a formal counterclaim for the shortfall would invite art. 2741
c.c. <i>par condicio creditorum</i> objections, and I am therefore
<b>not</b> asking you to plead the shortfall as statutory
compensation. I am asking you to present it as the commercial
context within which the technical points below are heard, and to
use it as the decisive lever with the curator.</p>

<hr>

<h3>2. Technical defence points to include</h3>

<p>Within the equitable frame above, the defence should also press
the following:</p>

<ul>
<li><b>The &euro;3,932 &quot;legal expenses not admitted to the
bankruptcy liabilities&quot;</b> (one of the components the trustee
includes inside his &euro;629,975.04 figure). By the trustee's own
characterisation this sum sits outside the formal concorso and
therefore cannot be the subject of <i>ex lege</i> restitution under
art. 110 L.F. / art. 2033 c.c.</li>
<li><b>The &euro;4,761.47 prededuzione</b> excluded by the G.D. at
2019 admission &mdash; to be preserved as an equitable exception
against any amount ordered to be returned.</li>
<li><b>Factual distinguishing of Cass. 23482/2018 and Cass.
12673/2022.</b> I do not want finality pleaded in the abstract. I
want the two Supreme Court decisions read in full and distinguished
on their facts (in particular: was the curator notified of the
04.04.2019 distribution hearing, and did he fail to intervene in
time?). I would be grateful for your honest view before the
pleading is settled.</li>
<li><b>Errore materiale in the 2018 Istanza</b> &mdash; clause 3
recites &euro;1,118,438.29 while clause 4's parenthetical
calculation recites &euro;1,188,438.29 (only the latter
reconciles). I had no direct contact with Avv. Fiorilli at the
time &mdash; all instruction ran through Argo Ge.Re.Cre. Please
plead this as contextual support, not as a decree-reopening
attack (I accept the 2019 admission order is res judicata
endofallimentare).</li>
<li><b>Interest start date.</b> Interest should run from the
judicial demand (30.12.2025), not from the informal diffide
(01.07.2025).</li>
<li><b>Art. 210 c.p.c. document production</b> of the 04.04.2019
hearing minutes, the distribution plan as filed, and the decree
executing the state of liabilities (with its reasoning on the
&euro;4,761.47 exclusion).</li>
</ul>

<hr>

<h3>3. Settlement authority &mdash; to be used in parallel with the defence</h3>

<p>Please open a parallel settlement channel with Dott. Scarpellini
as soon as the costituzione is filed. Your authority:</p>
<ul>
<li><b>Opening</b>: &euro;20,000 &ndash; &euro;25,000 all-in
(capital, interest, all costs), saldo e stralcio.</li>
<li><b>Target landing</b>: &euro;30,000 &ndash; &euro;40,000.</li>
<li><b>Maximum authorised ceiling (walkaway)</b>: &euro;45,000.
Above this figure I would rather proceed to hearing.</li>
</ul>

<p>My pitch to the curator, which I would like you to convey, is
set out in &sect;1 above: Naissance is already ~&euro;80k short on
the bankruptcy's own admitted numbers; 100% recovery against that
background is not realistic; a figure within &euro;30&ndash;40k,
paid promptly, is the sensible resolution.</p>

<hr>

<h3>4. Handling of Avv. Fiorilli</h3>

<p>I confirm your recommendation not to join Avv. Fiorilli to this
proceeding. However, please <b>draft a PEC diffida to Avv.
Fiorilli this month</b>, in terms sufficient to interrupt the
limitation period on any future professional-negligence action.
Hold it; do not serve it before the outcome of this proceeding is
known. I want the draft ready.</p>

<hr>

<h3>5. What I need back from you, in writing, before you settle the pleading</h3>

<ol type="a">
<li>Confirmation of the procedural vehicle (<i>memoria difensiva</i>
vs <i>comparsa di costituzione e risposta</i> under the rito
semplificato) and the costituzione deadline of 04.05.2026.</li>
<li>Your view &mdash; having read the full text of Cass. 23482/2018
and Cass. 12673/2022 &mdash; on whether their facts are genuinely
distinguishable from this case.</li>
<li>Your drafting timetable.</li>
<li>Your confidential estimate of the probability of success on
(i) the &euro;3,932 attack and (ii) the factual distinguishing of
the Cassazione cases.</li>
<li>Your candid view of the curator's likely settlement posture
and of what figure he could realistically accept.</li>
</ol>

<p>I am available for a short call in the next few days.</p>

<p>Kind regards,</p>
<p>Grahame<br>
Grahame McGirr<br>
Director<br>
Naissance UK Limited<br>
07930 473 842</p>

</body></html>
"""


def build():
    out_path = OUT / "27_Draft_email_to_Belardi_v8_ENGLISH.pdf"
    HTML(string=HTML_BODY).write_pdf(out_path, stylesheets=[CSS(string=CSS_STYLE)])
    print(f"Saved: {out_path}")


if __name__ == "__main__":
    build()
