#!/usr/bin/env node
/*
 * ispeziona.js
 * Apre una pagina HTML nel navigatore, la fotografa in formato telefono e
 * scrivania e raccoglie misure oggettive su usabilita', accessibilita' e peso.
 *
 * Uso:
 *   node ispeziona.js <pagina.html | indirizzo> <cartella di uscita> [radice]
 *
 * Un file locale viene servito da un piccolo servitore web interno, cosi'
 * funzionano anche le pagine che leggono i dati con fetch. La radice del
 * servitore e' la cartella del repository git che contiene il file (oppure la
 * cartella del file); si puo' indicarne un'altra come terzo argomento.
 *
 * Produce nella cartella di uscita:
 *   telefono.png, scrivania.png   fotografie a pagina intera
 *   telefono-inizio.png, scrivania-inizio.png   solo la prima schermata
 *   testo.txt                     testo reso dal navigatore
 *   rapporto.json                 tutte le misure
 * e stampa a schermo una sintesi leggibile.
 */
const fs = require('fs');
const path = require('path');
const { pathToFileURL } = require('url');

let chromium;
try {
  ({ chromium } = require('playwright'));
} catch (e) {
  console.error(
    'Playwright non disponibile. Installarlo con "npm install playwright" e ' +
      '"npx playwright install chromium", oppure eseguire le verifiche a mano ' +
      'seguendo la sezione "Senza navigatore" di SKILL.md.'
  );
  process.exit(2);
}

const http = require('http');
const [, , bersaglio, cartella, radiceIndicata] = process.argv;
if (!bersaglio || !cartella) {
  console.error('Uso: node ispeziona.js <pagina.html | indirizzo> <cartella di uscita>');
  process.exit(2);
}

const eRemoto = /^https?:\/\//i.test(bersaglio);
let indirizzo = eRemoto ? bersaglio : pathToFileURL(path.resolve(bersaglio)).href;
fs.mkdirSync(cartella, { recursive: true });

const TIPI = {
  '.html': 'text/html; charset=utf-8', '.htm': 'text/html; charset=utf-8',
  '.css': 'text/css; charset=utf-8', '.js': 'text/javascript; charset=utf-8',
  '.mjs': 'text/javascript; charset=utf-8', '.json': 'application/json; charset=utf-8',
  '.geojson': 'application/json; charset=utf-8', '.csv': 'text/csv; charset=utf-8',
  '.txt': 'text/plain; charset=utf-8', '.xml': 'application/xml', '.svg': 'image/svg+xml',
  '.png': 'image/png', '.jpg': 'image/jpeg', '.jpeg': 'image/jpeg', '.gif': 'image/gif',
  '.webp': 'image/webp', '.avif': 'image/avif', '.ico': 'image/x-icon',
  '.woff': 'font/woff', '.woff2': 'font/woff2', '.ttf': 'font/ttf',
  '.mp4': 'video/mp4', '.webm': 'video/webm', '.vtt': 'text/vtt', '.pdf': 'application/pdf',
};

function trovaRadice(file) {
  if (radiceIndicata) return path.resolve(radiceIndicata);
  for (let d = path.dirname(file); ; d = path.dirname(d)) {
    if (fs.existsSync(path.join(d, '.git'))) return d;
    if (d === path.dirname(d)) break;
  }
  return path.dirname(file);
}

function avviaServitore(radice) {
  const servitore = http.createServer((richiesta, risposta) => {
    let relativo;
    try {
      relativo = decodeURIComponent(new URL(richiesta.url, 'http://x').pathname);
    } catch (e) {
      risposta.writeHead(400).end();
      return;
    }
    let file = path.join(radice, relativo);
    if (!file.startsWith(radice)) {
      risposta.writeHead(403).end();
      return;
    }
    if (fs.existsSync(file) && fs.statSync(file).isDirectory()) file = path.join(file, 'index.html');
    if (!fs.existsSync(file)) {
      risposta.writeHead(404).end();
      return;
    }
    risposta.writeHead(200, {
      'Content-Type': TIPI[path.extname(file).toLowerCase()] || 'application/octet-stream',
      'Content-Length': fs.statSync(file).size,
    });
    fs.createReadStream(file).pipe(risposta);
  });
  return new Promise((ok) => servitore.listen(0, '127.0.0.1', () => ok(servitore)));
}

