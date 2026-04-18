#!/usr/bin/env python3
"""Build an Outlook-compatible .eml draft email file to Avv. Belardi."""

import os
from email.message import EmailMessage
from email.utils import formatdate
from pathlib import Path

OUT = Path("/home/user/pdf-text/Being sued project/_output")

BODY_PLAIN = """Egregio Avv. Belardi,

La ringrazio per la Sua email del 16 aprile u.s. e per la Sua disponibilita'.

Premesso che la Curatela del Fallimento Agricola Gavioli S.r.l. in liquidazione (n. 35/2018 R.G. Tribunale di Siena, Dott. Stefano Scarpellini quale Curatore) ha depositato ricorso ex artt. 281-decies e undecies c.p.c. chiedendo la condanna di Naissance (UK) Limited alla restituzione della somma di EUR 57.536,75 oltre interessi e spese, con udienza fissata per il 14 maggio 2026 e termine di costituzione al 4 maggio p.v.,

Dopo un'attenta e ulteriore riflessione sulla documentazione depositata dalla curatela, nonche' sull'impianto giurisprudenziale richiamato (Cass. 28.09.2018 n. 23482 e 20.04.2022 n. 12673), desidero fornirLe indicazioni chiare e operative circa la linea difensiva che intendo assumere.

-----

1. IMPOSTAZIONE GENERALE

Ritengo che l'approccio basato esclusivamente sull'argomento dell'"errore materiale" nell'istanza di ammissione al passivo sia insufficiente e rischi di esporci a rilievi di inammissibilita'. Il testo del paragrafo 4 dell'istanza del 18.12.2018 -- laddove reca "EUR 572.438,29 (1.188.438,29 sottratta la somma di assegnazione pari ad euro 616.000,00)" -- e' aritmeticamente coerente e, a mio avviso, difficilmente qualificabile come mero errore materiale.

Analogamente, la tesi della definitivita' del progetto di distribuzione del 4.4.2019, pur interessante sul piano sistematico, si scontra con il consolidato orientamento di legittimita' secondo cui la restituzione del maggior incassato in sede esecutiva al fallimento opera ex lege, indipendentemente dall'eventuale impugnazione del piano di riparto (art. 41 TUB, artt. 52 e 111 L.F., e giurisprudenza richiamata dalla stessa controparte).

Per tali ragioni, Le chiedo di strutturare la nostra difesa su basi piu' mirate ed economicamente realistiche, come segue.

-----

2. LINEE DIFENSIVE DA SVILUPPARE NELLA COSTITUZIONE

Le chiedo gentilmente di sviluppare la costituzione sui seguenti punti:

a) Conversione al rito ordinario ex art. 281-decies, co. 2 c.p.c., in considerazione della complessita' della causa e della pluralita' di profili giuridici da esaminare (art. 41 TUB, art. 52 L.F., art. 111 L.F., art. 2855 c.c., nonche' la specifica interpretazione dei precedenti di Cass. 23482/2018 e 12673/2022).

b) Contestazione del quantum rispetto ai seguenti importi inclusi dalla curatela nel totale di EUR 629.975,04:
   - EUR 3.932,00 qualificati dalla stessa curatela come "spese legali non ammesse al passivo" -- circostanza che, per definizione, le pone al di fuori del concorso formale e quindi della restituzione ex lege;
   - computo degli interessi: la curatela pretende interessi legali dal 1.7.2025 e, dal deposito del ricorso, il tasso commerciale ex art. 1284 co. 4 c.c., mentre quest'ultimo dovrebbe decorrere dalla sola proposizione della domanda giudiziale;
   - verifica aritmetica di tutte le somme distribuite con ricostruzione autonoma sulla base della documentazione prodotta.

c) Richiesta di esibizione documentale ex art. 210 c.p.c. dei seguenti atti:
   - verbale dell'udienza del 4.4.2019 con elenco presenti;
   - progetto di distribuzione come depositato dal professionista delegato;
   - stato delle ripartizioni a tutti i creditori nel Fallimento n. 35/2018;
   - decreto di esecutivita' dello stato passivo con specifica motivazione sull'esclusione della prededuzione di EUR 4.761,47;
   - eventuali osservazioni depositate dalla curatela nell'udienza del 4.4.2019.

d) Riserva espressa di azione risarcitoria nei confronti dell'Avv. Paolo Fiorilli per l'eventuale negligenza professionale connessa all'esclusione della prededuzione di EUR 4.761,47; tale azione sara' promossa autonomamente e non mediante chiamata in causa nel presente procedimento, al fine di non compromettere i termini di costituzione.

e) Astensione dai seguenti argomenti, che ritengo controproducenti:
   - attacco collaterale al decreto di esecutivita' dello stato passivo per la prededuzione (art. 98-99 L.F.; Cass. SS.UU. 4309/2010);
   - contestazione del rimborso di EUR 30.000 a titolo di spese di procedura anticipate, trattandosi di somma legittimamente distribuita dall'attivo ex artt. 2770 c.c. e 111 L.F.;
   - tesi della mera "provvisorieta'" del riparto come argomento autosufficiente, in quanto la giurisprudenza richiamata dalla controparte gia' assorbe tale argomento.

-----

3. DIALOGO TRANSATTIVO PARALLELO

Le chiedo espressamente di aprire, non appena depositata la costituzione, un canale transattivo con la curatela. Sono autorizzato a confermarLe sin d'ora i seguenti parametri:

- apertura a EUR 30.000 onnicomprensivi (capitale, interessi, spese legali), pagamento rapido, saldo e stralcio;
- atterraggio atteso nella forbice EUR 38.000 - EUR 45.000;
- tetto massimo (walkaway) EUR 52.000, ancora nettamente inferiore all'esposizione complessiva in caso di soccombenza totale (stimata in EUR 80.000 - EUR 95.000 tra capitale, interessi, contributo unificato, competenze della curatela e difesa di parte).

Ritengo che la curatela, alla luce dei tempi, dei costi di procedura e del rischio di una qualche riduzione del quantum, potrebbe avere interesse a una definizione rapida.

-----

4. ULTERIORI PASSI OPERATIVI

a) Le chiedo cortesemente di inoltrare, gia' in questi giorni, una diffida PEC all'Avv. Paolo Fiorilli per interrompere la prescrizione dell'eventuale azione di responsabilita' professionale, senza pregiudizio per la strategia principale.

b) Le sarei grato se potesse confermarmi per iscritto il cronoprogramma di preparazione della costituzione, tenuto conto del termine del 4 maggio p.v.

c) Raccolgo e Le trasmettero' separatamente, nei prossimi giorni, tutta la documentazione ulteriore di supporto (evidenze dei bonifici, eventuali comunicazioni di interesse all'acquisto, corrispondenza con l'Avv. Fiorilli nel 2018).

-----

5. CONSIDERAZIONI FINALI

Sono consapevole che la posizione giuridica della curatela e', sul piano formale, piu' solida di quanto inizialmente ritenuto. Per tale ragione, la priorita' e' (i) non perdere argomenti per decadenza processuale, (ii) contenere in modo significativo il quantum, e (iii) chiudere la vicenda, ove possibile, mediante accordo transattivo entro valori sostenibili.

La prego di farmi pervenire il Suo riscontro e la bozza di costituzione appena disponibile, unitamente a una Sua valutazione delle probabilita' di successo sui singoli profili.

La ringrazio sin d'ora per l'attenzione e la disponibilita' e resto a completa disposizione per ogni ulteriore confronto, anche telefonico.

Un caro saluto,

Grahame
Grahame McGirr
Director
Naissance UK Limited

07930 473 842


If you have received this message in error, please notify the sender and immediately delete this message and any attachment hereto and/or copy hereof, as such message contains confidential information intended solely for the individual or entity to whom it is addressed. The use or disclosure of such information to third parties is prohibited by law and may give rise to civil or criminal liability. This e-mail and any attached files are confidential and may be legally privileged or otherwise protected.
"""

