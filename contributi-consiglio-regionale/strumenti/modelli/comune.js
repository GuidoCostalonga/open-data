/* Funzioni comuni alle due dashboard: formati, mappa, grafici, tabelle, esportazione. */
function raggruppa(v, d) {
  const neg = v < 0, s = Math.abs(v).toFixed(d), [i, dec] = s.split(".");
  return (neg ? "-" : "") + i.replace(/\B(?=(\d{3})+(?!\d))/g, ".") + (dec ? "," + dec : "");
}
const F = {
  euro(v, dec) {
    if (v == null || !isFinite(v)) return "–";
    const d = dec == null ? (Math.abs(v) >= 1000 ? 0 : 2) : dec;
    return raggruppa(v, d) + "\u00a0€";
  },
  euroBreve(v) {
    if (v == null || !isFinite(v)) return "–";
    const a = Math.abs(v);
    if (a >= 1e6) return (v / 1e6).toLocaleString("it-IT", { maximumFractionDigits: 2 }) + "\u00a0mln\u00a0€";
    if (a >= 1e4) return (v / 1e3).toLocaleString("it-IT", { maximumFractionDigits: 0 }) + "\u00a0mila\u00a0€";
    return raggruppa(Math.round(v), 0) + "\u00a0€";
  },
  num(v, dec = 0) {
    if (v == null || !isFinite(v)) return "–";
    return raggruppa(v, dec);
  },
  pct(v, dec = 1, segno = false) {
    if (v == null || !isFinite(v)) return "–";
    const s = v.toLocaleString("it-IT", { minimumFractionDigits: dec, maximumFractionDigits: dec }) + "%";
    return segno && v > 0 ? "+" + s : s;
  },
  data(iso) {
    if (!iso) return "–";
    const [a, m, g] = iso.slice(0, 10).split("-");
    return `${g}/${m}/${a}`;
  },
  esc(s) {
    return String(s == null ? "" : s).replace(/[&<>"']/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
  },
};
const MESI = ["gennaio", "febbraio", "marzo", "aprile", "maggio", "giugno", "luglio", "agosto", "settembre", "ottobre", "novembre", "dicembre"];
const MESI_B = ["gen", "feb", "mar", "apr", "mag", "giu", "lug", "ago", "set", "ott", "nov", "dic"];
const PROV_NOME = { GO: "Gorizia", PN: "Pordenone", TS: "Trieste", UD: "Udine", VE: "Venezia (fuori regione)" };
const FASCE_POP = [
  { id: "a", et: "fino a 1.000 abitanti", min: 0, max: 1000 },
  { id: "b", et: "1.001 – 3.000", min: 1001, max: 3000 },
  { id: "c", et: "3.001 – 5.000", min: 3001, max: 5000 },
  { id: "d", et: "5.001 – 10.000", min: 5001, max: 10000 },
  { id: "e", et: "10.001 – 20.000", min: 10001, max: 20000 },
  { id: "f", et: "oltre 20.000", min: 20001, max: Infinity },
];
const fasciaPop = (p) => (p == null ? null : FASCE_POP.find((f) => p >= f.min && p <= f.max));

function el(tag, attrs = {}, html) {
  const e = document.createElement(tag);
  for (const k in attrs) e.setAttribute(k, attrs[k]);
  if (html != null) e.innerHTML = html;
  return e;
}
const NS = "http://www.w3.org/2000/svg";
function sv(tag, attrs = {}) {
  const e = document.createElementNS(NS, tag);
  for (const k in attrs) e.setAttribute(k, attrs[k]);
  return e;
}
const css = (n) => getComputedStyle(document.documentElement).getPropertyValue(n).trim();

/* ---------------- tooltip ---------------- */
const Tip = {
  e: null,
  mostra(html, ev) {
    if (!this.e) { this.e = el("div", { class: "tooltip", role: "status" }); document.body.appendChild(this.e); }
    this.e.innerHTML = html;
    this.e.hidden = false;
    this.sposta(ev);
  },
  sposta(ev) {
    if (!this.e || this.e.hidden) return;
    const w = this.e.offsetWidth, h = this.e.offsetHeight;
    let x = ev.clientX + 14, y = ev.clientY + 14;
    if (x + w > innerWidth - 8) x = ev.clientX - w - 14;
    if (y + h > innerHeight - 8) y = ev.clientY - h - 14;
    this.e.style.left = Math.max(8, x) + "px";
    this.e.style.top = Math.max(8, y) + "px";
  },
  nascondi() { if (this.e) this.e.hidden = true; },
};

/* ---------------- classi di colore ---------------- */
function classiQuantili(valori, n = 6) {
  const v = valori.filter((x) => x != null && isFinite(x) && x > 0).sort((a, b) => a - b);
  if (!v.length) return [];
  const uniq = [...new Set(v)];
  if (uniq.length <= n) return uniq.slice(0, -1).map((x, i) => (x + uniq[i + 1]) / 2);
  const br = [];
  for (let i = 1; i < n; i++) br.push(arrotonda(v[Math.floor((i * v.length) / n)]));
  return [...new Set(br)];
}
function arrotonda(x) {
  if (x <= 0) return x;
  const m = Math.pow(10, Math.floor(Math.log10(x)) - 1);
  return Math.round(x / m) * m;
}
function classiDivergenti(valori) {
  const a = valori.filter((x) => x != null && isFinite(x)).map(Math.abs).sort((p, q) => p - q);
  if (!a.length) return [];
  const q = (p) => arrotonda(a[Math.min(a.length - 1, Math.floor(p * a.length))] || 1);
  const b1 = q(0.5), b2 = Math.max(q(0.85), b1 * 1.5);
  return [-b2, -b1, 0, b1, b2];
}

/* ---------------- mappa ---------------- */
class Mappa {
  constructor(box, geo, prov, comuni, opz) {
    this.box = box; this.opz = opz; this.comuni = comuni;
    const lat0 = 46.1, kx = Math.cos((lat0 * Math.PI) / 180);
    let x0 = 1e9, x1 = -1e9, y0 = 1e9, y1 = -1e9;
    for (const c in geo) for (const p of geo[c]) for (const [x, y] of p[0]) { x0 = Math.min(x0, x); x1 = Math.max(x1, x); y0 = Math.min(y0, y); y1 = Math.max(y1, y); }
    const W = 1000, s = (W - 20) / ((x1 - x0) * kx), H = Math.round((y1 - y0) * s) + 20;
    this.W = W; this.H = H;
    this.pr = ([x, y]) => [(x - x0) * kx * s + 10, (y1 - y) * s + 10];
    const d = (polys) => polys.map((poly) => poly.map((r) => "M" + r.map((pt) => this.pr(pt).map((v) => v.toFixed(1)).join(",")).join("L") + "Z").join("")).join("");
    this.svg = sv("svg", { viewBox: `0 0 ${W} ${H}`, role: "img", "aria-label": opz.etichetta || "Mappa dei Comuni del Friuli Venezia Giulia" });
    this.g = sv("g");
    this.svg.appendChild(this.g);
    this.paths = {};
    for (const c of comuni) {
      if (!geo[c.c]) continue;
      const p = sv("path", { d: d(geo[c.c]), class: "com", tabindex: "0", "data-c": c.c });
      p.setAttribute("aria-label", c.n);
      this.g.appendChild(p);
      this.paths[c.c] = p;
    }
    for (const k in prov) this.g.appendChild(sv("path", { d: d(prov[k]), class: "prov" }));
    this.gb = sv("g"); this.g.appendChild(this.gb);
    this.gl = sv("g"); this.g.appendChild(this.gl);
    for (const nome of ["Trieste", "Udine", "Pordenone", "Gorizia"]) {
      const c = comuni.find((x) => x.n === nome);
      if (!c) continue;
      const [x, y] = this.pr(c.k);
      const t = sv("text", { x: x + 6, y: y - 6, class: "cap" });
      t.textContent = nome; this.gl.appendChild(t);
    }
    box.appendChild(this.svg);
    const z = el("div", { class: "zoom" });
    z.innerHTML = '<button type="button" aria-label="Ingrandisci">+</button><button type="button" aria-label="Riduci">−</button><button type="button" aria-label="Vista intera" style="font-size:14px">⤢</button>';
    box.appendChild(z);
    const [bp, bm, br] = z.querySelectorAll("button");
    bp.onclick = () => this.zoomA(1.6); bm.onclick = () => this.zoomA(1 / 1.6); br.onclick = () => this.reset();
    this.vb = { x: 0, y: 0, w: W, h: H };
    this.eventi();
  }
  applica() { this.svg.setAttribute("viewBox", `${this.vb.x} ${this.vb.y} ${this.vb.w} ${this.vb.h}`); const k = this.W / this.vb.w; this.gl.querySelectorAll("text").forEach((t) => { t.style.fontSize = 12 / k + "px"; t.style.strokeWidth = 3 / k + "px"; }); }
  reset() { this.vb = { x: 0, y: 0, w: this.W, h: this.H }; this.applica(); }
  zoomA(f, cx, cy) {
    const v = this.vb;
    const nw = Math.min(this.W, Math.max(this.W / 14, v.w / f)), nh = (nw * this.H) / this.W;
    cx = cx == null ? v.x + v.w / 2 : cx; cy = cy == null ? v.y + v.h / 2 : cy;
    const rx = (cx - v.x) / v.w, ry = (cy - v.y) / v.h;
    v.x = cx - rx * nw; v.y = cy - ry * nh; v.w = nw; v.h = nh;
    this.limita(); this.applica();
  }
  limita() { const v = this.vb; v.x = Math.min(Math.max(v.x, -v.w * 0.3), this.W - v.w * 0.7); v.y = Math.min(Math.max(v.y, -v.h * 0.3), this.H - v.h * 0.7); }
  pt(ev) { const r = this.svg.getBoundingClientRect(); return [this.vb.x + ((ev.clientX - r.left) / r.width) * this.vb.w, this.vb.y + ((ev.clientY - r.top) / r.height) * this.vb.h]; }
  eventi() {
    const sv_ = this.svg, punt = new Map();
    let mosso = false, ultimo = null, dist0 = null;
    sv_.addEventListener("wheel", (ev) => {
      if (!ev.ctrlKey && !ev.metaKey) return;
      ev.preventDefault();
      const [x, y] = this.pt(ev); this.zoomA(ev.deltaY < 0 ? 1.25 : 0.8, x, y);
    }, { passive: false });
    sv_.addEventListener("dblclick", (ev) => { const [x, y] = this.pt(ev); this.zoomA(1.8, x, y); });
    sv_.addEventListener("pointerdown", (ev) => { punt.set(ev.pointerId, ev); mosso = false; ultimo = ev; if (punt.size === 2) { const [a, b] = [...punt.values()]; dist0 = Math.hypot(a.clientX - b.clientX, a.clientY - b.clientY); } });
    sv_.addEventListener("pointermove", (ev) => {
      const p = ev.target.closest && ev.target.closest("path.com");
      if (!punt.size) {
        if (p) { const c = this.comuni.find((x) => x.c === p.dataset.c); Tip.mostra(this.opz.tip(c), ev); } else Tip.nascondi();
        return;
      }
      if (!punt.has(ev.pointerId)) return;
      punt.set(ev.pointerId, ev);
      if (punt.size === 2) {
        const [a, b] = [...punt.values()];
        const d = Math.hypot(a.clientX - b.clientX, a.clientY - b.clientY);
        if (dist0) { const m = { clientX: (a.clientX + b.clientX) / 2, clientY: (a.clientY + b.clientY) / 2 }; const [x, y] = this.pt(m); this.zoomA(d / dist0, x, y); }
        dist0 = d; mosso = true; return;
      }
      const dx = ev.clientX - ultimo.clientX, dy = ev.clientY - ultimo.clientY;
      if (Math.abs(dx) + Math.abs(dy) > 3) mosso = true;
      if (mosso) {
        sv_.classList.add("trascina"); Tip.nascondi();
        const r = sv_.getBoundingClientRect();
        this.vb.x -= (dx / r.width) * this.vb.w; this.vb.y -= (dy / r.height) * this.vb.h; this.limita(); this.applica();
        if (!sv_.hasPointerCapture(ev.pointerId)) sv_.setPointerCapture(ev.pointerId);
      }
      ultimo = ev;
    });
    const fine = (ev) => {
      if (!mosso && punt.size === 1 && ev.type === "pointerup") {
        const p = document.elementFromPoint(ev.clientX, ev.clientY);
        const pc = p && p.closest && p.closest("path.com");
        this.opz.click(pc ? pc.dataset.c : null);
      }
      punt.delete(ev.pointerId); if (punt.size < 2) dist0 = null;
      sv_.classList.remove("trascina");
    };
    sv_.addEventListener("pointerup", fine);
    sv_.addEventListener("pointercancel", fine);
    sv_.addEventListener("pointerleave", () => { if (!punt.size) Tip.nascondi(); });
    sv_.addEventListener("keydown", (ev) => {
      const p = ev.target.closest && ev.target.closest("path.com");
      if (p && (ev.key === "Enter" || ev.key === " ")) { ev.preventDefault(); this.opz.click(p.dataset.c); }
    });
    sv_.addEventListener("focusin", (ev) => {
      const p = ev.target.closest && ev.target.closest("path.com");
      if (p) { const c = this.comuni.find((x) => x.c === p.dataset.c); const r = p.getBoundingClientRect(); Tip.mostra(this.opz.tip(c), { clientX: r.right, clientY: r.top }); }
    });
    sv_.addEventListener("focusout", () => Tip.nascondi());
  }
  /* colori: funzione codice -> colore; filtro: Set dei codici visibili; bolle: codice -> numero */
  disegna({ colore, filtro, bolle, sel }) {
    for (const c in this.paths) {
      const p = this.paths[c];
      p.style.fill = colore(c);
      p.classList.toggle("fuori", filtro ? !filtro.has(c) : false);
      p.classList.toggle("sel", sel === c);
    }
    if (sel && this.paths[sel]) this.paths[sel].parentNode.insertBefore(this.paths[sel], this.paths[sel].parentNode.querySelector("path.prov"));
    this.gb.innerHTML = "";
    if (bolle) {
      const max = Math.max(1, ...Object.values(bolle));
      const lista = this.comuni.filter((c) => bolle[c.c] > 0 && c.k && (!filtro || filtro.has(c.c))).sort((a, b) => bolle[b.c] - bolle[a.c]);
      for (const c of lista) {
        const [x, y] = this.pr(c.k);
        this.gb.appendChild(sv("circle", { cx: x.toFixed(1), cy: y.toFixed(1), r: (2.2 + 22 * Math.sqrt(bolle[c.c] / max)).toFixed(1), class: "bolla" }));
      }
      this.maxBolla = max;
    }
  }
}

/* scala di colori sequenziale o divergente */
function scala(breaks, divergente) {
  const seq = ["--s1", "--s2", "--s3", "--s4", "--s5", "--s6"].map(css);
  const div = ["--d1", "--d2", "--d3", "--d4", "--d5", "--d6"].map(css);
  const zero = css("--zero");
  if (divergente) {
    return (v) => {
      if (v == null || !isFinite(v)) return zero;
      let i = 0; while (i < breaks.length && v > breaks[i]) i++;
      return div[Math.min(i, 5)];
    };
  }
  const pal = breaks.length + 1 >= 6 ? seq : seq.slice(6 - (breaks.length + 1));
  return (v) => {
    if (v == null || !isFinite(v) || v <= 0) return zero;
    let i = 0; while (i < breaks.length && v > breaks[i]) i++;
    return pal[i];
  };
}
function legenda(box, breaks, colFn, fmt, opz = {}) {
  const mid = [];
  if (opz.divergente) {
    const b = breaks;
    const et = [`oltre ${fmt(b[0])}`, `${fmt(b[0])} / ${fmt(b[1])}`, `${fmt(b[1])} / 0`, `0 / +${fmt(b[3]).replace("-", "")}`, `+${fmt(b[3])} / +${fmt(b[4])}`, `oltre +${fmt(b[4])}`];
    const v = [b[0] - 1, (b[0] + b[1]) / 2, b[1] / 2, b[3] / 2, (b[3] + b[4]) / 2, b[4] + 1];
    for (let i = 0; i < 6; i++) mid.push(`<div><i style="background:${colFn(v[i])}"></i><span>${et[i]}</span></div>`);
  } else {
    const ed = [0, ...breaks];
    for (let i = 0; i < ed.length; i++) {
      const lo = ed[i], hi = ed[i + 1];
      const v = hi == null ? lo + 1 : (lo + hi) / 2 || hi / 2;
      const t = hi == null ? `oltre ${fmt(lo)}` : i === 0 ? `fino a ${fmt(hi)}` : `${fmt(lo)} – ${fmt(hi)}`;
      mid.push(`<div><i style="background:${colFn(v || 1e-9)}"></i><span>${t}</span></div>`);
    }
  }
  box.innerHTML = `<span class="sc">${mid.join("")}</span>` +
    (opz.divergente ? "" : `<span class="zero"><i></i>${opz.zero || "nessun contributo"}</span>`) +
    (opz.bolle ? `<span class="bol"><i></i>cerchio = ${opz.bolle}</span>` : "");
}

/* ---------------- grafici SVG ---------------- */
function barreOrizzontali(box, voci, opz = {}) {
  box.innerHTML = "";
  if (!voci.length) { box.innerHTML = '<p class="vuoto">Nessun dato con i filtri scelti.</p>'; return; }
  const W = Math.max(320, Math.round(box.clientWidth || 560)), rh = 26, lw = opz.lw || 190, vw = 96, H = voci.length * rh + 6;
  const max = Math.max(...voci.map((v) => Math.abs(v.v)), 1e-9);
  const s = sv("svg", { viewBox: `0 0 ${W} ${H}`, role: "img", "aria-label": opz.etichetta || "grafico a barre" });
  voci.forEach((v, i) => {
    const y = i * rh + 3, bw = Math.max(1.5, ((W - lw - vw - 8) * Math.abs(v.v)) / max);
    const g = sv("g", { class: "bar" + (v.attivo ? " attivo" : ""), tabindex: opz.click ? "0" : "-1" });
    const t = sv("text", { x: lw - 8, y: y + rh / 2 + 4, "text-anchor": "end" });
    t.textContent = v.l.length > 30 ? v.l.slice(0, 29) + "…" : v.l;
    const r = sv("rect", { x: lw, y: y + 3, width: bw.toFixed(1), height: rh - 8, rx: 3, fill: v.col || css("--accent") });
    if (v.attivo) { r.setAttribute("stroke", css("--focus")); r.setAttribute("stroke-width", "2.5"); }
    const tv = sv("text", { x: lw + bw + 6, y: y + rh / 2 + 4, class: "forte" });
    tv.textContent = opz.fmt ? opz.fmt(v.v) : v.v;
    const ti = sv("title"); ti.textContent = `${v.l}: ${opz.fmt ? opz.fmt(v.v) : v.v}${v.extra ? ", " + v.extra : ""}`;
    g.append(ti, t, r, tv);
    if (opz.click) { g.addEventListener("click", () => opz.click(v)); g.addEventListener("keydown", (e) => { if (e.key === "Enter") opz.click(v); }); }
    s.appendChild(g);
  });
  box.appendChild(s);
}
function colonne(box, cat, serie, opz = {}) {
  box.innerHTML = "";
  const W = Math.max(320, Math.round(box.clientWidth || 620)), ml = 62, mt = 22;
  // etichette su due righe quando non entrano nella colonna
  const cwStima = (W - ml) / cat.length;
  const righe = cat.map((c) => {
    if (c.length * 6.6 <= cwStima - 6) return [c];
    const sp = [...c.matchAll(/ /g)].map((m) => m.index);
    if (!sp.length) return [c];
    const k = sp.reduce((a, b) => (Math.abs(b - c.length / 2) < Math.abs(a - c.length / 2) ? b : a));
    return [c.slice(0, k), c.slice(k + 1)];
  });
  const nr = Math.max(...righe.map((r) => r.length));
  const mb = 20 + 14 * nr + (opz.sotto ? 14 : 0), H = (opz.h || 250) + (mb - 34);
  const max = Math.max(1e-9, ...serie.flatMap((s) => s.v));
  const step = niceStep(max / 4), top = Math.ceil(max / step) * step;
  const s = sv("svg", { viewBox: `0 0 ${W} ${H}`, role: "img", "aria-label": opz.etichetta || "grafico a colonne" });
  for (let t = 0; t <= top + 1e-9; t += step) {
    const y = mt + (H - mt - mb) * (1 - t / top);
    s.appendChild(sv("line", { x1: ml, x2: W, y1: y, y2: y, class: "asse" }));
    const tx = sv("text", { x: ml - 6, y: y + 4, "text-anchor": "end" }); tx.textContent = opz.fmtAsse ? opz.fmtAsse(t) : F.num(t); s.appendChild(tx);
  }
  const cw = (W - ml) / cat.length, gap = Math.min(10, cw * 0.18), bw = (cw - gap * 2) / serie.length;
  cat.forEach((c, i) => {
    serie.forEach((se, j) => {
      const v = se.v[i] || 0, h = ((H - mt - mb) * v) / top;
      const x = ml + i * cw + gap + j * bw, y = H - mb - h;
      const g = sv("g", { class: "bar", tabindex: opz.click ? "0" : "-1" });
      const r = sv("rect", { x: x + 1, y, width: Math.max(1, bw - 2), height: Math.max(0, h), rx: 2, fill: se.col });
      if (opz.attivo != null && opz.attivo === i) { r.setAttribute("stroke", css("--focus")); r.setAttribute("stroke-width", "2.5"); }
      const ti = sv("title"); ti.textContent = `${c}${se.n ? ", " + se.n : ""}: ${opz.fmt ? opz.fmt(v) : v}${se.extra ? ", " + se.extra[i] : ""}`;
      g.append(ti, r);
      if (opz.valori && (serie.length === 1 || bw > 34) && v > 0) {
        const tv = sv("text", { x: x + bw / 2, y: y - 5, "text-anchor": "middle", class: "forte" });
        tv.style.fontSize = serie.length > 1 ? "10.5px" : "11.5px";
        tv.textContent = opz.fmtBreve ? opz.fmtBreve(v) : v; g.appendChild(tv);
      }
      if (opz.click) { g.addEventListener("click", () => opz.click(i)); g.addEventListener("keydown", (e) => { if (e.key === "Enter") opz.click(i); }); }
      s.appendChild(g);
    });
    righe[i].forEach((r, j) => { const tc = sv("text", { x: ml + i * cw + cw / 2, y: H - mb + 16 + j * 14, "text-anchor": "middle" }); tc.textContent = r; s.appendChild(tc); });
    if (opz.sotto) { const t2 = sv("text", { x: ml + i * cw + cw / 2, y: H - mb + 16 + nr * 14 + 1, "text-anchor": "middle" }); t2.style.fontSize = "10.5px"; t2.textContent = opz.sotto[i]; s.appendChild(t2); }
  });
  s.appendChild(sv("line", { x1: ml, x2: W, y1: H - mb, y2: H - mb, class: "asse" }));
  box.appendChild(s);
}
function niceStep(x) {
  if (x <= 0) return 1;
  const p = Math.pow(10, Math.floor(Math.log10(x))), m = x / p;
  return (m <= 1 ? 1 : m <= 2 ? 2 : m <= 2.5 ? 2.5 : m <= 5 ? 5 : 10) * p;
}

/* ---------------- tabella ordinabile ---------------- */
function intestazioni(thead, colonne, stato, ridisegna) {
  thead.innerHTML = "<tr>" + colonne.map((c) => `<th scope="col" class="${c.n ? "n" : ""}" data-k="${c.k}" tabindex="0" ${stato.k === c.k ? `aria-sort="${stato.d > 0 ? "ascending" : "descending"}"` : ""}>${c.t}</th>`).join("") + "</tr>";
  thead.querySelectorAll("th").forEach((th) => {
    const f = () => { const k = th.dataset.k; if (stato.k === k) stato.d = -stato.d; else { stato.k = k; stato.d = colonne.find((c) => c.k === k).n ? -1 : 1; } ridisegna(); };
    th.onclick = f; th.onkeydown = (e) => { if (e.key === "Enter") f(); };
  });
}
function ordina(righe, stato, val) {
  return righe.sort((a, b) => {
    const x = val(a, stato.k), y = val(b, stato.k);
    if (x == null && y == null) return 0; if (x == null) return 1; if (y == null) return -1;
    return (typeof x === "string" ? x.localeCompare(y, "it") : x - y) * stato.d;
  });
}
function scaricaCSV(nome, righe) {
  const testo = "﻿" + righe.map((r) => r.map((v) => {
    if (v == null) return "";
    if (typeof v === "number") return String(v).replace(".", ",");
    const s = String(v); return /[";\n]/.test(s) ? '"' + s.replace(/"/g, '""') + '"' : s;
  }).join(";")).join("\r\n");
  const b = new Blob([testo], { type: "text/csv;charset=utf-8" });
  const a = el("a", { href: URL.createObjectURL(b), download: nome });
  document.body.appendChild(a); a.click(); setTimeout(() => { URL.revokeObjectURL(a.href); a.remove(); }, 500);
}
function ridisegnaAlRidimensionamento(fn) {
  let t; addEventListener("resize", () => { clearTimeout(t); t = setTimeout(fn, 200); });
  if (window.matchMedia) matchMedia("(prefers-color-scheme: dark)").addEventListener?.("change", fn);
  new MutationObserver(fn).observe(document.documentElement, { attributes: true, attributeFilter: ["data-theme"] });
}

/* sul telefono i filtri stanno chiusi sotto un pulsante, così i dati si vedono subito */
function filtriRichiudibili() {
  document.querySelectorAll(".filtri").forEach((f) => {
    if (f.previousElementSibling && f.previousElementSibling.classList.contains("apri-filtri")) return;
    const b = el("button", { type: "button", class: "pulsante apri-filtri", "aria-expanded": "false" }, "Mostra i filtri");
    if (f.id) b.setAttribute("aria-controls", f.id);
    b.addEventListener("click", () => { const ap = f.classList.toggle("aperti"); b.setAttribute("aria-expanded", String(ap)); b.textContent = ap ? "Nascondi i filtri" : "Mostra i filtri"; });
    f.parentNode.insertBefore(b, f);
  });
}
