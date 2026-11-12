---
name: rivedi-design-html
description: Rivede il design di una pagina HTML per renderla più facile da usare per chi la legge. Analizza la pagina con il navigatore (telefono e scrivania), presenta un rapporto con problemi e proposte, attende l'approvazione e poi applica le modifiche inserendo diagrammi, schemi, animazioni e video, con verifiche finali su accessibilità, integrità dei dati e peso. Da usare quando l'utente chiede di rivedere, migliorare, rendere più chiara o più usabile una pagina HTML o una dashboard, di aggiungere grafici, schemi, infografiche, animazioni o video a una pagina esistente, oppure dice "rivedi il design", "migliora questa pagina", "rendila più leggibile", "non si capisce, sistemala".
argument-hint: "[percorso della pagina HTML]"
---

# Rivedi il design di una pagina HTML

Lo scopo è uno solo: chi apre la pagina deve capire prima e fare meno fatica. Diagrammi, schemi, animazioni e video sono mezzi. Si aggiungono dove tolgono fatica al lettore, non dove abbelliscono soltanto.

La pagina da rivedere è quella indicata dall'utente (`$ARGUMENTS`). Se non è indicata, chiedere quale.

## Regole che valgono sempre

1. **Prima il rapporto, poi le modifiche.** Nessun file viene toccato prima che l'utente abbia approvato le proposte. Un ridisegno non richiesto, anche se migliore, costringe l'utente a ricontrollare tutto.
2. **I dati non si toccano.** Numeri, date, nomi, citazioni, fonti e testi normativi restano identici. Un diagramma mostra solo dati già presenti nella pagina o da essi ricavabili con un calcolo dichiarato. Se a un grafico manca un dato, non lo si stima: si lascia il vuoto e lo si segnala con la dicitura *DA VERIFICARE* in corsivo rosso. Queste pagine finiscono davanti a cittadini e giornalisti: un numero sbagliato costa più di un grafico mancante.
3. **Tutto dentro il file.** Diagrammi in SVG, animazioni in CSS, comportamento in JavaScript scritto nella pagina. Nessuna nuova libreria, nessun nuovo carattere da rete, nessuna immagine esterna. La pagina deve restare un unico file che funziona anche senza connessione. Le risorse esterne già presenti nell'originale si lasciano dove sono e si segnalano nel rapporto. Unica eccezione: i video, che restano file separati o collegamenti (vedi sotto).
4. **Quattro tipi di lettore, una sola pagina.** Ogni scelta va provata contro tutti e quattro:

   | Lettore | Cosa cerca | Cosa gli serve |
   |---|---|---|
   | Cittadino | Capire in fretta, spesso dal telefono | Risposta in cima, parole comuni, un'immagine che spiega |
   | Amministratore o politico | Il dato chiave e il confronto | Numeri in evidenza, confronti a colpo d'occhio |
   | Giornalista | Numeri citabili e fonti | Valori esatti leggibili, fonte e data accanto al dato |
   | Tecnico o ufficio | Il dettaglio completo | Tabelle integrali, possibilità di copiare e scaricare |

   La soluzione che regge per tutti è quasi sempre a strati: sintesi visiva in alto, dettaglio completo più sotto o a richiesta. Un grafico non sostituisce mai la tabella da cui nasce: la affianca.
5. **Testi aggiunti.** Titoli, didascalie ed etichette nuove si scrivono nella lingua della pagina, con parole semplici e senza burocratese. In italiano: niente inglesismi, niente trattini usati come punteggiatura, "ed" e "ad" solo davanti alla stessa vocale, sigle sciolte tra parentesi alla prima occorrenza.

## Percorso di lavoro

### 1. Fotografare lo stato di partenza

```bash
node <cartella della skill>/scripts/ispeziona.js <pagina.html> <cartella di lavoro>/prima
```

Lo strumento serve la pagina da un piccolo servitore locale, la apre in formato telefono (390 px) e scrivania (1440 px), salva le fotografie e scrive `rapporto.json` con le misure: errori, peso, risorse esterne, scorrimento orizzontale, contrasto, caratteri piccoli, bersagli al tocco, nomi accessibili, struttura dei titoli, animazioni, video. Salva anche `testo.txt`, il testo reso dal navigatore, che servirà alla fine.

