# Sito istituzionale · Fabio Scoccimarro

Sito statico (HTML, CSS e JavaScript senza dipendenze) per l'Assessore alla Difesa dell'Ambiente, Energia e Sviluppo sostenibile della Regione Autonoma FVG (Friuli Venezia Giulia).

## Identità visiva (Editorial Pop nei colori FdI)

- Carta puntinata `#F5F4EE`, superfici bianche, inchiostro blu profondo `#062E4F` per testi, bordi da 2 px e ombre piene sfalsate.
- Blu FdI `#084270` per testata delle pagine interne, invito all'azione e azioni secondarie; giallo FdI `#F8F06D` per l'azione principale (testo blu), evidenze e segni grafici.
- Verde `#3DAE6A` e rosso `#CE2B37` del tricolore solo come dettagli (barre dei numeri, stelle, filetto del piè di pagina).
- Caratteri: Archivo Black maiuscolo per nome, titoli e numeri; DM Sans per testo, moduli e controlli.
- Simbolo FdI: `assets/img/simbolo-fdi.svg`, dal PDF ufficiale, proporzioni originali, dentro un medaglione con bordo.
- Contrasti verificati: testo da 5,9:1 a 14,5:1.

## Pagine

| File | Sezione |
|---|---|
| `index.html` | Inizio: apertura con ritratto, contatori, priorità, citazione, ultime iniziative |
| `chi-sono.html` | Biografia, percorso istituzionale, pilastri dell'azione amministrativa |
| `progetti.html` | Cosa facciamo: Barcola, bonifiche, energia, mare e giovani, comunità locali |
| `notizie.html` | Sala stampa con filtri per categoria, ricerca e finestra di lettura con galleria |
| `contatti.html` | Modulo, riferimenti ufficiali, canali ufficiali, informativa e accessibilità |

## Cosa completare prima della messa in linea

1. **Fotografie** in `assets/img/`: inserite `ritratto.jpg` (alla scrivania, 678×452 px), `ritratto-primo-piano.jpg` (347×288 px) e `barcola.jpg` (365×273 px). Sono a bassa risoluzione: sostituirle con file da almeno 1600 px di lato lungo mantenendo lo stesso nome. Restano segnaposto `conferenza.svg` (serve una foto di conferenza stampa o di un tavolo regionale) e le illustrazioni delle altre notizie.
2. **`assets/js/configurazione.js`**: indirizzo della segreteria, pagine Facebook, Instagram, LinkedIn, YouTube. Finché un campo è vuoto in pagina compare *DA VERIFICARE* in rosso.
3. **Voci in rosso *DA VERIFICARE***: 40+ progetti comunali, 14 lotti di Barcola, anni di presidenza della Provincia, attribuzione della citazione, testi delle notizie senza fonte, titolare del trattamento dati.
4. **Notizie**: si aggiungono in `assets/js/notizie.js` (istruzioni in testa al file). Impostare `verificato: true` e `fonte` solo dopo il controllo.

## Dati già verificati

- Impegno 2026 oltre 300 milioni e voci della manovra estiva: [Italpress, 23 luglio 2026](https://www.italpress.com/?p=719803)
- Progetto "La nuova costa di Barcola" (studio Metroarea, due ambiti, circa 20 anni): [InTrieste, 16 novembre 2023](https://intrieste.com/?p=22207)
- PEC della Direzione centrale difesa dell'ambiente, energia e sviluppo sostenibile `ambiente@certregione.fvg.it` (atti regionali 2023); Sportello Ambiente ed Energia, via Carducci 6, Trieste, 040 3774130.

## Modulo contatti

Senza servizio esterno il modulo apre il programma di posta del cittadino con il messaggio già compilato. Per l'invio diretto impostare `indirizzoServizioModulo` (ad esempio Formspree o un modulo regionale).

## Anteprima locale

Aprire `index.html` nel browser, oppure:

```bash
cd sito-scoccimarro && python3 -m http.server 8000
```

## Pubblicazione protetta su costalonga.org/scocci

L'anteprima è pubblicata nel repository `GuidoCostalonga/GuidoCostalonga.github.io`, cartella `scocci/`. GitHub Pages non consente password lato server: ogni pagina viene quindi cifrata (AES-GCM a 256 bit, chiave ricavata dalla parola chiave con PBKDF2-SHA256, 600.000 iterazioni) e decifrata nel browser. La parola chiave non è scritta in nessun file. Fogli di stile e immagini restano in chiaro.

Per ripubblicare dopo una modifica:

```bash
PAROLA_CHIAVE='...' node strumenti/proteggi.mjs . ../../GuidoCostalonga.github.io/scocci
```

Poi registrare e caricare la cartella `scocci/` nel repository del sito.

## Varianti grafiche

Le tre versioni condividono pagine, testi, notizie e immagini; cambia solo il foglio di stile. In tutte le scritte sono nel blu di Fratelli d'Italia `#084270`.

| Variante | Anteprima | Stile | Foglio di stile |
|---|---|---|---|
| A | costalonga.org/scocci | istituzionale FdI; apertura con la foto in Vespa | `varianti/a/stile.css` |
| B | costalonga.org/scocci-b | Editorial Pop nei colori FdI; apertura con la foto in Vespa | `assets/css/stile.css` |
| C | costalonga.org/scocci-c | stile del sito di Manuel Pil8 (Cordenons 2027) con il blu FdI al posto del rosso; apertura con la foto in Vespa | `varianti/c/stile.css` |

Per preparare e pubblicare una variante (A o C):

```bash
strumenti/variante.sh c /tmp/scocci-c
PAROLA_CHIAVE='...' node strumenti/proteggi.mjs /tmp/scocci-c ../../GuidoCostalonga.github.io/scocci-c
```

## Notizie dal notiziario «La passione di sempre»

Le 43 notizie di maggio, estate e settembre 2026 sono in testa a `assets/js/notizie.js` (`NOTIZIE_NOTIZIARIO`), con il campo `periodo` al posto della data esatta e le foto in `assets/img/notizie/`. Le foto sono state estratte dai PDF e ingrandite fino a 1400 px di lato lungo (ricampionamento Lanczos con leggera maschera di contrasto). Non sono state riprese le parti del notiziario di polemica personale, il cruciverba e i testi di altri autori (lettera di Giorgia Meloni, intervento di Luca Ciriani).

Anche `barcola.jpg`, `ritratto.jpg` e `ritratto-primo-piano.jpg` sono stati ingranditi: per una resa davvero nitida servono comunque gli originali ad alta risoluzione.

## Notiziario da scaricare

I tre numeri di «La passione di sempre» (maggio, estate, settembre 2026) sono in `assets/notiziario/`, con le copertine in `assets/img/notiziario/`. La pagina `notiziario.html` («Notiziario» nel menu, tra Notizie e Contatti) raccoglie i numeri da scaricare; la pagina Notizie e il piè di pagina rimandano lì.

I PDF originali (17–26 MB) sono stati alleggeriti a 3,5–6 MB ricomprimendo soltanto le fotografie senza trasparenza (lato lungo massimo 1600 px, qualità JPEG 80): testi, grafica e immagini trasparenti restano identici. Attenzione: le pagine del sito sono cifrate, i PDF invece no. Chi conosce l'indirizzo esatto può scaricarli anche senza parola chiave.

Per aggiungere un nuovo numero: copiare il PDF in `assets/notiziario/`, creare la copertina con `pdftoppm -r 90 -f 1 -l 1 -jpeg -singlefile` e duplicare una scheda in `notiziario.html`.
