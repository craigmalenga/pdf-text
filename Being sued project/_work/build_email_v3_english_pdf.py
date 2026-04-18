#!/usr/bin/env python3
"""Build 20_Draft_email_to_Belardi_v3_ENGLISH.pdf - English translation
of the Italian draft email for Grahame's review only."""

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
        content: "Draft email to Belardi (v3) - English - for review only";
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
h1 { color: #1a365d; font-size: 17pt; border-bottom: 2px solid #1a365d; padding-bottom: 6px; }
h2 { color: #2c5282; font-size: 13pt; margin-top: 1em; }
h3 { color: #2c5282; font-size: 11.5pt; margin-top: 0.8em; }
.header-note {
    background-color: #fff8e1;
    border-left: 4px solid #f0a500;
    padding: 10px 14px;
    margin: 1em 0 2em 0;
    font-size: 10pt;
}
.metadata {
    font-size: 10pt;
    color: #555;
    margin-bottom: 1.5em;
    border-bottom: 1px solid #ccc;
    padding-bottom: 0.8em;
}
strong, b { color: #1a365d; }
ul { margin: 0.4em 0 0.8em 1.2em; }
li { margin-bottom: 0.25em; }
hr { border: none; border-top: 1px solid #ccc; margin: 1em 0; }
"""


HTML_BODY = """<!DOCTYPE html>
<html><head><meta charset="utf-8"><title>Draft email to Belardi - v3 English</title></head><body>

<h1>Draft email to Avv. Primo Belardi &mdash; English translation</h1>

<div class="header-note">
<b>Note:</b> This is an English translation of the Italian draft email
(<code>19_Draft_email_to_Belardi_v3.eml</code>). It is for your review
only. The actual email to be sent to Avv. Belardi is the Italian
version.
</div>

<div class="metadata">
<b>From:</b> Grahame McGirr &lt;gmcgirr@naissance.co.uk&gt;<br>
<b>To:</b> Primo Belardi &lt;avv.primobelardi@gmail.com&gt;<br>
<b>Subject:</b> Re: Naissance UK Ltd / Curatela Fallimento Agricola Gavioli &mdash; Defence approach and integrations
</div>

<p>Dear Avv. Belardi,</p>

<p>Thank you for your email of 17 April and for your analysis of the
documentation filed by the curator.</p>

<p>I have read your proposed defensive strategy carefully and, in
general terms, <b>I confirm my agreement with its overall direction</b>,
in particular as regards:</p>
<ol>
<li>the <b>clerical error</b> (<i>errore materiale</i>) argument in the
14.12.2018 Istanza di Ammissione al Passivo prepared by Avv. Fiorilli;</li>
<li>the subordinate reservation to involve Avv. Paolo Fiorilli via his
professional-indemnity insurer;</li>
<li>opening a parallel settlement dialogue with the curator on different
and lower economic terms.</li>
</ol>

<p>I would however like, before you draft the pleading, to share some
reflections and additions that I think will strengthen our position, in
light of the complete documentation I forwarded on Saturday 18 April.</p>

<hr>

<h3>1. The 14.12.2018 Istanza is <b>actually internally inconsistent</b></h3>

<p>Re-reading the text of the Istanza di Ammissione al Passivo
carefully, one can see that:</p>
<ul>
<li>at <b>clause 3</b> of the premises, it refers to a credit of
<b>&euro;1,118,438.29</b>;</li>
<li>at <b>clause 4</b>, it states a residual amount of
<b>&euro;572,438.29</b> expressly calculated as
&laquo;(<i>1,188,438.29 minus the assignment sum of
&euro;616,000.00</i>)&raquo;.</li>
</ul>

<p>A quick arithmetic check confirms that only the second figure
(&euro;1,188,438.29) reconciles with the stated residual:
&euro;1,188,438.29 &minus; &euro;616,000 = &euro;572,438.29, whereas
&euro;1,118,438.29 &minus; &euro;616,000 would give &euro;502,438.29,
which is incompatible with the Istanza itself and with all the
attached documents (28.07.2017 credit assignment contracts).</p>

<p>Clause 3 of the Istanza therefore almost certainly contains a
clerical typo. This strengthens your proposed primary line: the
document is genuinely ambiguous, the attached contracts consistently
show &euro;1,188,438.29, and it would be inequitable to penalise
Naissance for a drafting slip.</p>

<hr>

<h3>2. Proposal to <b>integrate the defence</b> on three further points</h3>

<p>It remains true that the Delegated Judge admitted Naissance to the
liabilities for &euro;572,438.29, and the order admitting the state
of liabilities is now binding within the bankruptcy. I would therefore
ask you to consider integrating the defence on the following three
points, which can operate principally or cumulatively alongside the
clerical-error argument:</p>

<p><b>a) Finality of the 04.04.2019 distribution plan.</b></p>

<p>The distribution plan in the foreclosure proceeding RGE 187/2015 was
approved by the Enforcement Judge at a hearing on 04.04.2019,
<b>without opposition</b> from the curator or any other creditor, and
<b>was not challenged</b> within the statutory time limits. Referring
to Cass. 23482/2018 and 12673/2022 &mdash; of which I would ask you
kindly to read the full text, not just the massimario &mdash; the
curator now seeks an <i>ex post</i> re-allocation of the sums
distributed. I would be grateful if the defence could:</p>
<ul>
<li>produce the minutes of the 04.04.2019 hearing and the distribution
plan as filed;</li>
<li>verify the presence / notification of the curator at the 04.04.2019
hearing;</li>
<li>emphasise the curator's inaction in the enforcement proceeding;</li>
<li>distinguish the Supreme Court precedents on their facts (in those
cases the curator intervened in time).</li>
</ul>

<p><b>b) Targeted challenge to the quantum &euro;629,975.04 stated by
the curator.</b></p>

<p>I would like to highlight three items within the &euro;629,975.04
figure on which I ask the curator to be specifically held to account,
with a clearly differentiated order of priority:</p>

<ul>
<li><b>&euro;30,000 classified as a "refund" of procedural expense
advances (central point).</b> The banking documentation in my
possession shows that this figure corresponds to a &euro;30,000
payment from Naissance to Argo Ge.Re.Cre. made on 5 June 2018
(cheque executed as FX wire &mdash; the same payment). The subsequent
"refund" at the distribution is not, in economic terms, money
Naissance <i>received from the bankruptcy estate</i>, but rather the
return of an advance Naissance itself had previously paid.
<p>The decisive legal question is whether, for the purposes of
restitution under art. 110 L.F. / art. 2033 c.c., the calculation
should be made on the <b>gross flows that passed through the
procedure</b> or on the <b>net economic benefit</b> actually obtained
by the creditor. In my view the second reading is the correct and
equitable one, but I expressly ask you to give me your authoritative
view on the position of the Court of Cassation and the lower courts
on this point, <b>before</b> settling the pleading &mdash; this is
the point on which to press hardest. If accepted, it reduces the
claim from &euro;57,536.75 to &euro;27,536.75;</p></li>

<li><b>&euro;3,932.00 expressly classified by the curator as
"legal expenses not admitted to the bankruptcy liabilities"</b>
(secondary point): by definition outside the formal concorso and
therefore outside <i>ex lege</i> restitution. Moderate-strength
argument, easily documented on the face of the Ricorso;</li>

<li><b>&euro;4,761.47 in prededuzione</b> (legal fees from RGE 187/2015)
excluded by the Delegated Judge at admission (discretionary point).
Without reopening that ruling, I ask you to reserve &mdash; by way of
exception &mdash; Naissance's right to have those expenses recognised
as legitimately incurred, to be set off against any amount of
restitution. Weaker argument, to be pleaded as an equitable
exception.</li>
</ul>

<p><b>I am aware that these three points do not have equal
argumentative force</b> and it is not realistic to expect them all to
land cumulatively: the realistic target for a partial win is to bring
the quantum into the <b>&euro;25,000 &ndash; &euro;35,000 range</b>,
principally on the strength of the first point.</p>

<p><b>c) Calculation of interest.</b></p>

<p>The legal interest claimed by the curator from 01.07.2025 and
subsequently at the commercial rate under art. 1284, para. 4 c.c.
should, in my view, accrue only from the filing of the judicial
claim, not from a mere formal demand. This is a specific point we
can challenge.</p>

<hr>

<h3>3. Cost and market-value evidence, supporting the overall picture</h3>

<p>On Saturday 18 April I forwarded to you, in several separate emails,
the following additional documentation, which is useful to contextualise
Naissance's economic position and the fairness of the auction price:</p>

<ul>
<li><b>Documented financial flows</b> (totalling approximately
&euro;152,000, <b>net</b> of any double-counting between the &euro;30,000
cheque and its related FX execution wire, which represent the same
payment):
<ul>
<li>wire of &euro;57,000 on 26.04.2018 to Argo Ge.Re.Cre., corresponding
to the Gavioli cost items in the reconciliation schedule;</li>
<li>wire of &euro;20,000 on 01.05.2018 to Argo Ge.Re.Cre.;</li>
<li><b>cheque of &euro;30,000</b>, executed as FX wire on 05.06.2018
(same payment, not an additional sum);</li>
<li><b>cheque of &euro;45,000</b>;</li>
</ul></li>
<li><b>Analytical cost schedule</b> (Gavioli and Bettolle), totalling
approximately &euro;60,311;</li>
<li><b>Pre-auction expressions of interest</b> at &euro;550,000
(06.09.2017), &euro;620,000 (12.09.2017), and acceptance of a
pre-auction transaction at &euro;630,000. Read together with the final
auction clearing price of &euro;616,000, these data points confirm that
the market value of the property was in line with the auction price,
excluding any suggestion of a "hidden surplus" accruing to Naissance.</li>
</ul>

<hr>

<h3>4. Handling of the Fiorilli aspect</h3>

<p>I confirm your approach of <b>not joining</b> Avv. Fiorilli in
the present proceedings, so as not to compromise the costituzione
deadline. However, as a precaution I would ask you to:</p>
<ul>
<li>prepare in the coming days, in my name, a <b>PEC <i>diffida</i>
to Avv. Fiorilli</b> in terms sufficient to interrupt the limitation
period on any professional-liability action, to be held in suspense
and activated only after the outcome of this proceeding is known;</li>
<li>treat the Fiorilli dimension internally as a fallback, not as a
front-line argument.</li>
</ul>

<hr>

<h3>5. Parallel settlement</h3>

<p>I confirm your proposal to open a parallel settlement channel with
the Curatore, Dott. Scarpellini. For the purposes of the negotiation
mandate, I authorise you from now on to work within the following
parameters:</p>
<ul>
<li><b>opening</b>: &euro;15,000 &ndash; &euro;20,000 all-in (capital,
interest, legal costs), prompt payment, saldo e stralcio;</li>
<li><b>target landing</b>: &euro;25,000 &ndash; &euro;35,000;</li>
<li><b>maximum authorised ceiling (walkaway)</b>: &euro;45,000, still
well below the total exposure in the event of a full loss (estimated
at &euro;70,000 &ndash; &euro;85,000 including capital, interest,
contributo unificato, the curator's legal costs and our own defence
costs).</li>
</ul>

<p>Given the particular features of this case, the concrete defensive
arguments on quantum (especially the &euro;30,000 at &sect;2.b.) and
the costs the curator will incur in pursuing the matter, there is
realistic room for an agreement in the range indicated.</p>

<hr>

<h3>6. Operational requests</h3>

<p>I would be very grateful if you could confirm as soon as possible:</p>
<ol type="a">
<li>your <b>authoritative view</b> on the gross-versus-net question in
the context of restitution under art. 110 L.F. / art. 2033 c.c.
(decisive point for the &euro;30,000 argument at &sect;2.b.): how is
this treated by the lower courts and the Court of Cassation?;</li>
<li>your view on <b>distinguishing on the facts</b> the precedents
Cass. 23482/2018 and 12673/2022 (it is not enough to invoke the
finality of the distribution in the abstract; the distinctive features
of our case must be identified);</li>
<li>the drafting timetable for the pleading, in view of the 4 May
deadline;</li>
<li>your indicative and confidential estimate of the probability of
success on each defensive line, with particular reference to the
first point of &sect;2.b. (&euro;30,000 quantum) and to the binding
weight of the admission to the liabilities for
&euro;572,438.29;</li>
<li>your view on the opportunity to request document production under
art. 210 c.p.c. of the minutes of the 04.04.2019 hearing, the
distribution plan, and the order enforcing the state of liabilities
with specific reasoning on the exclusion of the prededuzione.</li>
</ol>

<p>If useful, I am fully available for a short telephone or video call
in the coming days.</p>

<p>Thank you again for your collaboration and for the clarity of your
analysis. I look forward to your response.</p>

<p>Kind regards,</p>
<p>Grahame<br>
Grahame McGirr<br>
Director<br>
Naissance UK Limited<br>
07930 473 842</p>

</body></html>
"""


def build():
    out_path = OUT / "20_Draft_email_to_Belardi_v3_ENGLISH.pdf"
    HTML(string=HTML_BODY).write_pdf(out_path, stylesheets=[CSS(string=CSS_STYLE)])
    print(f"Saved: {out_path}")


if __name__ == "__main__":
    build()
