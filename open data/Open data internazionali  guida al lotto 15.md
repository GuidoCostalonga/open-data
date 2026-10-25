# Open data internazionali: guida al lotto 15

Il lotto 15 aggiunge **2.855.835 osservazioni**, 72.155 identità di serie e 248 Excel dati. La raccolta cumulativa dei lotti 1–15 raggiunge 24.457.035 osservazioni, 2.252.484 identità e 3.725 Excel dati; l'acquisizione integrale degli otto portali rimane incompleta.

## Contenuto e copertura

| Codice FAOSTAT | Risorsa | Osservazioni | Identità | Annualità effettive |
|---|---|---:|---:|---|
| EMN | Letame degli allevamenti | 2.555.034 | 45.182 | 1961–2023 |
| GFDI | Quote di valore per industrie e fattori primari della filiera alimentare | 161.088 | 20.994 | 2005–2021 |
| PA | Archivio storico dei prezzi alla produzione | 139.713 | 5.979 | 1966–1990 |

Sono state incluse tutte le annualità presenti nei tre CSV acquisiti, senza soglie temporali. Numeri originali in testo, valori numerici, unità, codici, dimensioni, flag, note e provenienza sono conservati; non sono applicate conversioni di unità o valuta né stime proprie.

Le osservazioni numeriche del lotto sono 2.852.955; le altre 2.880 righe restano presenti con il valore originale mancante o non numerico, senza trasformarlo in zero. PA è un archivio storico cessato: le sue valute e codifiche non sono armonizzate ai prezzi correnti.

Il catalogo FAOSTAT elenca 69 risorse, delle quali 44 ora acquisite e 25 residue. Gli altri sette portali mantengono i dati dei lotti precedenti e non sono stati riverificati nel lotto 15.

## Organizzazione dei file

- **Indice del lotto 15**: elenco di tutti gli Excel, righe, annualità, dimensioni in byte e SHA256; prima parte del registro cumulativo e riferimenti a tutte le altre parti.
- **Archivi dati**: 210 Excel per paesi e territori originali e 38 Excel per aggregati statistici, in 11 ZIP distinti. Gli aggregati non sono qualificati come regioni amministrative.
- **Dizionari FAOSTAT**: tutti i CSV ausiliari delle tre fonti, conservati nei relativi fogli senza tradurre o ricodificare i contenuti.
- **Stato complessivo 1–15**: riepilogo cumulativo per lotto e portale, catalogo FAOSTAT e continuità del registro.
- **Manifest e verifica**: conteggi, hash, recupero del registro precedente, catalogo acquisito, dettagli del controllo e candidati forestali rinviati.

Ogni Excel mantiene lo schema precedente: colonna A di margine, titolo alla riga 2, intestazioni alla riga 3, dati dalla riga 4. I fogli DATI riportano le 16 colonne comuni più tutti i campi originali non già rappresentati; la colonna del numero originale in testo protegge la precisione della fonte.

Ogni XLSX e ZIP consegnato è strettamente inferiore a **29.000.000 byte**. L'Excel più grande del lotto misura 8.948.294 byte e lo ZIP dati più grande 20.006.203 byte; anche il pacchetto di verifica rispetta lo stesso limite.

## Recupero e continuità del registro

Prima delle nuove acquisizioni sono state ricostruite e lette tutte le 22 parti del registro del lotto 14: 2.180.329 identità, 21.601.200 osservazioni. Gli allegati pubblicati sono stati recuperati e confrontati con hash, dimensioni e CRC, senza assumere attendibile il vecchio database di lavoro; i 325 Excel dati del lotto 14 sono stati verificati, mentre per i precedenti 3.152 Excel resta esplicitamente ereditata la verifica storica documentata.

Il registro cumulativo arriva ora a **23 parti**. Occorre conservare insieme:

- **Parte 1**: foglio REGISTRO_SERIE dell'indice del lotto 15, copiato invariato dall'indice precedente.
- **Parti 2–21**: file storici immutati nei sette ZIP di continuità consegnati con il lotto 14.
- **Parte 22**: file separato del lotto 14, immutato.
- **Parte 23**: nuova appendice del lotto 15 con 72.155 identità.

Le nuove identità non intersecano le 2.180.329 precedenti e non vi sono ripetizioni serie-periodo. È stato inoltre eseguito un confronto esatto di dimensioni codificate e unità fra dataset FAOSTAT; il controllo non equivale a un'armonizzazione semantica tra sistemi di codici differenti.

## Eccezioni documentate e controlli finali

La risorsa FO, Forestry Production and Trade, è stata scaricata per ispezione ma **non inclusa né conteggiata**. Il confronto ha individuato 794 identità con dimensioni codificate e unità identiche a serie FOP già consegnate: sono candidati da verificare, non duplicati accertati; l'intero dataset FO è rinviato finché non siano confrontati contenuti, periodi, valori e provenienza.

Per EMN il catalogo dichiara 2.606.359 righe, mentre il CSV acquisito ne contiene 2.555.034: scostamento di 51.325 righe. Sono conservate tutte le righe effettive del CSV, senza inventare quelle mancanti o presentare il conteggio del catalogo come dati acquisiti; GFDI e PA coincidono invece con i conteggi del catalogo.

Il controllo finale rilegge ogni cella dei fogli DATI nei 248 Excel dati e la confronta con la struttura acquisita: testo originale esatto, valori numerici verificati con tolleranza relativa e assoluta di 1e-14, dizionari riletti integralmente, appendice del registro confrontata riga per riga. Sono verificati anche SHA256, CRC, conteggi e limiti dimensionali degli archivi; l'esito del lotto è PASS.

## Fonti originali

Il catalogo di riferimento è il [catalogo bulk FAOSTAT](https://bulks-faostat.fao.org/production/datasets_E.json), acquisito il 25 ottobre 2026. Le tre risorse incluse provengono dai seguenti archivi ufficiali e mantengono nei file i nomi e gli aggiornamenti della fonte:

- **EMN**: [Environment Livestock Manure, archivio normalizzato completo](https://bulks-faostat.fao.org/production/Environment_LivestockManure_E_All_Data_(Normalized).zip).
- **GFDI**: [Value shares industry primary factors, archivio normalizzato completo](https://bulks-faostat.fao.org/production/Value_shares_industry_primary_factors_E_All_Data_(Normalized).zip).
- **PA**: [Prices Archive, archivio normalizzato completo](https://bulks-faostat.fao.org/production/PricesArchive_E_All_Data_(Normalized).zip).
- **FO rinviato**: [Forestry, archivio ispezionato e non consegnato come nuovi dati](https://bulks-faostat.fao.org/production/Forestry_E_All_Data_(Normalized).zip).