const FORMATI = [
  { nome: 'telefono', width: 390, height: 844, isMobile: true, hasTouch: true },
  { nome: 'scrivania', width: 1440, height: 900, isMobile: false, hasTouch: false },
];

/* Misure eseguite dentro la pagina. */
function misuraPagina(eTelefono) {
  const visibile = (el) => {
    const r = el.getBoundingClientRect();
    if (r.width === 0 || r.height === 0) return false;
    const s = getComputedStyle(el);
    return s.visibility !== 'hidden' && s.display !== 'none' && parseFloat(s.opacity) > 0.05;
  };
  const descrivi = (el) => {
    let d = el.tagName.toLowerCase();
    if (el.id) d += '#' + el.id;
    else if (el.classList.length) d += '.' + [...el.classList].slice(0, 2).join('.');
    const t = (el.innerText || el.getAttribute('aria-label') || '').trim().replace(/\s+/g, ' ');
    return t ? d + ' «' + t.slice(0, 50) + '»' : d;
  };

  /* Colori e contrasto */
  const leggiColore = (testo) => {
    const m = /^rgba?\(([^)]+)\)$/.exec(testo.trim());
    if (!m) return null;
    const p = m[1].split(/[\s,\/]+/).filter(Boolean).map(parseFloat);
    if (p.length < 3 || p.some(Number.isNaN)) return null;
    return { r: p[0], g: p[1], b: p[2], a: p.length > 3 ? p[3] : 1 };
  };
  const sovrapponi = (sopra, sotto) => ({
    r: sopra.r * sopra.a + sotto.r * (1 - sopra.a),
    g: sopra.g * sopra.a + sotto.g * (1 - sopra.a),
    b: sopra.b * sopra.a + sotto.b * (1 - sopra.a),
    a: 1,
  });
  const luminanza = (c) => {
    const f = (v) => {
      v /= 255;
      return v <= 0.03928 ? v / 12.92 : Math.pow((v + 0.055) / 1.055, 2.4);
    };
    return 0.2126 * f(c.r) + 0.7152 * f(c.g) + 0.0722 * f(c.b);
  };
  const sfondoEffettivo = (el) => {
    const strati = [];
    for (let n = el; n && n.nodeType === 1; n = n.parentElement) {
      const s = getComputedStyle(n);
      if (s.backgroundImage && s.backgroundImage !== 'none') return null;
      const c = leggiColore(s.backgroundColor);
      if (c === null) return null;
      if (c.a > 0) {
        strati.push(c);
        if (c.a >= 1) break;
      }
    }
    let base = { r: 255, g: 255, b: 255, a: 1 };
    for (let i = strati.length - 1; i >= 0; i--) base = sovrapponi(strati[i], base);
    return base;
  };

  const contrastoBasso = [];
  let testiValutati = 0;
  let testiNonValutabili = 0;
  const caratteriPiccoli = [];
  const giaVisti = new Set();
  const camminatore = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
  for (let nodo = camminatore.nextNode(); nodo; nodo = camminatore.nextNode()) {
    if (!nodo.nodeValue.trim()) continue;
    const el = nodo.parentElement;
    if (!el || giaVisti.has(el)) continue;
    giaVisti.add(el);
    if (['SCRIPT', 'STYLE', 'NOSCRIPT', 'TEMPLATE'].includes(el.tagName)) continue;
    if (el.closest('svg')) continue; // il testo negli SVG usa fill: si controlla a occhio
    if (!visibile(el)) continue;
    const s = getComputedStyle(el);
    const corpo = parseFloat(s.fontSize);
    if (corpo < 12) caratteriPiccoli.push({ elemento: descrivi(el), corpo: corpo });
    const colore = leggiColore(s.color);
    const sfondo = sfondoEffettivo(el);
    if (!colore || !sfondo) {
      testiNonValutabili++;
      continue;
    }
    testiValutati++;
    const davanti = sovrapponi(colore, sfondo);
    const l1 = luminanza(davanti);
    const l2 = luminanza(sfondo);
    const rapporto = (Math.max(l1, l2) + 0.05) / (Math.min(l1, l2) + 0.05);
    const grassetto = parseInt(s.fontWeight, 10) >= 700;
    const grande = corpo >= 24 || (corpo >= 18.66 && grassetto);
    const soglia = grande ? 3 : 4.5;
    if (rapporto < soglia) {
      contrastoBasso.push({
        elemento: descrivi(el),
        rapporto: Math.round(rapporto * 100) / 100,
        soglia: soglia,
        colore: s.color,
      });
    }
  }

  /* Elementi interattivi */
  const interattivi = [
    ...document.querySelectorAll(
      'a[href], button, input:not([type=hidden]), select, textarea, summary, [role=button], [role=tab], [tabindex]:not([tabindex="-1"])'
    ),
  ].filter(visibile);
  const senzaNome = [];
  const bersagliPiccoli = [];
  let bersagliSotto44 = 0;
  for (const el of interattivi) {
    const nome =
      (el.innerText || '').trim() ||
      el.getAttribute('aria-label') ||
      el.getAttribute('aria-labelledby') ||
      el.getAttribute('title') ||
      el.getAttribute('alt') ||
      el.getAttribute('placeholder') ||
      (el.labels && el.labels.length ? 'x' : '') ||
      (el.querySelector('img[alt]:not([alt=""]), svg title') ? 'x' : '') ||
      (el.tagName === 'INPUT' && ['submit', 'button', 'reset'].includes(el.type) ? el.value : '');
    if (!nome) senzaNome.push(descrivi(el));
    if (eTelefono && getComputedStyle(el).display !== 'inline') {
      const r = el.getBoundingClientRect();
      if (r.width < 24 || r.height < 24) {
        bersagliPiccoli.push({
          elemento: descrivi(el),
          misura: Math.round(r.width) + ' x ' + Math.round(r.height),
        });
      } else if (r.width < 44 || r.height < 44) bersagliSotto44++;
    }
  }

  /* Immagini, grafica, video, cornici */
  const immaginiSenzaAlt = [...document.querySelectorAll('img:not([alt])')].map(descrivi);
  const svgSenzaDescrizione = [...document.querySelectorAll('svg')]
    .filter(visibile)
    .filter((s) => {
      const r = s.getBoundingClientRect();
      if (r.width < 48 && r.height < 48) return false; // icone
      if (s.getAttribute('aria-hidden') === 'true') return false;
      return !(
        s.querySelector(':scope > title') ||
        s.getAttribute('aria-label') ||
        s.getAttribute('aria-labelledby')
      );
    })
    .map(descrivi);
  const canvasSenzaAlternativa = [...document.querySelectorAll('canvas')]
    .filter((c) => !c.getAttribute('aria-label') && !c.textContent.trim())
    .map(descrivi);
  const video = [...document.querySelectorAll('video')].map((v) => ({
    elemento: descrivi(v),
    comandi: v.hasAttribute('controls'),
    avvioAutomatico: v.hasAttribute('autoplay'),
    muto: v.muted,
    sottotitoli: !!v.querySelector('track[kind=captions], track[kind=subtitles]'),
    precaricamento: v.getAttribute('preload') || 'non indicato',
    anteprima: v.hasAttribute('poster'),
  }));
  const cornici = [...document.querySelectorAll('iframe')].map((f) => ({
    sorgente: f.getAttribute('src') || f.getAttribute('data-src') || '',
    titolo: f.getAttribute('title') || '',
    differita: f.getAttribute('loading') === 'lazy',
  }));

  /* Struttura */
  const titoli = [...document.querySelectorAll('h1,h2,h3,h4,h5,h6')].filter(visibile);
  const saltiTitoli = [];
  let precedente = 0;
  for (const t of titoli) {
    const livello = parseInt(t.tagName[1], 10);
    if (precedente && livello > precedente + 1) {
      saltiTitoli.push('da h' + precedente + ' a h' + livello + ': ' + descrivi(t));
    }
    precedente = livello;
  }
  const tabelleSenzaIntestazioni = [...document.querySelectorAll('table')]
    .filter((t) => !t.querySelector('th'))
    .map(descrivi);

  /* Scorrimento orizzontale */
  const larghezza = document.documentElement.clientWidth;
  const sforamento = document.documentElement.scrollWidth - larghezza;
  const elementiCheSforano = [];
  if (sforamento > 1) {
    for (const el of document.body.querySelectorAll('*')) {
      if (!visibile(el)) continue;
      const r = el.getBoundingClientRect();
      if (r.right > larghezza + 1 && r.width <= larghezza * 3) {
        // si tengono solo gli elementi piu' interni
        if (![...el.children].some((f) => f.getBoundingClientRect().right > larghezza + 1)) {
          elementiCheSforano.push(descrivi(el));
        }
      }
      if (elementiCheSforano.length >= 10) break;
    }
  }

  /* Animazioni e rispetto del movimento ridotto */
  let regolaMovimentoRidotto = false;
  let usaAnimazioniCss = false;
  const esamina = (regole) => {
    for (const r of regole) {
      if (r.media && /prefers-reduced-motion/.test(r.conditionText || r.media.mediaText || '')) {
        regolaMovimentoRidotto = true;
      }
      if (r.type === CSSRule.KEYFRAMES_RULE) usaAnimazioniCss = true;
      if (r.style && (r.style.animationName || r.style.transitionDuration)) usaAnimazioniCss = true;
      if (r.cssRules) esamina(r.cssRules);
    }
  };
  for (const foglio of document.styleSheets) {
    try {
      esamina(foglio.cssRules);
    } catch (e) {
      /* foglio esterno non leggibile */
    }
  }
  const animazioniAttive = document.getAnimations ? document.getAnimations() : [];
  const animazioniSenzaFine = animazioniAttive.filter((a) => {
    try {
      return a.effect && a.effect.getComputedTiming().iterations === Infinity && a.playState === 'running';
    } catch (e) {
      return false;
    }
  }).length;

  return {
    lingua: document.documentElement.getAttribute('lang') || '',
    titoloPagina: document.title,
    metaViewport: !!document.querySelector('meta[name=viewport]'),
    numeroH1: document.querySelectorAll('h1').length,
    saltiTitoli: saltiTitoli,
    puntiDiRiferimento: {
      main: !!document.querySelector('main, [role=main]'),
      nav: !!document.querySelector('nav, [role=navigation]'),
    },
    nodi: document.getElementsByTagName('*').length,
    altezzaPagina: document.documentElement.scrollHeight,
    schermate: Math.round((document.documentElement.scrollHeight / window.innerHeight) * 10) / 10,
    sforamentoOrizzontale: Math.max(0, sforamento),
    elementiCheSforano: elementiCheSforano,
    testiValutati: testiValutati,
    testiNonValutabili: testiNonValutabili,
    contrastoBasso: contrastoBasso.slice(0, 40),
    contrastoBassoTotale: contrastoBasso.length,
    caratteriPiccoli: caratteriPiccoli.slice(0, 20),
    caratteriPiccoliTotale: caratteriPiccoli.length,
    interattivi: interattivi.length,
    interattiviSenzaNome: senzaNome.slice(0, 20),
    bersagliPiccoli: bersagliPiccoli.slice(0, 20),
    bersagliPiccoliTotale: bersagliPiccoli.length,
    bersagliSotto44: bersagliSotto44,
    immagini: document.images.length,
    immaginiSenzaAlt: immaginiSenzaAlt.slice(0, 20),
    svg: document.querySelectorAll('svg').length,
    svgSenzaDescrizione: svgSenzaDescrizione.slice(0, 20),
    canvasSenzaAlternativa: canvasSenzaAlternativa,
    tabelle: document.querySelectorAll('table').length,
    tabelleSenzaIntestazioni: tabelleSenzaIntestazioni,
    video: video,
    cornici: cornici,
    usaAnimazioniCss: usaAnimazioniCss,
    regolaMovimentoRidotto: regolaMovimentoRidotto,
    animazioniAttive: animazioniAttive.length,
    animazioniSenzaFine: animazioniSenzaFine,
  };
}