BODY_HTML = """<html>
<head><meta charset="utf-8"></head>
<body style="font-family: Calibri, Arial, sans-serif; font-size: 11pt; color: #202020;">

<p>Egregio Avv. Belardi,</p>

<p>La ringrazio per la Sua email del 16 aprile u.s. e per la Sua disponibilit&agrave;.</p>

<p>Premesso che la Curatela del Fallimento Agricola Gavioli S.r.l. in liquidazione (n. 35/2018 R.G. Tribunale di Siena, Dott. Stefano Scarpellini quale Curatore) ha depositato ricorso ex artt. 281-decies e undecies c.p.c. chiedendo la condanna di Naissance (UK) Limited alla restituzione della somma di <b>&euro;. 57.536,75</b> oltre interessi e spese, con udienza fissata per il 14 maggio 2026 e termine di costituzione al 4 maggio p.v.,</p>

<p>Dopo un'attenta e ulteriore riflessione sulla documentazione depositata dalla curatela, nonch&eacute; sull'impianto giurisprudenziale richiamato (Cass. 28.09.2018 n. 23482 e 20.04.2022 n. 12673), desidero fornirLe indicazioni chiare e operative circa la linea difensiva che intendo assumere.</p>

<hr>

<p><b>1. Impostazione generale</b></p>

<p>Ritengo che l'approccio basato esclusivamente sull'argomento dell'&ldquo;errore materiale&rdquo; nell'istanza di ammissione al passivo sia insufficiente e rischi di esporci a rilievi di inammissibilit&agrave;. Il testo del &sect;4 dell'istanza del 18.12.2018 &mdash; laddove reca &laquo;&euro;.572.438,29 (1.188.438,29 sottratta la somma di assegnazione pari ad euro 616.000,00)&raquo; &mdash; &egrave; aritmeticamente coerente e, a mio avviso, difficilmente qualificabile come mero errore materiale.</p>

<p>Analogamente, la tesi della definitivit&agrave; del progetto di distribuzione del 4.4.2019, pur interessante sul piano sistematico, si scontra con il consolidato orientamento di legittimit&agrave; secondo cui la restituzione del maggior incassato in sede esecutiva al fallimento opera <i>ex lege</i>, indipendentemente dall'eventuale impugnazione del piano di riparto (art. 41 TUB, artt. 52 e 111 L.F., e giurisprudenza richiamata dalla stessa controparte).</p>

<p>Per tali ragioni, Le chiedo di strutturare la nostra difesa su basi pi&ugrave; mirate ed economicamente realistiche, come segue.</p>

<hr>

<p><b>2. Linee difensive da sviluppare nella costituzione</b></p>

<p>Le chiedo gentilmente di sviluppare la costituzione sui seguenti punti:</p>

<p>a) <b>Conversione al rito ordinario</b> ex art. 281-decies, co. 2 c.p.c., in considerazione della complessit&agrave; della causa e della pluralit&agrave; di profili giuridici da esaminare (art. 41 TUB, art. 52 L.F., art. 111 L.F., art. 2855 c.c., nonch&eacute; la specifica interpretazione dei precedenti di Cass. 23482/2018 e 12673/2022).</p>

<p>b) <b>Contestazione del quantum</b> rispetto ai seguenti importi inclusi dalla curatela nel totale di &euro;.629.975,04:</p>
<ul>
<li>&euro;.3.932,00 qualificati dalla stessa curatela come &ldquo;spese legali non ammesse al passivo&rdquo; &mdash; circostanza che, per definizione, le pone al di fuori del concorso formale e quindi della restituzione <i>ex lege</i>;</li>
<li>computo degli interessi: la curatela pretende interessi legali dal 1.7.2025 e, dal deposito del ricorso, il tasso commerciale ex art. 1284 co. 4 c.c., mentre quest'ultimo dovrebbe decorrere dalla sola proposizione della domanda giudiziale;</li>
<li>verifica aritmetica di tutte le somme distribuite con ricostruzione autonoma sulla base della documentazione prodotta.</li>
</ul>

<p>c) <b>Richiesta di esibizione documentale</b> ex art. 210 c.p.c. dei seguenti atti:</p>
<ul>
<li>verbale dell'udienza del 4.4.2019 con elenco presenti;</li>
<li>progetto di distribuzione come depositato dal professionista delegato;</li>
<li>stato delle ripartizioni a tutti i creditori nel Fallimento n. 35/2018;</li>
<li>decreto di esecutivit&agrave; dello stato passivo con specifica motivazione sull'esclusione della prededuzione di &euro;.4.761,47;</li>
<li>eventuali osservazioni depositate dalla curatela nell'udienza del 4.4.2019.</li>
</ul>

<p>d) <b>Riserva espressa di azione risarcitoria</b> nei confronti dell'Avv. Paolo Fiorilli per l'eventuale negligenza professionale connessa all'esclusione della prededuzione di &euro;.4.761,47; tale azione sar&agrave; promossa autonomamente e non mediante chiamata in causa nel presente procedimento, al fine di non compromettere i termini di costituzione.</p>

<p>e) <b>Astensione</b> dai seguenti argomenti, che ritengo controproducenti:</p>
<ul>
<li>attacco collaterale al decreto di esecutivit&agrave; dello stato passivo per la prededuzione (art. 98-99 L.F.; Cass. SS.UU. 4309/2010);</li>
<li>contestazione del rimborso di &euro;.30.000 a titolo di spese di procedura anticipate, trattandosi di somma legittimamente distribuita dall'attivo ex artt. 2770 c.c. e 111 L.F.;</li>
<li>tesi della mera &ldquo;provvisoriet&agrave;&rdquo; del riparto come argomento autosufficiente, in quanto la giurisprudenza richiamata dalla controparte gi&agrave; assorbe tale argomento.</li>
</ul>

<hr>

<p><b>3. Dialogo transattivo parallelo</b></p>

<p>Le chiedo espressamente di aprire, non appena depositata la costituzione, un canale transattivo con la curatela. Sono autorizzato a confermarLe sin d'ora i seguenti parametri:</p>
<ul>
<li>apertura a &euro;.30.000 onnicomprensivi (capitale, interessi, spese legali), pagamento rapido, saldo e stralcio;</li>
<li>atterraggio atteso nella forbice &euro;.38.000 &ndash; &euro;.45.000;</li>
<li>tetto massimo (walkaway) &euro;.52.000, ancora nettamente inferiore all'esposizione complessiva in caso di soccombenza totale (stimata in &euro;.80.000 &ndash; &euro;.95.000 tra capitale, interessi, contributo unificato, competenze della curatela e difesa di parte).</li>
</ul>

<p>Ritengo che la curatela, alla luce dei tempi, dei costi di procedura e del rischio di una qualche riduzione del quantum, potrebbe avere interesse a una definizione rapida.</p>

<hr>

<p><b>4. Ulteriori passi operativi</b></p>

<p>a) Le chiedo cortesemente di inoltrare, gi&agrave; in questi giorni, una diffida PEC all'Avv. Paolo Fiorilli per interrompere la prescrizione dell'eventuale azione di responsabilit&agrave; professionale, senza pregiudizio per la strategia principale.</p>

<p>b) Le sarei grato se potesse confermarmi per iscritto il cronoprogramma di preparazione della costituzione, tenuto conto del termine del 4 maggio p.v.</p>

<p>c) Raccolgo e Le trasmetter&ograve; separatamente, nei prossimi giorni, tutta la documentazione ulteriore di supporto (evidenze dei bonifici, eventuali comunicazioni di interesse all'acquisto, corrispondenza con l'Avv. Fiorilli nel 2018).</p>

<hr>

<p><b>5. Considerazioni finali</b></p>

<p>Sono consapevole che la posizione giuridica della curatela &egrave;, sul piano formale, pi&ugrave; solida di quanto inizialmente ritenuto. Per tale ragione, la priorit&agrave; &egrave; (i) non perdere argomenti per decadenza processuale, (ii) contenere in modo significativo il quantum, e (iii) chiudere la vicenda, ove possibile, mediante accordo transattivo entro valori sostenibili.</p>

<p>La prego di farmi pervenire il Suo riscontro e la bozza di costituzione appena disponibile, unitamente a una Sua valutazione delle probabilit&agrave; di successo sui singoli profili.</p>

<p>La ringrazio sin d'ora per l'attenzione e la disponibilit&agrave; e resto a completa disposizione per ogni ulteriore confronto, anche telefonico.</p>

<p>Un caro saluto,</p>

<p>Grahame<br>
Grahame McGirr<br>
Director<br>
Naissance UK Limited</p>

<p>07930 473 842</p>

<hr>

<p style="font-size: 9pt; color: #808080;"><i>If you have received this message in error, please notify the sender and immediately delete this message and any attachment hereto and/or copy hereof, as such message contains confidential information intended solely for the individual or entity to whom it is addressed. The use or disclosure of such information to third parties is prohibited by law and may give rise to civil or criminal liability. This e-mail and any attached files are confidential and may be legally privileged or otherwise protected.</i></p>

</body>
</html>
"""


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    msg = EmailMessage()
    msg['From'] = "Grahame McGirr <gmcgirr@naissance.co.uk>"
    msg['To'] = "Primo Belardi <avv.primobelardi@gmail.com>"
    msg['Subject'] = "Re: Procedimento Curatela Fallimento Agricola Gavioli — Istruzioni difensive e linea strategica"
    msg['Date'] = formatdate(localtime=True)
    msg['X-Unsent'] = "1"  # Outlook flag: draft / unsent
    msg.set_content(BODY_PLAIN)
    msg.add_alternative(BODY_HTML, subtype='html')

    out_path = OUT / "07_Draft_email_to_Belardi.eml"
    with open(out_path, 'wb') as f:
        f.write(bytes(msg))
    print(f"Saved: {out_path}")


if __name__ == '__main__':
    main()
