# Lotti completi su Google Drive

I 31 lotti di «Open data internazionali» (1.543 allegati originali, 18,1 GB) sono conservati integralmente nella cartella Google Drive
«Open data internazionali - Lotti 01-31» (identificativo `1MKzgg6XTKP04VaySMjPKpRwPOgAHXGXZ`), suddivisi per lotto con una cartella
«00 - Documentazione generale». Il file `Open data internazionali  indice completo dei lotti 1-31 su Drive.csv` elenca ogni allegato con
lotto, nome originale, dimensione in byte, SHA256, MD5, identificativo e collegamento Drive.

Questo repository contiene solo una parte degli archivi (i file `Lotto N ...zip` e `.xlsx` di questa cartella), più gli indici, le guide e le
ricevute SHA256: gli archivi completi superano i limiti di GitHub e restano su Drive. L'Atlante dei dati (`atlante/`) è generato leggendo
tutti gli archivi scaricati da Drive con `atlante/strumenti/estrai_lotti.py`, che ne verifica l'impronta SHA256 contro l'indice; i valori
estratti stanno in `atlante/dati/archivi/` in forma compressa, serie per serie. Le tre matrici bilaterali FAOSTAT (lotto 19 RFM, lotto 26 EA,
lotto 31 TM: tutti i 38 allegati del lotto 19, tutti i 218 del lotto 26 e i 290 archivi ZIP di dati dei 363 allegati del
lotto 31, in tutto 7,6 GB) sono state scaricate da Drive con `atlante/strumenti/scarica_lotti.py`, verificate per
dimensione e SHA256 e lette integralmente con `atlante/strumenti/estrai_partner.py`: i valori stanno in `atlante/dati/partner/`, un file
compresso per dichiarante o destinatario, e si consultano nella vista Partner dell'Atlante. Il lotto 31 è stato trattato a blocchi di 25
archivi per i limiti di disco; gli archivi scaricati non sono conservati nel repository.

Stato di acquisizione nell'Atlante: vedi `atlante/LEGGIMI.md` e la pagina «Fonti e metodo» del sito.
