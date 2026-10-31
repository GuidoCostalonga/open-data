# Sito istituzionale · Fabio Scoccimarro

Sito statico (HTML, CSS e JavaScript senza dipendenze) per l'Assessore alla Difesa dell'Ambiente, Energia e Sviluppo sostenibile della Regione Autonoma FVG (Friuli Venezia Giulia).

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