async function scorriTutto(page) {
  // Fa comparire i contenuti che si rivelano allo scorrimento, poi torna in cima.
  await page.evaluate(async () => {
    const passo = Math.max(200, Math.floor(window.innerHeight * 0.8));
    for (let y = 0; y < document.documentElement.scrollHeight; y += passo) {
      window.scrollTo(0, y);
      await new Promise((r) => setTimeout(r, 60));
    }
    window.scrollTo(0, 0);
    await new Promise((r) => setTimeout(r, 200));
  });
}

(async () => {
  const rapporto = { pagina: bersaglio, data: new Date().toISOString(), formati: {} };
  if (!eRemoto) {
    rapporto.pesoFileHtml = fs.statSync(path.resolve(bersaglio)).size;
  }
  let servitore = null;
  if (!eRemoto) {
    const file = path.resolve(bersaglio);
    const radice = trovaRadice(file);
    servitore = await avviaServitore(radice);
    const relativo = path.relative(radice, file).split(path.sep).map(encodeURIComponent).join('/');
    indirizzo = 'http://127.0.0.1:' + servitore.address().port + '/' + relativo;
    rapporto.radiceServita = radice;
  }
  const origineLocale = new URL(indirizzo).host;
  const browser = await chromium.launch();

  for (const f of FORMATI) {
    const contesto = await browser.newContext({
      viewport: { width: f.width, height: f.height },
      isMobile: f.isMobile,
      hasTouch: f.hasTouch,
      deviceScaleFactor: 1,
    });
    const page = await contesto.newPage();
    const erroriConsole = [];
    const richieste = [];
    const fallite = [];
    page.on('console', (m) => {
      if (m.type() === 'error') erroriConsole.push(m.text().slice(0, 300));
    });
    page.on('pageerror', (e) => erroriConsole.push(String(e).slice(0, 300)));
    page.on('requestfailed', (r) => fallite.push(r.url().slice(0, 200)));
    page.on('response', async (r) => {
      let peso = 0;
      try {
        peso = (await r.body()).length;
      } catch (e) {
        /* risposta senza corpo */
      }
      richieste.push({ url: r.url(), peso: peso, tipo: r.request().resourceType() });
    });

    const inizio = Date.now();
    try {
      await page.goto(indirizzo, { waitUntil: 'load', timeout: 45000 });
    } catch (e) {
      erroriConsole.push('Caricamento non completato: ' + String(e).slice(0, 200));
    }
    const tempoCaricamento = Date.now() - inizio;
    await page.waitForLoadState('networkidle', { timeout: 8000 }).catch(() => {});
    await page.waitForTimeout(800);

    await page.screenshot({ path: path.join(cartella, f.nome + '-inizio.png') });
    await scorriTutto(page);
    const misure = await page.evaluate(misuraPagina, f.isMobile);
    await page.screenshot({ path: path.join(cartella, f.nome + '.png'), fullPage: true });

    if (f.nome === 'scrivania') {
      const testo = await page.evaluate(() => document.body.innerText);
      fs.writeFileSync(path.join(cartella, 'testo.txt'), testo);
    }

    const esterne = richieste.filter(
      (r) => /^https?:/.test(r.url) && new URL(r.url).host !== origineLocale
    );
    rapporto.formati[f.nome] = {
      ...misure,
      tempoCaricamentoMs: tempoCaricamento,
      erroriConsole: [...new Set(erroriConsole)].slice(0, 20),
      richiesteFallite: [...new Set(fallite)].slice(0, 20),
      numeroRichieste: richieste.length,
      pesoTotale: richieste.reduce((s, r) => s + r.peso, 0),
      risorseEsterne: [...new Set(esterne.map((r) => r.url.slice(0, 160)))].slice(0, 30),
    };
    await contesto.close();
  }

  /* Seconda passata con movimento ridotto: nessuna animazione deve restare in ciclo. */
  {
    const contesto = await browser.newContext({
      viewport: { width: 1440, height: 900 },
      reducedMotion: 'reduce',
    });
    const page = await contesto.newPage();
    try {
      await page.goto(indirizzo, { waitUntil: 'load', timeout: 45000 });
      await page.waitForTimeout(800);
      await scorriTutto(page);
      rapporto.movimentoRidotto = await page.evaluate(() => {
        const tutte = document.getAnimations ? document.getAnimations() : [];
        const inCiclo = tutte.filter((a) => {
          try {
            return (
              a.playState === 'running' &&
              a.effect &&
              (a.effect.getComputedTiming().iterations === Infinity ||
                a.effect.getComputedTiming().activeDuration > 1000)
            );
          } catch (e) {
            return false;
          }
        });
        const videoInAvvio = [...document.querySelectorAll('video')].filter((v) => !v.paused).length;
        return { animazioniAncoraAttive: inCiclo.length, videoInRiproduzione: videoInAvvio };
      });
    } catch (e) {
      rapporto.movimentoRidotto = { errore: String(e).slice(0, 200) };
    }
    await contesto.close();
  }

  await browser.close();
  if (servitore) servitore.close();
  fs.writeFileSync(path.join(cartella, 'rapporto.json'), JSON.stringify(rapporto, null, 2));

  /* Sintesi a schermo */
  const kb = (n) => (n / 1024).toFixed(0) + ' kB';
  const righe = [];
  righe.push('PAGINA: ' + bersaglio);
  if (rapporto.pesoFileHtml) righe.push('Peso del file HTML: ' + kb(rapporto.pesoFileHtml));
  for (const f of FORMATI) {
    const m = rapporto.formati[f.nome];
    righe.push('');
    righe.push('== ' + f.nome.toUpperCase() + ' (' + f.width + ' x ' + f.height + ') ==');
    righe.push(
      'Caricamento: ' + m.tempoCaricamentoMs + ' ms, ' + m.numeroRichieste + ' richieste, ' +
        kb(m.pesoTotale) + ', ' + m.nodi + ' nodi, ' + m.schermate + ' schermate di altezza'
    );
    righe.push('Errori in console: ' + m.erroriConsole.length + ', richieste fallite: ' + m.richiesteFallite.length);
    righe.push('Risorse esterne: ' + m.risorseEsterne.length);
    righe.push(
      'Scorrimento orizzontale: ' +
        (m.sforamentoOrizzontale > 1 ? 'SI, ' + m.sforamentoOrizzontale + ' px (' + m.elementiCheSforano.slice(0, 3).join('; ') + ')' : 'no')
    );
    righe.push(
      'Contrasto insufficiente: ' + m.contrastoBassoTotale + ' su ' + m.testiValutati +
        ' testi valutati (' + m.testiNonValutabili + ' non valutabili, da guardare a occhio)'
    );
    righe.push('Caratteri sotto 12 px: ' + m.caratteriPiccoliTotale);
    if (f.isMobile) {
      righe.push('Bersagli al tocco sotto 24 px: ' + m.bersagliPiccoliTotale + ', tra 24 e 44 px: ' + m.bersagliSotto44);
    }
    righe.push(
      'Interattivi senza nome: ' + m.interattiviSenzaNome.length + ', immagini senza alt: ' +
        m.immaginiSenzaAlt.length + ', SVG senza descrizione: ' + m.svgSenzaDescrizione.length +
        ', tabelle senza intestazioni: ' + m.tabelleSenzaIntestazioni.length
    );
    righe.push(
      'Struttura: lang="' + m.lingua + '", h1: ' + m.numeroH1 + ', salti di livello nei titoli: ' +
        m.saltiTitoli.length + ', main: ' + (m.puntiDiRiferimento.main ? 'si' : 'no') +
        ', meta viewport: ' + (m.metaViewport ? 'si' : 'no')
    );
    righe.push(
      'Animazioni: ' + m.animazioniAttive + ' attive, ' + m.animazioniSenzaFine + ' in ciclo continuo, regola per il movimento ridotto: ' +
        (m.regolaMovimentoRidotto ? 'si' : m.usaAnimazioniCss ? 'NO (manca)' : 'non serve')
    );
    righe.push('Video: ' + m.video.length + ', cornici incorporate: ' + m.cornici.length);
  }
  if (rapporto.movimentoRidotto && !rapporto.movimentoRidotto.errore) {
    righe.push('');
    righe.push(
      'Con movimento ridotto: ' + rapporto.movimentoRidotto.animazioniAncoraAttive +
        ' animazioni ancora attive, ' + rapporto.movimentoRidotto.videoInRiproduzione + ' video in riproduzione'
    );
  }
  righe.push('');
  righe.push('Dettagli in ' + path.join(cartella, 'rapporto.json') + ', fotografie nella stessa cartella.');
  console.log(righe.join('\n'));
})().catch((e) => {
  console.error('Ispezione fallita: ' + e);
  process.exit(1);
});
