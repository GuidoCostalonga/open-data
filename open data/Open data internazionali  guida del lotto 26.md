# Open data internazionali: guida al lotto 26

Il lotto 26 acquisisce integralmente lo ZIP ufficiale FAOSTAT EA, “Investment: Development Flows to Agriculture”, dopo il recupero preventivo dei 54 allegati pubblicati del lotto 25 e la rilettura delle 69 parti del registro cumulativo. Il contenuto effettivo dello ZIP è distinto dai metadati del catalogo; non sono modificati retroattivamente dati o conteggi dei lotti precedenti ([FAOSTAT, file acquisito](https://bulks-faostat.fao.org/production/Development_Assistance_to_Agriculture_E_All_Data_(Normalized).zip)).

## Dati e confezionamento

- **Contenuto**: 13.020.275 righe, tutte con valore numerico, e 1.362.214 nuove identità di serie specifiche del dataset; annualità 1973–2023.
- **Entità originali**: 149 donatori e 231 tuple di destinatario; i donatori comprendono anche organizzazioni e non sono automaticamente paesi.
- **Excel dati**: 394 file in 198 ZIP: 110 archivi per paesi e territori, 61 per aggregati statistici e 27 per destinatari non classificati. Il numero degli archivi non è il numero dei paesi.
- **Registro**: nuove appendici 70–83, con 100.000 identità ciascuna nelle parti 70–82 e 62.214 nella parte 83. Parti 2–69 immutate; XML della parte 1 copiato byte per byte dal nuovo recupero dell’indice 25.
- **Consegna**: 218 allegati previsti: 198 ZIP dati, 14 appendici e 6 file di supporto, inclusa questa guida, indice, stato, dizionari, audit e ricevuta SHA256. La pubblicazione effettiva è documentata separatamente dalla generazione locale.

Questi conteggi descrivono le righe effettivamente lette nel file ufficiale, non un riempimento dei metadati attesi. Tutti i donatori rimangono presenti negli Excel dei rispettivi destinatari, nell’ordine relativo originale, senza aggregazioni aggiuntive ([FAOSTAT EA](https://bulks-faostat.fao.org/production/Development_Assistance_to_Agriculture_E_All_Data_(Normalized).zip)).

## Cumulativo dopo il lotto 26

| Misura | Lotti 1–25 | Lotto 26 | Lotti 1–26 |
|---|---:|---:|---:|
| Osservazioni/righe fonte | 63.201.399 | 13.020.275 | 76.221.674 |
| Identità di serie per dataset | 6.415.710 | 1.362.214 | 7.777.924 |
| Excel dati | 6.157 | 394 | 6.551 |
| Valori numerici | 59.012.388 | 13.020.275 | 72.032.663 |

FAOSTAT passa da 63 a 64 risorse acquisite su 69. Restano FBSH, SCL, TCL, TI e TM; le coperture degli altri sette portali, data.europa.eu, UNdata, World Bank, OECD, Eurostat, IMF e WHO/GHO, sono ereditate e non sono state riverificate in questo lotto.

## Scostamento del catalogo e della fonte

Il catalogo corrente è stato confrontato con i checkpoint 19 e 25: 69 risorse e contenuto byte-identico; un ulteriore download senza cache ha restituito lo stesso SHA256. Il catalogo indica per EA 13.869.395 righe e, nella descrizione Topic, 189 donatori e 208 destinatari, mentre il CSV ufficiale effettivo contiene 13.020.275 righe, 149 donatori e 231 destinatari: differenza righe −849.120 ([catalogo ufficiale FAOSTAT](https://bulks-faostat.fao.org/production/datasets_E.json)).

Un secondo download indipendente dello ZIP, con risposta CloudFront “Miss”, ha confermato byte e SHA256 identici al primo. Si consegna il contenuto effettivamente disponibile, senza inventare righe per raggiungere il catalogo; la data di aggiornamento del dataset resta 2025-07-24T00:00:00, distinta dai timestamp tecnici HTTP ([file ufficiale EA](https://bulks-faostat.fao.org/production/Development_Assistance_to_Agriculture_E_All_Data_(Normalized).zip)).

Una lettura binaria indipendente del CSV ha contato 13.020.276 righe fisiche, esattamente un’intestazione più le 13.020.275 osservazioni lette dal parser. Sono registrati anche lo SHA256 del CSV non compresso e la dimensione di 2.542.793.099 byte, senza confondere il conteggio delle righe fisiche con quello delle osservazioni ([CSV nello ZIP EA](https://bulks-faostat.fao.org/production/Development_Assistance_to_Agriculture_E_All_Data_(Normalized).zip)).

## Fedeltà e formato

- **Campi**: le 16 colonne comuni restano in B:Q, seguite da 15 campi originali non già rappresentati. Tutti i 18 campi originali sono conservati, inclusi entrambi i ruoli e i relativi codici e nomi; le colonne comuni geografiche rappresentano il destinatario.
- **Valori**: sono mantenuti il numero e il testo numerico originale; 2.767.074 zeri effettivi restano zeri. Non vi sono righe a valore non numerico; nessun valore mancante è stato imputato.
- **Unità**: million USD, percentuali e 14.756 unità vuote restano come nella fonte. Un’unità vuota non rende mancante un valore numerico e non viene inventata né convertita.
- **Flag**: X in 11.958.575 righe significa “Figure from external organization”; E in 1.061.700 righe significa “Estimated value”. Le stime non diventano dati osservati.
- **Codici**: gli apostrofi letterali nei codici originali, compresi valori non geografici come 'F1033, restano preservati. Non sono interpretati come classificazioni amministrative.
- **Classificazioni**: soltanto corrispondenze esatte codice e nome con il manifest 24, recuperato nell’audit 25, riusano classificazioni esplicitamente ereditate. Gli altri destinatari restano non classificati; SSA/420 mantiene la correzione a aggregato statistico.
- **Layout**: margine A, titolo riga 2, intestazioni riga 3, dati dalla riga 4, blocco D4 e griglia nascosta; banca stili originale invariata. Eventuali troncamenti visivi dovuti a larghezze e altezze ereditate non eliminano il contenuto completo delle celle.
- **Limite**: ogni Excel e ZIP consegnato è strettamente inferiore a 29.000.000 byte.

Unità, flag e dizionari derivano dai file originali del medesimo ZIP. ItemCodes contiene soltanto le intestazioni, senza righe, ed è consegnato così, senza inventare un dizionario: codici e nomi presenti nei dati restano comunque conservati ([FAOSTAT EA](https://bulks-faostat.fao.org/production/Development_Assistance_to_Agriculture_E_All_Data_(Normalized).zip)).

## Controlli nuovi e controlli ereditati

Il recupero preventivo ha verificato tutti i 54 allegati 25 per byte e SHA256, i CRC dei 26 ZIP dati, gli hash dei 59 Excel interni e 52 CRC complessivi di archivi/workbook. Sono stati riletti gli 11 campi di tutte le 69 parti del registro, ricostruiti gli identificativi e verificata l’unicità globale: 6.415.710 identità, 63.201.399 righe e 59.012.388 valori numerici.

Le celle DATI storiche non sono state nuovamente rilette integralmente: il loro controllo contenutistico resta ereditato dagli audit precedenti. Per le parti 2–21 sono nuovamente verificate le copie originali e i relativi hash; il CRC dei sette ZIP di continuità 14 resta ereditato, non è presentato come nuovo controllo.

La nuova fonte EA è stata letta integralmente in due passaggi con confronto del digest dei 18 campi originali. Tutte le 31 celle dati per riga sono state rilette dagli Excel effettivamente contenuti nei ZIP, confrontate con lo staging, insieme a tutte le celle dei metadati; sono verificati CRC, hash, banca stili, stile di ogni cella serializzata e layout dei fogli.

Le 1.362.214 nuove identità sono state confrontate con tutte le 6.415.710 identità storiche senza intersezioni, e non esistono ripetizioni identità-periodo. Lo schema completo EA è assente dai 38 schemi dimensionali storici, quindi non risultano candidati con la medesima chiave dimensionale completa; questo non costituisce un’armonizzazione semantica fra schemi differenti.

Le nuove appendici sono rilette integralmente e confrontate con il registro EA di staging. Dizionari, indice, riepiloghi e formule dello stato cumulativo sono verificati; i valori delle formule sono ricalcolati e nessun errore Excel è ammesso, mantenendo inalterate le righe storiche dei lotti e degli altri sette portali.

Le anteprime sono viewport limitati ricostruiti dalle celle e dimensioni native, non schermate di Excel/LibreOffice né un’ispezione visiva integrale. L’audit conserva l’ambito preciso dei controlli, il codice di lavoro e le prove di recupero; lo ZIP fonte da 124.703.688 byte è identificato da URL, dimensione e SHA256, ma non è incluso nell’audit per rispettare il limite degli allegati.

## Ripresa successiva

Prima del lotto 27 recuperare tutti i 218 allegati effettivamente pubblicati, verificare manifest e ricevuta e ricostruire le 83 parti del registro cumulativo. La prossima nuova appendice è la parte 84; le cinque risorse residue non sono escluse definitivamente né acquisite soltanto perché presenti nel catalogo.