Usare come cartella di lavoro una cartella temporanea fuori dal progetto. Poi:

* leggere tutto il codice della pagina;
* guardare le quattro fotografie (`telefono-inizio.png`, `telefono.png`, `scrivania-inizio.png`, `scrivania.png`). Le misure dicono cosa è rotto; solo le immagini dicono se la pagina si capisce.

### 2. Analizzare

Rispondere per iscritto, prima di ogni proposta, a tre domande:

* A cosa serve questa pagina, in una frase?
* Qual è la prima cosa che ciascuno dei quattro lettori vuole trovare?
* La trova nella prima schermata del telefono?

Poi passare la pagina su questa griglia:

| Aspetto | Domande |
|---|---|
| Gerarchia | Si capisce cosa è più importante? Il messaggio principale è in cima o sepolto? I titoli raccontano il contenuto o lo etichettano soltanto? |
| Orientamento | Su pagine lunghe c'è un indice o un modo per saltare alle sezioni? Si sa sempre dove ci si trova? |
| Leggibilità | Righe troppo lunghe, corpo piccolo, contrasto basso, blocchi di testo senza respiro? |
| Telefono | Qualcosa esce dallo schermo? Le tabelle si leggono? I comandi si toccano senza sbagliare? |
| Numeri | I valori chiave sono in evidenza con unità, data e fonte? Ci sono tabelle che nascondono un confronto o un andamento? |
| Testo che andrebbe disegnato | Procedure, flussi, strutture, scadenze, rapporti tra parti descritti a parole |
| Interazione | Filtri, schede e comandi sono evidenti? Rispondono in modo visibile? Funzionano da tastiera? |
| Accessibilità | Misure di `rapporto.json`, più uso da tastiera e senso della lettura senza immagini |
| Peso | Risorse esterne, tempi di caricamento, dimensione complessiva |

Per decidere dove un elemento visivo serve davvero e quale scegliere, leggere `riferimenti/schemi-e-diagrammi.md`. Per animazioni e video, `riferimenti/animazioni-e-video.md`.

### 3. Presentare il rapporto e fermarsi

Il rapporto va scritto per essere deciso in pochi minuti:

1. **La pagina in una frase** e i lettori a cui si rivolge.
2. **Cosa non funziona**, in ordine di gravità, ogni voce con la prova (misura o punto della fotografia) e l'effetto sul lettore. Niente elenchi di difetti generici.
3. **Due livelli di intervento**, entrambi descritti in concreto:
   * *Ritocco conservativo*: colori, caratteri e impianto restano quelli; si correggono usabilità e leggibilità e si aggiungono gli elementi visivi.
   * *Ridisegno*: si ripensano impaginazione, gerarchia e stile dove serve, senza toccare contenuti e dati.

   Dire quale dei due si consiglia e perché.
4. **Elementi visivi proposti**, in tabella: cosa (diagramma, schema, animazione, video), dove, quali dati o quale testo traduce, quale lettore ne beneficia.
5. **Video**: quali punti della pagina ne trarrebbero vantaggio.
6. **Cosa non verrà toccato.**

