#!/usr/bin/env node
/* ==========================================================
   Pubblicazione protetta da parola chiave
   ----------------------------------------------------------
   Uso:
     PAROLA_CHIAVE='...' node strumenti/proteggi.mjs <cartella-sito> <cartella-uscita>

   Per ogni pagina HTML:
   1. inserisce dentro la pagina gli script locali (testi delle
      notizie e configurazione compresi), così nessun contenuto
      testuale resta leggibile in chiaro;
   2. cifra la pagina con AES-GCM a 256 bit; la chiave è ricavata
      dalla parola chiave con PBKDF2-SHA256 (600.000 iterazioni);
   3. scrive una pagina d'ingresso che chiede la parola chiave e
      decifra il contenuto nel browser.
   Fogli di stile e immagini sono copiati in chiaro.
   La parola chiave non viene mai scritta nei file prodotti.
   ========================================================== */
import { webcrypto as cripto } from "node:crypto";
import fs from "node:fs";
import path from "node:path";

const [origine, uscita] = process.argv.slice(2);
const parola = process.env.PAROLA_CHIAVE;
if (!origine || !uscita || !parola) {
  console.error("Uso: PAROLA_CHIAVE='...' node strumenti/proteggi.mjs <cartella-sito> <cartella-uscita>");
  process.exit(1);
}
const ITERAZIONI = 600000;
const b64 = (u8) => Buffer.from(u8).toString("base64");

const sale = cripto.getRandomValues(new Uint8Array(16));
const base = await cripto.subtle.importKey("raw", new TextEncoder().encode(parola), "PBKDF2", false, ["deriveKey"]);
const chiave = await cripto.subtle.deriveKey(
  { name: "PBKDF2", salt: sale, iterations: ITERAZIONI, hash: "SHA-256" },
  base, { name: "AES-GCM", length: 256 }, false, ["encrypt"]
);

fs.rmSync(uscita, { recursive: true, force: true });
fs.mkdirSync(uscita, { recursive: true });

// Copia fogli di stile e immagini (gli script finiscono dentro le pagine cifrate)
for (const sotto of ["assets/css", "assets/img"]) {
  fs.cpSync(path.join(origine, sotto), path.join(uscita, sotto), { recursive: true });
}

const ingresso = fs.readFileSync(new URL("./ingresso.html", import.meta.url), "utf8");
const pagine = fs.readdirSync(origine).filter((f) => f.endsWith(".html"));

for (const nome of pagine) {
  let html = fs.readFileSync(path.join(origine, nome), "utf8");
  html = html.replace(/<script src="(assets\/js\/[^"]+)"><\/script>/g, (_, src) => {
    const codice = fs.readFileSync(path.join(origine, src), "utf8").replace(/<\/script/gi, "<\\/script");
    return "<script>\n" + codice + "\n</script>";
  });
  if (/<script src="assets\//.test(html)) throw new Error("Script locale non incorporato in " + nome);

  const iv = cripto.getRandomValues(new Uint8Array(12));
  const cifrato = new Uint8Array(await cripto.subtle.encrypt({ name: "AES-GCM", iv }, chiave, new TextEncoder().encode(html)));
  const dati = JSON.stringify({ s: b64(sale), n: ITERAZIONI, iv: b64(iv), c: b64(cifrato) });
  fs.writeFileSync(path.join(uscita, nome), ingresso.replace("__DATI_CIFRATI__", dati));
  console.log("cifrata:", nome, (cifrato.length / 1024).toFixed(1) + " KB");
}
