#!/usr/bin/env bash
# Prepara una variante grafica del sito senza toccare l'originale.
# Uso: strumenti/variante.sh <nome-variante> <cartella-uscita>
#   es. strumenti/variante.sh c /tmp/scocci-c
# La variante sostituisce assets/css/stile.css con varianti/<nome>/stile.css
# e, se presente, il collegamento ai caratteri con varianti/<nome>/caratteri.txt
set -euo pipefail
SITO="$(cd "$(dirname "$0")/.." && pwd)"
NOME="$1"; USCITA="$2"
rm -rf "$USCITA"; mkdir -p "$USCITA"
cp -r "$SITO"/*.html "$SITO/assets" "$USCITA"/
cp "$SITO/varianti/$NOME/stile.css" "$USCITA/assets/css/stile.css"
if [ -f "$SITO/varianti/$NOME/caratteri.txt" ]; then
  NUOVO="$(cat "$SITO/varianti/$NOME/caratteri.txt")"
  sed -i "s|https://fonts.googleapis.com/css2?[^\"]*|$NUOVO|" "$USCITA"/*.html
fi
echo "Variante $NOME pronta in $USCITA"
