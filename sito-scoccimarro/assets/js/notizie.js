/* ==========================================================
   ARCHIVIO NOTIZIE
   Per aggiungere un articolo: copiare un blocco { ... } in cima
   all'elenco e compilare i campi.
   - data: formato AAAA-MM-GG; se vuota compare "DA VERIFICARE".
   - categoria: "ambiente" | "energia" | "territorio" | "eventi"
   - verificato: true solo dopo il controllo su fonte ufficiale.
   - fonte: indirizzo della fonte (comunicato regionale, testata).
   ========================================================== */
window.NOTIZIE = [
  {
    id: "manovra-estiva-2026",
    titolo: "Manovra estiva: quasi 103 milioni per ambiente, energia e sviluppo sostenibile",
    categoria: "energia",
    data: "2026-07-23",
    verificato: true,
    fonte: "https://www.italpress.com/?p=719803",
    fonteNome: "Italpress, 23 luglio 2026",
    immagine: "assets/img/conferenza.svg",
    sintesi: "Con la manovra estiva l’impegno complessivo 2026 sulle deleghe ambientali ed energetiche supera i 300 milioni di euro: dalle sedi di ARPA FVG alle comunità energetiche, fino alla difesa del suolo.",
    testo: [
      "Il pacchetto destinato all’ambiente, all’energia e allo sviluppo sostenibile nella manovra estiva vale quasi 103 milioni di euro. Sommato agli stanziamenti già previsti, porta l’impegno finanziario complessivo del 2026 oltre quota 300 milioni.",
      "Le voci principali: 6 milioni per il piano delle sedi e le nuove strumentazioni di ARPA FVG (Agenzia regionale per la protezione dell’ambiente del Friuli Venezia Giulia); 7 milioni ad AUSIR (Autorità unica per i servizi idrici e i rifiuti) per le infrastrutture dei rifiuti e il servizio idrico integrato; 3,7 milioni per i centri di raccolta comunali, per un totale di legislatura di quasi 50 milioni.",
      "Sul fronte energetico arrivano 8 milioni per le comunità energetiche rinnovabili (3 milioni per Comuni e Università, 5 milioni per le imprese), 2 milioni per la sostituzione dei generatori di calore, 5 milioni per lo sconto carburanti fino a fine 2026 e 500 mila euro per il rifacimento delle cabine elettriche delle imprese.",
      "Previsti inoltre 7 milioni per l’efficientamento ecologico degli impianti sportivi, 4 milioni alla cabina di regia per la difesa del suolo (circa 39 milioni l’impegno totale sul rischio idrogeologico), 775 mila euro per la bonifica dell’ex inceneritore di Gorizia e 500 mila euro per i polmoni verdi urbani."
    ],
    galleria: [
      { src: "assets/img/conferenza.svg", didascalia: "Presentazione della manovra" },
      { src: "assets/img/energia.svg", didascalia: "Comunità energetiche rinnovabili" },
      { src: "assets/img/sopralluogo.svg", didascalia: "Difesa del suolo" }
    ]
  },
  {
    id: "ia-mare-barcolana",
    titolo: "Intelligenza artificiale e tutela del mare: la Regione alla Barcolana con gli studenti del Nautico",
    categoria: "eventi",
    data: "",
    verificato: false,
    fonte: "",
    immagine: "assets/img/ia-mare.svg",
    sintesi: "Tecnologia al servizio dell’ecosistema marino: un’iniziativa educativa nel cuore della Barcolana che unisce giovani, innovazione e amore per il Golfo.",
    testo: [
      "La Barcolana non è soltanto la regata più partecipata: è l’occasione per parlare di mare a chi il mare lo vivrà domani. Con gli studenti dell’Istituto Nautico di Trieste la Regione ha presentato strumenti di intelligenza artificiale applicati al monitoraggio e alla salvaguardia dell’ambiente marino.",
      "L’obiettivo è avvicinare i ragazzi alle professioni del futuro, mostrando come la tecnologia possa aiutare a leggere lo stato di salute delle acque e a prevenire i rischi per l’ecosistema del Golfo.",
      "Testo di presentazione da completare con i dati ufficiali dell’iniziativa (data, partner, strumenti impiegati)."
    ],
    galleria: [
      { src: "assets/img/mare-giovani.svg", didascalia: "Studenti in mare" },
      { src: "assets/img/ia-mare.svg", didascalia: "Monitoraggio con intelligenza artificiale" },
      { src: "assets/img/barcola.svg", didascalia: "Il Golfo di Trieste" }
    ]
  },
  {
    id: "sin-torviscosa",
    titolo: "Bonifiche: passo avanti per il Sito di Interesse Nazionale di Torviscosa",
    categoria: "ambiente",
    data: "",
    verificato: false,
    fonte: "",
    immagine: "assets/img/bonifiche.svg",
    sintesi: "Risanare le aree industriali significa restituire terreni sicuri alle comunità e nuove possibilità di sviluppo al territorio.",
    testo: [
      "Il Sito di Interesse Nazionale (SIN) di Torviscosa è una delle partite ambientali più rilevanti per il Friuli Venezia Giulia. La Regione ha lavorato per sbloccare l’iter di bonifica, in raccordo con il Ministero competente e con gli enti locali.",
      "Accanto alle bonifiche prosegue il rafforzamento di ARPA FVG (Agenzia regionale per la protezione dell’ambiente del Friuli Venezia Giulia), con nuove sedi e strumentazioni per controlli sempre più puntuali.",
      "Testo da completare con gli estremi degli atti e lo stato di avanzamento ufficiale dell’iter."
    ],
    galleria: [
      { src: "assets/img/bonifiche.svg", didascalia: "Area industriale" },
      { src: "assets/img/sopralluogo.svg", didascalia: "Sopralluogo tecnico" }
    ]
  },
  {
    id: "enpa-efficientamento",
    titolo: "Benessere animale: sostegno all’efficientamento energetico delle sedi ENPA",
    categoria: "territorio",
    data: "",
    verificato: false,
    fonte: "",
    immagine: "assets/img/comunita.svg",
    sintesi: "Sedi più efficienti significano meno costi in bolletta e più risorse per la cura degli animali accolti dai volontari.",
    testo: [
      "Chi si prende cura degli animali abbandonati merita strutture adeguate. Per questo la Regione sostiene l’efficientamento energetico delle sedi dell’ENPA (Ente nazionale protezione animali) presenti sul territorio.",
      "Un intervento concreto che unisce due obiettivi: ridurre i consumi e liberare risorse da destinare al benessere animale e all’attività dei volontari.",
      "Testo da completare con sedi interessate e importi ufficiali."
    ],
    galleria: [
      { src: "assets/img/comunita.svg", didascalia: "Una sede di accoglienza" }
    ]
  },
  {
    id: "nuova-costa-barcola",
    titolo: "“La nuova costa di Barcola”: presentato il progetto per il lungomare di Trieste",
    categoria: "territorio",
    data: "2023-11-16",
    verificato: true,
    fonte: "https://intrieste.com/?p=22207",
    fonteNome: "InTrieste, 16 novembre 2023",
    immagine: "assets/img/barcola.svg",
    sintesi: "Un progetto in due parti, lato mare e linea di costa, da realizzare per fasi senza togliere ai triestini l’uso della spiaggia durante l’estate.",
    testo: [
      "L’assessore regionale Fabio Scoccimarro ha illustrato a istituzioni e associazioni di categoria il progetto “La nuova costa di Barcola: progetti, idee e futuro”, elaborato dallo studio Metroarea con l’architetto Giulio Paladini.",
      "Il progetto si articola in due parti destinate a confluire in un’unica realizzazione: il lato mare, dedicato a sicurezza, balneazione e strutture collegate; la linea di costa, con strade e parcheggi. Sono previste nuove baie, la protezione della costa e spazi per gli sport acquatici.",
      "Le priorità indicate sono il rispetto delle tradizioni dei residenti, l’attrattiva turistica, l’accessibilità per le persone più fragili e spazi dedicati agli animali.",
      "L’iter prevede l’adozione di una variante al Piano regolatore comunale, la redazione dei progetti esecutivi, le gare d’appalto e l’attuazione graduale dei lavori, con un orizzonte complessivo di circa vent’anni."
    ],
    galleria: [
      { src: "assets/img/barcola.svg", didascalia: "La costa di Barcola" },
      { src: "assets/img/mare-giovani.svg", didascalia: "Sport acquatici" },
      { src: "assets/img/conferenza.svg", didascalia: "Presentazione del progetto" }
    ]
  },
  {
    id: "cooperazione-golfo",
    titolo: "Un Golfo, tre Paesi: cooperazione ambientale con Slovenia e Croazia",
    categoria: "ambiente",
    data: "",
    verificato: false,
    fonte: "",
    immagine: "assets/img/mare-giovani.svg",
    sintesi: "Il mare non conosce confini: la tutela dell’Alto Adriatico passa da un lavoro comune con i Paesi vicini.",
    testo: [
      "La qualità delle acque e la sicurezza della navigazione nel Golfo di Trieste riguardano allo stesso modo Italia, Slovenia e Croazia. La Regione promuove tavoli di cooperazione per condividere dati, buone pratiche e strategie di intervento.",
      "Testo da completare con gli accordi o gli incontri ufficiali di riferimento."
    ],
    galleria: [
      { src: "assets/img/mare-giovani.svg", didascalia: "Alto Adriatico" }
    ]
  },
  {
    id: "impianti-sportivi-storici",
    titolo: "Impianti sportivi storici più efficienti e più sostenibili",
    categoria: "eventi",
    data: "2026-07-23",
    verificato: true,
    fonte: "https://www.italpress.com/?p=719803",
    fonteNome: "Italpress, 23 luglio 2026",
    immagine: "assets/img/comunita.svg",
    sintesi: "Nella manovra estiva 7 milioni di euro per l’efficientamento ecologico degli impianti sportivi: luoghi di comunità che meritano di durare nel tempo.",
    testo: [
      "Le società sportive sono presidi di comunità, soprattutto per i più giovani. Con la manovra estiva 2026 la Regione ha destinato 7 milioni di euro all’efficientamento ecologico degli impianti sportivi.",
      "Ridurre i consumi energetici delle strutture significa abbassare i costi di gestione e mettere le società nelle condizioni di investire su attività, allenatori e ragazzi."
    ],
    galleria: [
      { src: "assets/img/comunita.svg", didascalia: "Strutture per la comunità" }
    ]
  },
  {
    id: "energia-imprese",
    titolo: "Energia e competitività: diversificare le fonti per sostenere famiglie e imprese",
    categoria: "energia",
    data: "",
    verificato: false,
    fonte: "",
    immagine: "assets/img/energia.svg",
    sintesi: "Una strategia energetica che guarda ai costi reali di chi lavora e produce, senza scorciatoie ideologiche.",
    testo: [
      "La transizione energetica funziona se è sostenibile anche nei conti di famiglie e imprese. La strategia regionale punta sulla diversificazione delle fonti, sulle comunità energetiche rinnovabili e sul sostegno al tessuto produttivo per ridurre i costi.",
      "Testo da completare con i riferimenti al Piano energetico regionale e alle misure attive."
    ],
    galleria: [
      { src: "assets/img/energia.svg", didascalia: "Fonti rinnovabili" }
    ]
  }
];

window.CATEGORIE = {
  ambiente: { nome: "Ambiente", classe: "" },
  energia: { nome: "Energia", classe: "etichetta--energia" },
  territorio: { nome: "Territorio e Trieste", classe: "etichetta--territorio" },
  eventi: { nome: "Eventi e Sport", classe: "etichetta--eventi" }
};
