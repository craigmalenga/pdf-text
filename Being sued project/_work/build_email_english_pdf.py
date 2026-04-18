#!/usr/bin/env python3
"""Build English translation PDF of the draft email to Belardi."""

from pathlib import Path
from weasyprint import HTML, CSS

OUT = Path("/home/user/pdf-text/Being sued project/_output")

CSS_STYLE = """
@page {
    size: A4;
    margin: 2cm 2cm 2.5cm 2cm;
}
body {
    font-family: Calibri, Arial, sans-serif;
    font-size: 11pt;
    line-height: 1.5;
    color: #202020;
}
h1 { color: #1a365d; font-size: 16pt; border-bottom: 2px solid #1a365d; padding-bottom: 6px; }
h2 { color: #2c5282; font-size: 13pt; margin-top: 1.5em; }
hr { border: none; border-top: 1px solid #ccc; margin: 1.5em 0; }
ul { margin-left: 1em; }
.meta { color: #666; font-size: 10pt; margin-bottom: 2em; }
.note { background-color: #e6eef7; padding: 10px; border-left: 4px solid #2c5282; margin: 1em 0; font-style: italic; font-size: 10pt; }
"""

HTML_CONTENT = """<!DOCTYPE html>
<html><head><meta charset="utf-8"></head><body>

<h1>Draft Email to Avv. Primo Belardi — English Translation</h1>

<div class="note">This is an English translation for Grahame's reference only. The actual email to send is the Italian version in the .eml file (07_Draft_email_to_Belardi.eml).</div>

<div class="meta">
<b>From:</b> Grahame McGirr &lt;gmcgirr@naissance.co.uk&gt;<br>
<b>To:</b> Primo Belardi &lt;avv.primobelardi@gmail.com&gt;<br>
<b>Subject:</b> Re: Proceedings Curatela Fallimento Agricola Gavioli — Defence instructions and strategic direction
</div>

<hr>

<p>Dear Avv. Belardi,</p>

<p>Thank you for your email of 16 April and for your availability.</p>

<p>After careful and further reflection on the documentation filed by the trustee, as well as on the case law framework cited (Cass. 28.09.2018 n. 23482 and 20.04.2022 n. 12673), I wish to provide you with clear and operational guidance regarding the defence strategy I intend to adopt, also considering the imminent deadlines (costituzione due by 4 May and hearing set for 14 May 2026).</p>

<hr>

<h2>1. General Approach</h2>

<p>I believe that an approach based exclusively on the "clerical error" argument regarding the istanza di ammissione al passivo is insufficient and risks exposing us to objections of inadmissibility. The text of §4 of the 18.12.2018 istanza — where it states "€572,438.29 (1,188,438.29 less the assignment sum of €616,000.00)" — is arithmetically consistent and, in my view, difficult to characterise as a mere clerical error.</p>

<p>Similarly, the argument based on the finality of the 04.04.2019 distribution plan, while interesting from a systematic perspective, conflicts with the established line of authority holding that the restitution of excess sums obtained in enforcement to the bankruptcy operates <i>ex lege</i>, regardless of whether the distribution plan was challenged (art. 41 TUB, arts. 52 and 111 Bankruptcy Law, and the case law cited by the opposing party itself).</p>

<p>For these reasons, I ask you to structure our defence on more targeted and economically realistic grounds, as follows.</p>

<hr>

<h2>2. Defence Lines to Develop in the Costituzione</h2>

<p>I kindly ask you to develop the costituzione on the following points:</p>

<p><b>a) Request conversion to ordinary procedure</b> under art. 281-decies, paragraph 2 c.p.c., given the complexity of the case and the plurality of legal issues to examine (art. 41 TUB, art. 52 Bankruptcy Law, art. 111 Bankruptcy Law, art. 2855 Civil Code, as well as the specific interpretation of the precedents in Cass. 23482/2018 and 12673/2022).</p>

<p><b>b) Challenge the quantum</b> regarding the following amounts included by the trustee in the total of €629,975.04:</p>
<ul>
<li>€3,932.00 described by the trustee itself as "legal expenses not admitted to the liabilities" — a characterisation which, by definition, places them outside the <i>concorso formale</i> and therefore outside the <i>ex lege</i> restitution obligation;</li>
<li>Interest calculation: the trustee claims legal interest from 01.07.2025 and, from the filing of the ricorso, the commercial rate under art. 1284 paragraph 4 Civil Code, whereas the latter should run only from the formal commencement of legal proceedings;</li>
<li>Arithmetic verification of all distributed sums with our own independent reconstruction based on the documentation produced.</li>
</ul>

<p><b>c) Request for documentary production</b> under art. 210 c.p.c. of the following documents:</p>
<ul>
<li>Minutes of the 04.04.2019 hearing with attendance list;</li>
<li>Full distribution plan as filed by the delegated professional;</li>
<li>Statement of distributions to all creditors in Fallimento n. 35/2018;</li>
<li>Decree of enforceability of the state of liabilities with specific reasoning for the exclusion of the €4,761.47 <i>prededuzione</i>;</li>
<li>Any observations filed by the trustee at the 04.04.2019 hearing.</li>
</ul>

<p><b>d) Express reservation of damages claim</b> against Avv. Paolo Fiorilli for potential professional negligence connected to the exclusion of the €4,761.47 <i>prededuzione</i>; this action will be brought separately and not by way of third-party joinder in these proceedings, so as not to compromise the costituzione deadline.</p>

<p><b>e) Abstention</b> from the following arguments, which I consider counterproductive:</p>
<ul>
<li>Collateral attack on the decree of enforceability of the state of liabilities regarding the <i>prededuzione</i> (arts. 98-99 Bankruptcy Law; Cass. Supreme Sections 4309/2010);</li>
<li>Challenge to the refund of €30,000 for procedural expenses advanced, as this sum was legitimately distributed from the debtor's estate under arts. 2770 Civil Code and 111 Bankruptcy Law;</li>
<li>The thesis that the distribution plan was merely "provisional" as a self-standing argument, since the case law cited by the opposing party already absorbs this point.</li>
</ul>

<hr>

<h2>3. Parallel Settlement Dialogue</h2>

<p>I expressly ask you to open, as soon as the costituzione has been filed, a settlement channel with the trustee. I am authorised to confirm the following parameters:</p>
<ul>
<li>Opening offer: €30,000 all-inclusive (principal, interest, legal costs), prompt payment, full and final settlement;</li>
<li>Expected landing zone: €38,000 – €45,000;</li>
<li>Maximum ceiling (walkaway): €52,000, which remains significantly below our total exposure in the event of a full loss (estimated at €80,000 – €95,000 including principal, interest, court fees, trustee's legal costs and our own defence costs).</li>
</ul>

<p>I believe the trustee, in light of the timeframes, procedural costs and the risk of some quantum reduction, may have an interest in a prompt resolution.</p>

<hr>

<h2>4. Further Operational Steps</h2>

<p>a) I kindly ask you to send, already this week, a PEC formal demand to Avv. Paolo Fiorilli to interrupt the limitation period for any future professional negligence action, without prejudice to the main strategy.</p>

<p>b) I would be grateful if you could confirm in writing the drafting timetable for the costituzione, bearing in mind the 4 May deadline.</p>

<p>c) I am gathering and will send you separately, in the coming days, all additional supporting documentation (wire transfer evidence, any expressions of interest in the purchase, correspondence with Avv. Fiorilli in 2018).</p>

<hr>

<h2>5. Final Considerations</h2>

<p>I am aware that the trustee's legal position is, on a formal level, stronger than initially believed. For this reason, the priorities are (i) not to lose arguments through procedural forfeiture, (ii) to significantly reduce the quantum, and (iii) to close the matter, where possible, through a settlement within sustainable values.</p>

<p>I would ask you to provide me with your feedback and the draft costituzione as soon as available, together with your assessment of the probability of success on each individual point.</p>

<p>Thank you in advance for your attention and availability and I remain at your complete disposal for any further discussion, including by telephone.</p>

<p>Kind regards,</p>

<p><b>Grahame</b><br>
Grahame McGirr<br>
Director<br>
Naissance UK Limited</p>

<p>07930 473 842</p>

</body></html>
"""


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    out_path = OUT / "08_Draft_email_to_Belardi_ENGLISH.pdf"
    HTML(string=HTML_CONTENT).write_pdf(out_path, stylesheets=[CSS(string=CSS_STYLE)])
    print(f"Saved: {out_path}")


if __name__ == '__main__':
    main()
