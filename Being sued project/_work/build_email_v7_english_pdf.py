#!/usr/bin/env python3
"""Build 25_Draft_email_to_Belardi_v7_ENGLISH.pdf - English draft of
the Belardi instruction email, aligned with v7 of the report.
For Grahame's review only; Italian version follows on approval."""

from pathlib import Path
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
        content: "Draft email to Belardi - v7 English - for review only";
        font-family: Calibri, sans-serif;
        font-size: 9pt;
        color: #666;
    }
}
body { font-family: Calibri, Arial, sans-serif; font-size: 11pt; line-height: 1.45; color: #202020; }
h1 { color: #1a365d; font-size: 17pt; border-bottom: 2px solid #1a365d; padding-bottom: 6px; }
h3 { color: #2c5282; font-size: 11.5pt; margin-top: 0.9em; }
.header-note { background-color: #fff8e1; border-left: 4px solid #f0a500;
  padding: 10px 14px; margin: 1em 0 1.5em 0; font-size: 10pt; }
.metadata { font-size: 10pt; color: #555; margin-bottom: 1.5em;
  border-bottom: 1px solid #ccc; padding-bottom: 0.8em; }
strong, b { color: #1a365d; }
ul { margin: 0.4em 0 0.8em 1.2em; }
li { margin-bottom: 0.25em; }
hr { border: none; border-top: 1px solid #ccc; margin: 1em 0; }
"""

HTML_BODY = """<!DOCTYPE html><html><head><meta charset="utf-8"><title>Draft email to Belardi v7 English</title></head><body>

<h1>Draft email to Avv. Primo Belardi &mdash; English</h1>

<div class="header-note">
<b>Note:</b> This is the English draft of the proposed email to Avv.
Belardi, for Grahame's review. The Italian version will be produced
once the content is approved. Do not send this English version to
Belardi &mdash; it is a working document only.
</div>

<div class="metadata">
<b>From:</b> Grahame McGirr &lt;gmcgirr@naissance.co.uk&gt;<br>
<b>To:</b> Primo Belardi &lt;avv.primobelardi@gmail.com&gt;<br>
<b>Subject:</b> Naissance UK Ltd / Curatela Fallimento Agricola Gavioli &mdash; defence instructions and settlement authority
</div>

<p>Dear Avv. Belardi,</p>

<p>Thank you for your email of 17 April and for your analysis of the
trustee's Ricorso. I confirm in general terms my agreement with your
proposed direction &mdash; the <i>errore materiale</i> argument on the
2018 Istanza, the subordinate reservation of Avv. Fiorilli's
professional-indemnity position, and opening a settlement dialogue in
parallel with the costituzione.</p>

<p>Before you draft the pleading I would like to record some points
that I think are important to incorporate, based on a complete
re-reading of the documents you forwarded on 30 March and the
additional material I forwarded on 18 April.</p>

<hr>

<h3>1. The 2018 Istanza is genuinely internally inconsistent &mdash; and I was not involved in its drafting</h3>

<p>Clause 3 of the Istanza recites a credit of <b>&euro;1,118,438.29</b>
while clause 4's parenthetical calculation writes out
<b>&euro;572,438.29 (1,188,438.29 less the assignment sum of
&euro;616,000)</b>. The arithmetic only reconciles to €1,188,438.29,
and all the documents attached to the Istanza (the 28.07.2017 credit
assignment contracts) consistently show €1,188,438.29. Clause 3 is
therefore almost certainly a typographical error.</p>

<p>I would add this: I had <b>no direct contact with Avv. Fiorilli</b>
at the time of the 2018 Istanza. Communication passed through Argo
Ge.Re.Cre.; Fiorilli dealt on my behalf. I was not asked to approve
and did not approve the €577,199.76 admission figure. In my view the
<i>errore materiale</i> argument has both an arithmetic hook (the
clause 3 vs clause 4 inconsistency) and a procedural hook (the lack
of client instruction behind the reduced figure).</p>

<p>I understand that the 2019 admission decree for €572,438.29 is
<i>res judicata endofallimentare</i> and cannot be reopened on
errore-materiale grounds alone. I am therefore not expecting this
point to defeat the claim on its own. I am asking that it be pleaded
as contextual support to the defence and the settlement conversation.</p>

<hr>

<h3>2. Live quantum challenges in the trustee's &euro;629,975.04</h3>

<p>The trustee's figure of €629,975.04 is built as €616,000 property
assignment + €13,975.04 (= €10,043.04 "higher amount distributed, net
of procedural expenses advanced" + €3,932.00 "legal expenses not
admitted to the bankruptcy liabilities"). I would like to contest two
specific line items within that figure:</p>

<ul>
<li><b>&euro;3,932.00 "legal expenses not admitted to the bankruptcy
liabilities"</b>. By the trustee's own characterisation this sum sits
outside the formal concorso. If so, it cannot be the subject of <i>ex
lege</i> restitution under art. 110 L.F. / art. 2033 c.c. I understand
the trustee's likely counter (receipt without concorsual title is
itself indebito under art. 111-bis L.F.; Cass. 17590/2019), but the
point is arguable both ways and I would be grateful for your view.</li>
<li><b>&euro;4,761.47 of prededuzione</b> (legal fees in RGE 187/2015)
excluded by the G.D. at 2019 admission. Without reopening that
ruling, I would like to reserve Naissance's right to have these
expenses treated as a legitimately borne cost, by way of equitable
exception to any amount of restitution.</li>
</ul>

<p>I recognise these two items are of modest monetary effect. I am
not asking you to present them as decisive; I am asking that they be
preserved and argued.</p>

<hr>

<h3>3. The foreclosure distribution plan of 04.04.2019</h3>

<p>The 04.04.2019 progetto di distribuzione was approved by the
Enforcement Judge at a hearing, without opposition from the curator
or any creditor, and was not impugned within the statutory window
under art. 512 c.p.c. I understand that Cass. 23482/2018 and
Cass. 12673/2022 hold that such distributions to the fondiario
creditor are provisional pending final bankruptcy ranking, and that
the finality of the distribution plan does not on its own defeat the
trustee's restitution claim. I am <b>not</b> asking you to plead
finality in the abstract.</p>

<p>What I am asking is that you pull the full text of both Cassazione
cases and consider whether their facts can be distinguished from
Naissance's case. In particular: in those cases, was the curator on
notice of the distribution and did he intervene in time? Here, was
the curator notified of the 04.04.2019 hearing, and did the curator
attend? If the curator had the opportunity to intervene and did not,
that is a distinguishing fact. I would be grateful for your honest
view, before the pleading is settled, on whether genuine factual
distinguishing is available.</p>

<p>I would also ask you to consider requesting document production
under art. 210 c.p.c. of the 04.04.2019 hearing minutes, the
distribution plan as filed, and the decree executing the state of
liabilities (including the specific reasoning on the
€4,761.47 prededuzione exclusion).</p>

<hr>

<h3>4. Interest start date</h3>

<p>The trustee claims legal interest from 01.07.2025 (following his
informal <i>diffide</i>). Under Italian law, interest on a restitution
of this type should in my understanding run from the judicial demand
(30.12.2025 Ricorso), not from the informal letter. This is a small
but legitimate point and I would like it challenged.</p>

<hr>

<h3>5. Documentary position and market value (factual support)</h3>

<p>On the evidence I have forwarded:</p>
<ul>
<li>Naissance acquired the credit in July 2017 via a double assignment
(Banca CRAS &rarr; Argo Ge.Re.Cre. &rarr; Naissance) for a face value
of <b>&euro;1,188,438.29</b>.</li>
<li>Naissance paid approximately <b>&euro;132,000</b> in documented
recovery costs: FX wires of &euro;57,000 (26.04.2018) and &euro;20,000
(01.05.2018) to Argo Ge.Re.Cre., plus two cost cheques of &euro;30,000
(executed as FX wire 05.06.2018 &mdash; same payment) and &euro;45,000.</li>
<li>Contemporaneous pre-auction expressions of interest on the
Chianciano Terme property, forwarded via Gordana Lupi from Marco
Gavioli: <b>&euro;550,000</b> (06.09.2017) and <b>&euro;620,000</b>
(12.09.2017). Auction clearing price: &euro;616,000.</li>
</ul>

<p>I would ask that the defence plead, as part of the equitable
frame, the following commercial reality: Naissance acquired a credit
at face value of &euro;1,188,438.29, the best genuine pre-auction
market view of the underlying asset was &euro;620,000, and Naissance
paid &euro;132,000 out-of-pocket to run the recovery. On that basis
Naissance's net recovery is of the order of &euro;488,000 &mdash;
leaving Naissance approximately <b>&euro;700,000 short</b> on the
underlying credit. I understand this point does not formally offset
the claim under art. 56 L.F. and that a formal counterclaim for the
shortfall would invite a <i>par condicio creditorum</i> objection
under art. 2741 c.c. I am therefore not asking you to plead it as a
formal counterclaim. I am asking you to plead it as the equitable
frame within which the technical points above are heard, and to use
it in the settlement conversation.</p>

<p>I would add that the trustee's own "received" figure of
&euro;629,975.04 itself exceeds every pre-auction market indication,
which suggests that the &euro;13,975.04 of non-market-value
components is itself something the defence can point to.</p>

<hr>

<h3>6. Handling of Avv. Fiorilli</h3>

<p>I confirm your recommendation not to join Avv. Fiorilli to this
proceeding. However, given the limitation considerations, I would
ask you to <b>draft a PEC <i>diffida</i> to Avv. Fiorilli this
month</b>, interruptive of prescription on any future
professional-negligence action. I do not want it served before the
outcome of this proceeding is clearer, but I want it drafted and
ready.</p>

<hr>

<h3>7. Settlement authority</h3>

<p>I confirm your proposal to open a parallel settlement channel with
the Curatore. For the avoidance of doubt, I authorise you from now on
to negotiate within the following parameters:</p>
<ul>
<li><b>Opening</b>: &euro;20,000 &ndash; &euro;25,000 all-in (capital,
interest, legal costs), saldo e stralcio;</li>
<li><b>Target landing</b>: &euro;30,000 &ndash; &euro;40,000;</li>
<li><b>Maximum authorised ceiling (walkaway)</b>: &euro;45,000.
Above this number I would prefer to proceed to hearing.</li>
</ul>

<p>I am aware that if the case goes to hearing and is lost, my total
exposure on capital + interest + curator's costs + contributo unificato
+ our own costs is in the range &euro;70,000 &ndash; &euro;85,000. The
&euro;45,000 ceiling is set on that basis.</p>

<hr>

<h3>8. Operational questions for you</h3>

<p>Before the pleading is drafted, I would be very grateful for:</p>
<ol type="a">
<li>Your confirmation of the procedural vehicle (<i>memoria difensiva</i>
vs <i>comparsa di costituzione e risposta</i> under the rito
semplificato) and of the 04.05.2026 costituzione deadline /
14.05.2026 hearing.</li>
<li>Your view &mdash; after reading the full text of Cass.
23482/2018 and Cass. 12673/2022 &mdash; on whether their facts can
be genuinely distinguished in Naissance's favour.</li>
<li>Your drafting timetable in view of the 4 May deadline.</li>
<li>Your confidential estimate of the probability of success on each
of the points above, in particular on the €3,932 challenge and on
the factual distinguishing of the two Cassazione cases.</li>
<li>Your view on the &euro;30&ndash;40k settlement target &mdash;
is it realistic against this curator, and if not, what range would
you expect?</li>
</ol>

<p>I am available for a short telephone or video call in the next
few days if that would help.</p>

<p>Thank you again for your work on this. I look forward to your
response and to seeing a draft of the memoria in good time before the
deadline.</p>

<p>Kind regards,</p>
<p>Grahame<br>
Grahame McGirr<br>
Director<br>
Naissance UK Limited<br>
07930 473 842</p>

</body></html>
"""


def build():
    out_path = OUT / "25_Draft_email_to_Belardi_v7_ENGLISH.pdf"
    HTML(string=HTML_BODY).write_pdf(out_path, stylesheets=[CSS(string=CSS_STYLE)])
    print(f"Saved: {out_path}")


if __name__ == "__main__":
    build()
