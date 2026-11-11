# Animazioni e video

## A cosa serve il movimento

Il movimento attira lo sguardo più di ogni altra cosa sulla pagina: usato male distrae da tutto il resto. Si usa per quattro scopi soltanto.

| Scopo | Esempio | Durata |
|---|---|---|
| Rispondere a un gesto | Un pulsante che cambia stato, una scheda che si apre | da 120 a 200 ms |
| Mostrare un passaggio | Il contenuto di un filtro che cambia, un pannello che scorre | da 200 a 350 ms |
| Spiegare una sequenza | Un iter che si illumina un passo alla volta | Comandata dal lettore |
| Guidare lo sguardo una volta | Le barre di un grafico che crescono quando entra in vista | da 400 a 700 ms, una sola volta |

Non si anima: il testo principale all'ingresso, ciò che il lettore deve leggere subito, qualunque cosa in ciclo continuo senza comando di pausa.

## Regole tecniche

* Si animano solo `transform` e `opacity`. Animare larghezze, altezze, margini o posizioni costringe il navigatore a ricalcolare la pagina e la fa scattare, soprattutto sui telefoni lenti.
* Ogni pagina con animazioni contiene questa regola, senza eccezioni:

  ```css
  @media (prefers-reduced-motion: reduce) {
    *, *::before, *::after {
      animation-duration: 0.01ms !important;
      animation-iteration-count: 1 !important;
      transition-duration: 0.01ms !important;
      scroll-behavior: auto !important;
    }
  }
  ```

  Chi ha chiesto al proprio dispositivo meno movimento (per vertigini, emicrania, difficoltà di attenzione) deve vedere lo stato finale, completo e fermo.
* Lo stato finale è quello scritto nel codice. L'animazione parte da uno stato iniziale aggiunto con una classe da JavaScript. Così, se lo script non parte, il contenuto è già visibile. Schema:

  ```html
  <script>document.documentElement.classList.add('js');</script>
  ```
  ```css
  .js .rivela { opacity: 0; transform: translateY(12px); transition: opacity .5s, transform .5s; }
  .js .rivela.visibile { opacity: 1; transform: none; }
  ```
  ```js
  const oss = new IntersectionObserver((voci) => {
    for (const v of voci) if (v.isIntersecting) { v.target.classList.add('visibile'); oss.unobserve(v.target); }
  }, { threshold: 0.2 });
  document.querySelectorAll('.rivela').forEach((el) => oss.observe(el));
  ```
* Niente lampeggi oltre tre volte al secondo.
* Un'animazione che dura più di cinque secondi o si ripete deve avere un comando di pausa visibile.
* Per le barre di un grafico che crescono: `transform: scaleX()` con `transform-origin: left` (oppure `scaleY` dal basso), mai l'attributo `width`. Il valore numerico accanto alla barra resta fermo e leggibile dal primo istante.

## Sequenze animate che spiegano

Quando un procedimento ha più passaggi e manca un video, una sequenza comandata dal lettore funziona meglio di un filmato: ognuno va al proprio ritmo.

Struttura:

* un elenco ordinato con tutti i passaggi, sempre presente nel codice e leggibile per intero senza script;
* con JavaScript attivo, un passaggio in evidenza alla volta e tre comandi veri (`<button>`): Indietro, Avanti, Riproduci o Pausa;
* indicatore "Passaggio 2 di 5" in un elemento con `aria-live="polite"`;
* nessun avvio automatico: parte quando il lettore preme Riproduci, e si ferma all'ultimo passaggio;
* frecce della tastiera attive quando il fuoco è sui comandi;
* con movimento ridotto: nessuna transizione, il cambio di passaggio è immediato, i comandi restano.

## Video

I video sono l'unica eccezione alla regola "tutto nel file": restano file separati o collegamenti. Non si incorporano mai in base64.

### Dove mettere un video

Accanto al punto che spiega, mai in cima come ingresso obbligato. Sempre con un titolo che dice cosa si vedrà e quanto dura ("Come presentare la domanda, 2 minuti"). Sotto il video, la stessa informazione in testo: molti non possono o non vogliono ascoltare.

### File video forniti dall'utente

```html
<figure class="video">
  <video controls preload="none" playsinline poster="anteprima.jpg" width="1280" height="720"
         style="width:100%;height:auto">
    <source src="filmato.webm" type="video/webm">
    <source src="filmato.mp4" type="video/mp4">
    <track kind="captions" src="filmato.it.vtt" srclang="it" label="Italiano" default>
    <a href="filmato.mp4">Scarica il video</a>
  </video>
  <figcaption>Titolo del video, durata. <a href="#trascrizione-1">Leggi la trascrizione</a></figcaption>
</figure>
```

* `controls` sempre. Nessun avvio automatico con audio.
* `preload="none"` con `poster`: il video non pesa finché non viene avviato.
* `width` e `height` dichiarati, così la pagina non salta mentre carica.
* Sottotitoli in un file `.vtt`. Se l'utente non li ha forniti, lasciare l'elemento `<track>` commentato e segnalare nella consegna che mancano: non scriverli a intuito.
* Un video muto e decorativo in ciclo è ammesso solo se breve, con `muted playsinline`, con un comando di pausa e fermo quando è attivo il movimento ridotto.

### Video su piattaforme esterne

Non si inserisce direttamente la cornice della piattaforma: caricherebbe centinaia di kB e traccerebbe il lettore prima ancora che abbia deciso di guardare. Si mette un'anteprima che carica il video solo al tocco:

```html
<figure class="video">
  <button class="video-avvia" type="button" data-video="https://www.youtube-nocookie.com/embed/CODICE?autoplay=1"
          aria-label="Riproduci il video: Titolo del video (2 minuti)">
    <span aria-hidden="true">▶</span> Titolo del video, 2 minuti
  </button>
  <figcaption>Il video si apre da YouTube. <a href="https://www.youtube.com/watch?v=CODICE">Guardalo sul sito</a></figcaption>
</figure>
<script>
document.querySelectorAll('.video-avvia').forEach((b) => b.addEventListener('click', () => {
  const c = document.createElement('iframe');
  c.src = b.dataset.video;
  c.title = b.getAttribute('aria-label').replace('Riproduci il video: ', '');
  c.allow = 'autoplay; encrypted-media; picture-in-picture';
  c.allowFullscreen = true;
  c.style.cssText = 'width:100%;aspect-ratio:16/9;border:0';
  b.replaceWith(c);
  c.focus();
}));
</script>
```

L'anteprima è disegnata in CSS (un riquadro in proporzione 16:9 con il titolo e il simbolo di avvio): non si scarica la miniatura dalla piattaforma. Il collegamento diretto nella didascalia garantisce l'accesso anche senza JavaScript.

### Quando il video manca

Due possibilità, da concordare con l'utente nel rapporto:

1. **Sequenza animata** al posto del video, costruita come descritto sopra.
2. **Segnaposto con copione**: un riquadro visibile solo nel codice (commento HTML) oppure, se l'utente lo chiede, un riquadro tratteggiato in pagina con la scritta "Video in preparazione". Nella consegna si allega il copione:

   | Voce | Contenuto |
   |---|---|
   | Scopo | Cosa deve aver capito chi lo guarda |
   | Durata | Di norma tra 60 e 120 secondi |
   | Apertura | La domanda del lettore a cui il video risponde |
   | Scene | Per ciascuna: cosa si vede, cosa si dice, durata |
   | Chiusura | Cosa fare adesso, dove trovare il dettaglio |
   | Sottotitoli | Testo integrale del parlato |

   Il copione usa solo fatti e numeri già presenti nella pagina.
