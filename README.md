# Utopia Wiki Offline Scraper

Tool per scaricare offline il sito [Utopia Wiki](https://wiki.utopia-game.com/index.php?title=Welcome_to_the_Utopia_Wiki) e gestire le pagine scaricate.

## Requisiti

- Python 3.x
- `requests` (`pip3 install requests`)
- `beautifulsoup4` (`pip3 install beautifulsoup4`)

## Workflow consigliato

```bash
# 1. Download completo di tutte le pagine
python3 scraper.py

# 2. Classifica le pagine (keep/ignore)
python3 page_manager.py --classify

# 3. Rivedi la classificazione
python3 page_manager.py --review
python3 page_manager.py --list keep

# 4. Archivia le pagine ignorate
python3 page_manager.py --archive

# 5. Esporta tutto in un unico Markdown (per LLM grounding)
python3 page_manager.py --export-md

# 6. In futuro, aggiorna solo le pagine utili + Age Details
python3 scraper.py --update-keep
```

## scraper.py - Download delle pagine

### Download completo

```bash
python3 scraper.py
```

Il wiki viene salvato nella cartella `wiki_offline/`. Apri `wiki_offline/index.html` nel browser per consultarlo.

### Aggiornare solo le pagine keep + pagina speciale Age Details

```bash
python3 scraper.py --update-keep
```

Riscarica solo le pagine con status `keep` in `page_config.json` e la pagina speciale `age_details` dal sito principale.

### Controllare lo stato del download

```bash
python3 scraper.py --status
```

### Altre opzioni

| Opzione | Descrizione |
|---------|-------------|
| `--reset` | Ignora il progresso precedente e ricomincia da zero |
| `--no-images` | Non scaricare le immagini |
| `--retries N` | Numero massimo di retry per richiesta (default: 10) |
| `-d N` | Ritardo in secondi tra le richieste (default: 1.0) |
| `-o DIR` | Cartella di output personalizzata |

Il sito da spesso errori 502: lo script ritenta automaticamente con backoff esponenziale. Il progresso viene salvato, quindi basta rilanciare lo script per riprendere un download interrotto.

## page_manager.py - Gestione pagine

### Classificare le pagine

```bash
python3 page_manager.py --classify
```

Classifica automaticamente tutte le pagine in `keep` (regole/strategie) o `ignore` (duplicati, Age vecchie, alleanze, kingdoms, profili, IRC, ecc.). La classificazione viene salvata in `wiki_offline/page_config.json`.

Criteri automatici di ignore:
- **Pagine vuote/placeholder**: body corto, "TBD", "UNDER CONSTRUCTION"
- **Redirect**: pagine che reindirizzano ad altre
- **Duplicati**: pagine con contenuto identico (tiene la versione canonica)
- **Age specifiche**: Age_37..Age_112, Age_of_*, WoL_(Age_*) - eccetto l'age corrente
- **Alliance/Kingdom**: schede di alleanze e regni specifici
- **Profili giocatori**: pagine con "Player Information"
- **IRC**: pagine IRC (obsolete)
- **Tool esterni**: Firefox, UtopiaPimp, Metatron, ecc.
- **Meta**: Sandbox, Changelog, SpecialThanks, ecc.

### Rivedere la classificazione

```bash
python3 page_manager.py --review           # Riepilogo per categoria
python3 page_manager.py --list keep        # Lista pagine keep
python3 page_manager.py --list ignore      # Lista pagine ignore
python3 page_manager.py --list all         # Tutte
```

### Archiviare le pagine ignorate

```bash
python3 page_manager.py --archive
```

Sposta le pagine `ignore` da `pages/` a `archived/` e rigenera l'indice.

### Override manuale

```bash
python3 page_manager.py --set Spells keep
python3 page_manager.py --set Some_Page ignore
```

Gli override manuali vengono preservati nelle riclassificazioni successive.

### Ripristinare una pagina dall'archivio

```bash
python3 page_manager.py --restore Some_Page
```

### Cambiare l'age corrente

```bash
python3 page_manager.py --set-age 115
```

Aggiorna l'age nel config e riclassifica. Se esistono pagine per la nuova age (es. Age_115, Age_115_Mechanics), vengono classificate come `keep`.

### Esportare in Markdown (per LLM grounding)

```bash
python3 page_manager.py --export-md
```

Genera un unico file `wiki_offline/utopia_wiki.md` con tutte le pagine keep + speciali. Ideale per usarlo come contesto/grounding con un LLM, evitando di gestire decine di file separati.

Per salvare in un percorso custom:

```bash
python3 page_manager.py --export-md mio_file.md
```

Dopo un `--update-keep`, riesegui `--export-md` per rigenerare il file aggiornato.

## Pagine speciali

La pagina `https://utopia-game.com/wol/chooser/age_details/` contiene le informazioni chiave dell'age corrente. Viene scaricata automaticamente con `--update-keep` e salvata come `pages/_Age_Details_Current.html`.

Per aggiungere altre pagine speciali, modifica il campo `special_pages` in `wiki_offline/page_config.json`.

## Pagine keep (76 pagine + 1 speciale)

| # | Pagina | Contenuto |
|---|--------|-----------|
| | **_Age_Details_Current** | **[SPECIALE] Dettagli age corrente (dal sito principale)** |
| 1 | A_Players_Guide_to_Utopia | Guida generale per nuovi giocatori |
| 2 | Ages | Panoramica del sistema delle Age |
| 3 | Aggressive_Actions | Azioni aggressive e conseguenze |
| 4 | Aid | Sistema di aiuto tra province |
| 5 | Alliances | Indice e spiegazione delle alleanze |
| 6 | Ambush_Guide | Guida all'ambush |
| 7 | Ambushing | Meccaniche di ambush |
| 8 | Assassinate_wizards | Operazione thievery: assassinare maghi |
| 9 | Attacking_&_Calculating_an_Attack | Calcolo e meccaniche degli attacchi |
| 10 | Buildings | Edifici e costruzione |
| 11 | Bushels | Sistema dei bushels (cibo) |
| 12 | Chaining | Strategia di chaining degli attacchi |
| 13 | Creating_a_province | Come creare una provincia |
| 14 | Dark_Elves | Razza: Dark Elves |
| 15 | Dragons | Sistema dei draghi |
| 16 | Dragons,_Aid_&_Stances | Draghi, aiuti e stance |
| 17 | Dual_Monarch | Guida al Dual Monarch |
| 18 | Economy | Sistema economico |
| 19 | Ethics_of_Waving_and_War | Etica di wave e guerra |
| 20 | Exploration | Sistema di esplorazione |
| 21 | Explore_Pool | Pool di esplorazione |
| 22 | FAQ | Domande frequenti |
| 23 | Finding_Good_Learn_Targets | Come trovare buoni target per learn |
| 24 | Finding_Good_Plunder_Targets | Come trovare buoni target per plunder |
| 25 | Formulas | Indice delle formule di gioco |
| 26 | Fountain_of_knowledge | Spell: Fountain of Knowledge |
| 27 | Freeze_time | Meccanica del freeze time |
| 28 | Game_Rules | Regole ufficiali del gioco |
| 29 | Getting_Started_with_Utopia | Guida introduttiva |
| 30 | Guide | Guida strategica generale |
| 31 | Guide_Combo_Selection | Guida alla selezione combo razza/personalita |
| 32 | Guides | Indice delle guide |
| 33 | Island | Sistema delle isole |
| 34 | Kingdoms | Meccaniche dei kingdom |
| 35 | Land_Whorring_Tips_&_Tricks | Guida al land whoring |
| 36 | Leadership_Logic | Logica di leadership e gestione KD |
| 37 | Magic_Formulas | Formule magiche |
| 38 | Monarchy | Sistema della monarchia |
| 39 | Multi-Attack_Protection_(MAP) | Protezione multi-attacco |
| 40 | Mystics_Spell_Table | Tabella spell dei mystici |
| 41 | Networth | Calcolo del networth |
| 42 | Offensive_Military_Efficiency | Efficienza militare offensiva |
| 43 | Overpop_Mitigation | Mitigazione sovrappopolazione |
| 44 | Overpopulation | Meccanica di sovrappopolazione |
| 45 | Paper_Utopia | Il giornale del kingdom |
| 46 | Protection | Sistema di protezione |
| 47 | Province | Panoramica della provincia |
| 48 | Quick_Tips | Consigli rapidi |
| 49 | Races_and_Personalities | Razze e personalita |
| 50 | Recommended_Defense | Difesa consigliata |
| 51 | Relations | Sistema di relazioni tra kingdom |
| 52 | Relations_Meter | Contatore delle relazioni |
| 53 | Reservations | Sistema delle prenotazioni |
| 54 | Ritual | Meccanica dei rituali |
| 55 | Rules | Regole del gioco |
| 56 | Runes | Sistema delle rune |
| 57 | Science_Formulas | Formule scientifiche |
| 58 | Scientists | Sistema degli scienziati |
| 59 | Should_my_KD_Predetermine_a_Setup_ | Guida: predeterminare un setup di KD |
| 60 | SoM_translation | Traduzione Sword of Might |
| 61 | Spell_Uses | Utilizzi degli spell |
| 62 | Stances | Stance del kingdom |
| 63 | The_Plague | Meccanica della peste |
| 64 | Thievery_Formulas | Formule di thievery |
| 65 | Throne | Pagina del trono |
| 66 | Time_in_Utopia | Sistema del tempo in Utopia |
| 67 | Traditional_march | Tipo di attacco: Traditional March |
| 68 | Tutorials | Indice dei tutorial |
| 69 | Unique_Abilities | Abilita uniche delle razze |
| 70 | Utopia | Panoramica generale del gioco |
| 71 | Utopian_server | Info sui server di gioco |
| 72 | War_Score | Punteggio di guerra |
| 73 | Warleader_Guide_to_Attrition | Guida del warleader all'attrito |
| 74 | Wizards | Sistema dei maghi e unita |
| 75 | WoL_Personalities | Personalita su World of Legends |
| 76 | World_of_Legends | Info sul server WoL |

## Struttura output

```
wiki_offline/
  index.html                 # Indice con solo pagine keep + speciali
  page_config.json           # Configurazione (current_age, status pagine)
  scraper_progress.json      # Stato del download (per resume)
  css/
    style.css                # Stile per la consultazione offline
  pages/                     # Pagine keep (76 + 1 speciale)
    _Age_Details_Current.html
    Spells.html
    ...
  archived/                  # Pagine ignorate (~486 file)
  images/
```
