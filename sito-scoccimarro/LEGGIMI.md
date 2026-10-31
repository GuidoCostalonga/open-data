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

1. **Fotografie** in `assets/img/`: le immagini attuali sono segnaposto in formato SVG. Sostituire con foto reali mantenendo il nome del file oppure aggiornando il percorso nelle pagine:
   - `ritratto.svg` → foto istituzionale a mezzo busto (verticale 4:5, almeno 800×1000 px)
   - `barcola.svg` → panoramica di Barcola e del Golfo (orizzontale 16:10, almeno 1600×1000 px)
   - `conferenza.svg` → conferenza stampa o tavolo regionale
   - `bonifiche.svg`, `energia.svg`, `mare-giovani.svg`, `comunita.svg`, `ia-mare.svg`, `sopralluogo.svg` → foto di contesto
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
