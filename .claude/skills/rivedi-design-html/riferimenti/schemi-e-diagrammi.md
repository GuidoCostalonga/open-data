# Schemi e diagrammi

## Quando un elemento visivo serve

Un diagramma si guadagna il posto se il lettore, guardandolo, capisce in cinque secondi qualcosa che a parole richiederebbe un paragrafo. Segnali nel testo che indicano un'occasione:

| Nel testo si trova | Si disegna |
|---|---|
| "prima... poi... infine", un iter, una procedura | Schema a passaggi numerati |
| "se... allora... altrimenti", requisiti, casi | Albero di decisione |
| Date, scadenze, fasi | Linea del tempo |
| "dipende da", "fa capo a", organi e competenze | Schema a blocchi o organigramma |
| Un totale diviso in parti | Barra unica suddivisa (preferibile alla torta) |
| Lo stesso valore per più soggetti | Barre orizzontali ordinate |
| Un valore che cambia negli anni | Linea, oppure barre se gli anni sono pochi |
| Un valore rispetto a un obiettivo o a una media | Barra con riferimento segnato |
| Due grandezze in relazione | Dispersione di punti |
| Passaggi di risorse da una voce all'altra | Diagramma di flusso con spessori proporzionali |
| Tre o quattro numeri chiave | Riquadri con cifra grande, unità, data e fonte |

Segnali che invece dicono di non disegnare: i dati sono due soli (basta una frase), il confronto non interessa a nessuno dei lettori, il grafico ripeterebbe un altro già presente.

## Scegliere la forma

* Confronti tra categorie: barre orizzontali, ordinate dal valore maggiore al minore, con il nome per esteso a sinistra e il valore scritto in fondo alla barra. Si leggono bene anche al telefono.
* Le barre partono sempre da zero. Un asse tagliato esagera le differenze e toglie credibilità.
* Torte e ciambelle solo con due o tre parti. Oltre, una barra suddivisa o barre separate.
* Niente effetti a tre dimensioni, niente doppio asse verticale.
* Un grafico, un messaggio. Il titolo del grafico dice il messaggio ("Gli over 65 sono un quarto dei residenti"), non la variabile ("Popolazione per classi di età").
* La serie o la voce che conta si evidenzia con il colore; le altre in grigio.

## Costruire in SVG

Struttura di base, da adattare:

```html
<figure class="grafico">
  <svg viewBox="0 0 640 320" role="img" aria-labelledby="g1-titolo g1-desc"
       style="width:100%;height:auto;max-width:640px">
    <title id="g1-titolo">Titolo che dice il messaggio</title>
    <desc id="g1-desc">Descrizione in una o due frasi di ciò che il grafico mostra,
      con i valori principali.</desc>
    <!-- contenuto -->
  </svg>
  <figcaption>Cosa si vede, unità di misura, anno. Fonte: ...</figcaption>
</figure>
```

Regole:

* `viewBox` sempre, larghezza al 100% e altezza automatica: il disegno si adatta al contenitore senza script.
* Coordinate calcolate dai dati della pagina con una scala esplicita, scritta in un commento accanto al grafico (per esempio: `<!-- scala: 1 unità = 4,2 px; massimo 120 -->`). Chi rilegge deve poter rifare il conto.
* Valori scritti sul grafico identici a quelli della pagina, stesso numero di decimali, stesso separatore. Mai arrotondare un dato per farlo stare meglio.
* Testi dentro l'SVG di almeno 12 px effettivi a 390 px di larghezza. Con `viewBox` largo 640 e contenitore largo 358, un testo da 14 unità diventa meno di 8 px: in quel caso serve una seconda versione più stretta e più alta per il telefono, mostrata con una regola `@media`, oppure etichette spostate fuori dall'SVG in HTML.
* Colori presi dalle variabili CSS della pagina (`fill="var(--colore)"` oppure `currentColor`). Se la pagina ha il tema scuro, il grafico deve seguirlo.
* Contrasto degli elementi grafici rispetto allo sfondo di almeno 3 a 1; dei testi almeno 4,5 a 1.
* L'informazione non sta mai nel solo colore: etichetta diretta accanto alla serie, oppure tratteggio o forma diversa. Le etichette dirette sono preferibili alla legenda.
* Coordinate con al massimo un decimale. I decimali superflui sono la prima causa di SVG pesanti.
* Icone e decorazioni: `aria-hidden="true"`.

## Tenere insieme grafico e tabella

Il grafico affianca i dati esatti, non li sostituisce. Soluzioni:

* grafico sopra e tabella sotto, entrambi visibili;
* tabella dentro un elemento `<details>` con un `<summary>` chiaro ("Vedi tutti i dati in tabella"), quando è lunga;
* al telefono, una tabella larga sta in un contenitore con `overflow-x:auto` e prima colonna fissa, mai rimpicciolita fino a diventare illeggibile.

## Schemi di processo

* Blocchi in HTML e CSS (griglia o flex) più che in SVG quando contengono testo: il testo va a capo da solo, si traduce, si legge con gli strumenti assistivi.
* Elenco ordinato (`<ol>`) come struttura di fondo: lo schema è un elenco anche per chi non lo vede.
* In orizzontale su schermi larghi, in verticale al telefono, con la stessa marcatura.
* Frecce e connettori sono decorazione (`aria-hidden="true"`): l'ordine lo dà l'elenco.
* Ogni passaggio: numero, verbo all'infinito o nome dell'azione, chi lo compie, eventuale termine.

## Dati mancanti o incerti

Se per completare un diagramma manca un valore, il diagramma si disegna con il vuoto ben visibile e la dicitura:

```html
<em style="color:#c00">DA VERIFICARE</em>
```

Mai interpolare, stimare o prendere un valore da memoria.
