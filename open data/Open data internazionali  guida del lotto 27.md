# Open data internazionali: guida al lotto 27

Il lotto acquisisce integralmente FAOSTAT TI, “Trade: Trade Indices”, dal [file ufficiale normalizzato](https://bulks-faostat.fao.org/production/Trade_Indices_E_All_Data_(Normalized).zip). Il registro prosegue dalla parte 84 senza modificare le 83 parti precedenti; identità per dataset e dimensioni originali non equivalgono a fenomeni semanticamente armonizzati.

## Contenuto e cumulativo

| Misura | Lotto 27 | Cumulativo lotti 1–27 |
|---|---:|---:|
| Righe / osservazioni in senso contabile | 10.406.391 | 86.628.065 |
| Identità di serie per dataset | 252.080 | 8.030.004 |
| Excel dati | 335 | 6886 |
| Valori numerici | 10.406.391 | 82.439.054 |

- **Copertura TI**: annualità 1961–2024, 266 aree originali, 0 righe non numeriche e 302.903 zeri effettivi conservati.
- **Flag**: E: 10.406.391. Il dizionario originale è consegnato; E, Estimated value, non viene automaticamente qualificato come dato osservato.
- **Confezionamento**: 85 ZIP dati, 3 appendici del registro (84–86) e sei allegati di supporto, per 94 allegati. I numeri degli ZIP non sono numeri di paesi.

## Recupero preventivo e controlli distinti

Prima di scaricare TI sono stati nuovamente recuperati e verificati tutti i 218 allegati del lotto 26, a partire da ricevuta e audit: byte e SHA256, CRC dei 198 ZIP dati e SHA256 dei 394 Excel interni. Tutti gli 11 campi delle 83 parti del registro sono stati riletti e confrontati con le impronte dei campi già pubblicate; sono state nuovamente verificate 7.777.924 identità uniche, 76.221.674 righe e 72.032.663 valori numerici.

Le celle DATI storiche non sono state integralmente rilette nel lotto 27. La QA contenutistica storica è esplicitamente ereditata; i nuovi controlli riguardano integrità, manifest, registro e modello recuperati, mentre tutti i dati TI prodotti sono nuovamente riletti cella per cella dagli Excel realmente contenuti negli ZIP.

## Fedeltà alla fonte

Si conservano valore numerico e testo originale, unità anche vuote, tutti i codici ed etichette, flag e provenienza. Tutte le 13 colonne originali sono rappresentate nelle 16 colonne comuni e nelle sette colonne originali aggiuntive, senza conversioni, saldi o aggregazioni aggiuntive.

La base degli indici rimane nell’Element originale: non viene inventata un’unità quando Unit è vuota. Importazioni ed esportazioni restano distinte per Element Code ed Element; non esistono partner da inventare in questo schema.

Le classificazioni territoriali sono ereditate solo in caso di corrispondenza esatta di codice originale e nome con il manifest24 nuovamente recuperato nella catena degli audit. Aggregati statistici e paesi restano distinti; gli altri casi sono esplicitamente non classificati, senza inferire regioni amministrative.

## Identità e continuità

La chiave canonica comprende tutti i campi Code tranne Year Code, più Unit; l’identità è SHA256 di FAOSTAT|TI|JSON canonico. Il confronto ha usato tutte le 7.777.924 identità e chiavi dimensionali storiche recuperate: zero intersezioni di identità, zero candidati di chiave dimensionale completa e zero ripetizioni serie-periodo.

Questo non dimostra equivalenza o distinzione semantica fra schemi diversi. Nessuna riga viene eliminata sulla base di una sola corrispondenza di codici; eventuali confronti futuri devono considerare anche periodi, valori, flag e provenienza.

La parte 1 è nel foglio REGISTRO_SERIE dell’indice27, copiato byte per byte dall’indice26. Le parti 2–83 restano i file originali pubblicati e invariati; le nuove appendici sono le parti 84–86. L’indice elenca tutti i puntamenti; l’audit contiene l’intero piano di recupero e gli identificativi effettivi.

## Catalogo e risorse residue

Il nuovo confronto diretto del [catalogo ufficiale FAOSTAT](https://bulks-faostat.fao.org/production/datasets_E.json) lo trova byte-identico al checkpoint del lotto 26. La continuità con il checkpoint del lotto 19 del 25 ottobre 2026 è ereditata dal confronto documentato nell’audit26 recuperato, non presentata come un nuovo confronto diretto con un file del lotto19. Mantiene 69 risorse; per TI indica 10.406.391 righe, rispetto a 10.406.391 righe effettive nel CSV, differenza 0.

La copertura FAOSTAT passa a 65 risorse acquisite su 69. Restano FBSH, SCL, TCL e TM; non sono esclusioni definitive e non sono conteggiate come acquisite.

I portali data.europa.eu, UNdata, World Bank, OECD, Eurostat, IMF e WHO/GHO non sono stati riverificati nel lotto 27. I relativi conteggi sono ereditati e nessun conteggio già consegnato viene alterato retroattivamente.

## Formato e audit

Ogni Excel e ZIP è strettamente inferiore a 29.000.000 byte. Restano margine A, titolo alla riga 2, intestazioni alla riga 3, dati dalla riga 4, blocco D4, griglia nascosta e stili del modello pubblicato.

L’audit comprende manifest, SHA256, controlli del recupero preventivo, confronto con il catalogo, digest dei 13 campi originali, controlli fonte/staging, confronto di tutte le celle nuove, dizionari, registro, formule e codice riproducibile. Le anteprime sono ricostruzioni PIL di viewport campionati da celle e stili nativi, non schermate Office né una rilettura visiva integrale.

Lo ZIP ufficiale TI è escluso dall’audit perché da solo supera il limite degli allegati; URL, dimensione e SHA256 sono documentati. I dati contenuti sono integralmente distribuiti negli Excel dei ZIP consegnati.

La ricevuta SHA256 elenca tutti gli allegati eccetto sé stessa, inclusa l’impronta dell’audit. La propria impronta è verificata separatamente dopo la pubblicazione, evitando un riferimento crittografico ricorsivo.