Chiudere con le domande, tutte insieme (con lo strumento per le domande all'utente, se disponibile):

* Quale livello: ritocco conservativo o ridisegno?
* Sovrascrivere il file originale o creare una copia accanto (`nome.rivista.html`)?
* Ci sono video da incorporare? Servono file o collegamenti. Dove mancano si può scegliere tra una sequenza animata e un segnaposto con il copione del video da girare.
* Quali degli elementi visivi proposti approvare, se non tutti.

**Fermarsi qui e attendere la risposta.**

### 4. Applicare le modifiche approvate

* Se l'utente ha scelto la copia, lavorare sulla copia. Se ha scelto di sovrascrivere, tenere comunque una copia dell'originale nella cartella di lavoro: serve per i confronti finali.
* Fare solo ciò che è stato approvato. Un'idea venuta in corso d'opera si propone, non si applica.
* Riusare ciò che la pagina ha già: variabili CSS, classi, scala dei caratteri, colori. Un elemento nuovo deve sembrare nato con la pagina.
* Costruire ogni elemento secondo i due file in `riferimenti/`.
* Nel ridisegno si cambia la forma, mai la sostanza: stessi testi, stessi dati, stesse funzioni, stessi collegamenti.

### 5. Verificare

Le quattro verifiche sono tutte obbligatorie. Se una fallisce si corregge e si ripete, finché passano.

**Prova nel navigatore**

```bash
node <cartella della skill>/scripts/ispeziona.js <pagina rivista> <cartella di lavoro>/dopo
```

Guardare le fotografie del dopo accanto a quelle del prima. Devono risultare: nessun errore in console, nessuna richiesta fallita, nessuno scorrimento orizzontale, nessun elemento sovrapposto o tagliato, ogni diagramma leggibile a 390 px.

**Accessibilità** (da `dopo/rapporto.json`)

* contrasto insufficiente: nessun caso tra gli elementi aggiunti o modificati, e totale non peggiore di prima;
* nessun interattivo senza nome, nessuna immagine senza `alt`, nessun SVG informativo senza descrizione;
* bersagli al tocco di almeno 24 px, meglio 44;
* con movimento ridotto: zero animazioni ancora attive e zero video in riproduzione;
* ogni comando aggiunto si raggiunge e si aziona da tastiera, con il fuoco visibile.

**Integrità dei dati**

```bash
python3 <cartella della skill>/scripts/confronta_dati.py <originale.html> <rivista.html>
python3 <cartella della skill>/scripts/confronta_dati.py <lavoro>/prima/testo.txt <lavoro>/dopo/testo.txt
```

Servono entrambe: la prima legge il codice, la seconda il testo reso dal navigatore, l'unica che vede i dati caricati da file esterni o calcolati con JavaScript. Nessun numero deve sparire o comparire meno volte. Ogni numero nuovo va giustificato uno per uno (valori sugli assi, passaggi numerati, un totale dichiarato come calcolato): se non si sa dire da dove viene, va tolto. I blocchi di testo segnalati come non ritrovati vanno ricontrollati a mano.

**Peso e velocità**

Confrontare prima e dopo: peso del file, peso totale, numero di richieste, tempo di caricamento, numero di nodi. Nessuna risorsa esterna nuova. Se il file cresce di oltre un terzo o di oltre 150 kB, dire perché nella consegna oppure alleggerire (di solito tracciati SVG troppo dettagliati o decimali inutili).

### 6. Consegnare

* Fotografie del prima e del dopo, telefono e scrivania.
* Elenco delle modifiche, raggruppate per effetto sul lettore.
* Esito delle quattro verifiche con i numeri, compreso ciò che non è stato possibile verificare.
* Per ogni segnaposto video, il copione pronto (vedi `riferimenti/animazioni-e-video.md`).
* Ciò che resta da fare e non rientrava nell'incarico.

## Senza navigatore

Se `ispeziona.js` non può girare (Playwright assente), dirlo all'utente e proseguire leggendo il codice. Le verifiche su contrasto, scorrimento orizzontale e resa al telefono non sono allora dimostrate: nella consegna vanno indicate come non verificate, mai come superate. `confronta_dati.py` richiede solo Python e va eseguito comunque sul codice.

## Errori da evitare

* Aggiungere un grafico perché "ci sta bene". Se non risponde a una domanda del lettore, è rumore.
* Sostituire una tabella con un grafico: il tecnico e il giornalista perdono i valori esatti.
* Animare il contenuto principale all'ingresso, così che il lettore debba aspettare per leggere.
* Rendere un contenuto visibile solo dopo uno scorrimento o solo con JavaScript attivo: se lo script fallisce, il contenuto deve esserci lo stesso.
* Affidare un'informazione al solo colore.
* Dichiarare superata una verifica non eseguita.
