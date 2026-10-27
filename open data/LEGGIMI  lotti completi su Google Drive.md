# Lotti completi su Google Drive

I 31 lotti di «Open data internazionali» (1.543 allegati originali, 18,1 GB) sono conservati integralmente nella cartella Google Drive
«Open data internazionali - Lotti 01-31» (identificativo `1MKzgg6XTKP04VaySMjPKpRwPOgAHXGXZ`), suddivisi per lotto con una cartella
«00 - Documentazione generale». Il file `Open data internazionali  indice completo dei lotti 1-31 su Drive.csv` elenca ogni allegato con
lotto, nome originale, dimensione in byte, SHA256, MD5, identificativo e collegamento Drive.

Questo repository contiene solo una parte degli archivi (i file `Lotto N ...zip` e `.xlsx` di questa cartella), più gli indici, le guide e le
ricevute SHA256: gli archivi completi superano i limiti di GitHub e restano su Drive. L'Atlante dei dati (`atlante/`) è generato leggendo
tutti gli archivi scaricati da Drive con `atlante/strumenti/estrai_lotti.py`, che ne verifica l'impronta SHA256 contro l'indice; i valori
estratti stanno in `atlante/dati/archivi/` in forma compressa, serie per serie.

Stato di acquisizione nell'Atlante: vedi `atlante/LEGGIMI.md` e la pagina «Fonti e metodo» del sito.
