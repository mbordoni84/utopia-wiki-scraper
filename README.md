# Utopia Wiki Offline Scraper

Tool to download the [Utopia Wiki](https://wiki.utopia-game.com/index.php?title=Welcome_to_the_Utopia_Wiki) for offline use and manage the downloaded pages.

## Requirements

- Python 3.x
- `requests` (`pip3 install requests`)
- `beautifulsoup4` (`pip3 install beautifulsoup4`)

## Recommended Workflow

```bash
# 1. Full download of all wiki pages
python3 scraper.py

# 2. Classify pages (keep/ignore)
python3 page_manager.py --classify

# 3. Review the classification
python3 page_manager.py --review
python3 page_manager.py --list keep

# 4. Archive ignored pages
python3 page_manager.py --archive

# 5. Export everything into a single Markdown file (for LLM grounding)
python3 page_manager.py --export-md

# 6. In the future, update only the useful pages + Age Details
python3 scraper.py --update-keep
```

## scraper.py - Page Download

### Full Download

```bash
python3 scraper.py
```

The wiki is saved to the `wiki_offline/` folder. Open `wiki_offline/index.html` in your browser to browse it.

### Update only keep pages + Age Details special page

```bash
python3 scraper.py --update-keep
```

Re-downloads only pages with `keep` status in `page_config.json` and the special `age_details` page from the main site.

### Check download status

```bash
python3 scraper.py --status
```

### Other options

| Option | Description |
|--------|-------------|
| `--reset` | Ignore previous progress and start from scratch |
| `--no-images` | Skip image downloads |
| `--retries N` | Max retries per request (default: 10) |
| `-d N` | Delay in seconds between requests (default: 1.0) |
| `-o DIR` | Custom output directory |

The site frequently returns 502 errors: the script automatically retries with exponential backoff. Progress is saved, so you can simply re-run the script to resume an interrupted download.

## page_manager.py - Page Management

### Classify pages

```bash
python3 page_manager.py --classify
```

Automatically classifies all pages as `keep` (rules/strategy) or `ignore` (duplicates, old Ages, alliances, kingdoms, profiles, IRC, etc.). The classification is saved to `wiki_offline/page_config.json`.

Automatic ignore criteria:
- **Empty/placeholder pages**: short body, "TBD", "UNDER CONSTRUCTION"
- **Redirects**: pages that redirect to others
- **Duplicates**: pages with identical content (keeps the canonical version)
- **Age-specific**: Age_37..Age_112, Age_of_*, WoL_(Age_*) - except the current age
- **Alliance/Kingdom**: specific alliance and kingdom pages
- **Player profiles**: pages with "Player Information"
- **IRC**: IRC pages (obsolete)
- **External tools**: Firefox, UtopiaPimp, Metatron, etc.
- **Meta**: Sandbox, Changelog, SpecialThanks, etc.

### Review the classification

```bash
python3 page_manager.py --review           # Summary by category
python3 page_manager.py --list keep        # List keep pages
python3 page_manager.py --list ignore      # List ignored pages
python3 page_manager.py --list all         # List all
```

### Archive ignored pages

```bash
python3 page_manager.py --archive
```

Moves `ignore` pages from `pages/` to `archived/` and regenerates the index.

### Manual override

```bash
python3 page_manager.py --set Spells keep
python3 page_manager.py --set Some_Page ignore
```

Manual overrides are preserved across reclassifications.

### Restore a page from the archive

```bash
python3 page_manager.py --restore Some_Page
```

### Change the current age

```bash
python3 page_manager.py --set-age 115
```

Updates the age in the config and reclassifies. If pages exist for the new age (e.g. Age_115, Age_115_Mechanics), they are classified as `keep`.

### Export to Markdown (for LLM grounding)

```bash
python3 page_manager.py --export-md
```

Generates a single file `wiki_offline/utopia_wiki.md` structured in 3 parts:

1. **Part 1: Manual Notes (Authoritative)** — contents of `wiki_offline/manual_notes.md`. These override any conflicting information from the other parts.
2. **Part 2: Age Details — Races & Personalities** — the special page with current age race/personality data.
3. **Part 3: Wiki Pages** — all keep pages from the wiki.

The export will prompt you to confirm the current age before proceeding. The special page URL is printed with a warning to verify it hasn't changed between ages.

To save to a custom path:

```bash
python3 page_manager.py --export-md my_file.md
```

After running `--update-keep`, re-run `--export-md` to regenerate the updated file.

### Manual Notes

Create `wiki_offline/manual_notes.md` to add authoritative notes that override wiki content. This file is included as Part 1 in the exported markdown.

## Special Pages

The page `https://utopia-game.com/wol/chooser/age_details/` contains key information about the current age. It is automatically downloaded with `--update-keep` and saved as `pages/_Age_Details_Current.html`.

To add more special pages, edit the `special_pages` field in `wiki_offline/page_config.json`.

## Keep Pages (75 pages + 1 special)

| # | Page | Description |
|---|------|-------------|
| | **_Age_Details_Current** | **[SPECIAL] Current age details (from the main site)** |
| 1 | A_Players_Guide_to_Utopia | General guide for new players |
| 2 | Ages | Overview of the Age system |
| 3 | Aggressive_Actions | Aggressive actions and consequences |
| 4 | Aid | Aid system between provinces |
| 5 | Alliances | Alliance index and explanation |
| 6 | Ambush_Guide | Ambush guide |
| 7 | Ambushing | Ambush mechanics |
| 8 | Assassinate_wizards | Thievery operation: assassinate wizards |
| 9 | Attacking_&_Calculating_an_Attack | Attack calculation and mechanics |
| 10 | Buildings | Buildings and construction |
| 11 | Bushels | Bushels (food) system |
| 12 | Chaining | Attack chaining strategy |
| 13 | Creating_a_province | How to create a province |
| 14 | Dark_Elves | Race: Dark Elves |
| 15 | Dragons | Dragon system |
| 16 | Dragons,_Aid_&_Stances | Dragons, aid and stances |
| 17 | Dual_Monarch | Dual Monarch guide |
| 18 | Economy | Economic system |
| 19 | Ethics_of_Waving_and_War | Ethics of waving and war |
| 20 | Exploration | Exploration system |
| 21 | Explore_Pool | Explore pool |
| 22 | FAQ | Frequently asked questions |
| 23 | Finding_Good_Learn_Targets | How to find good learn targets |
| 24 | Finding_Good_Plunder_Targets | How to find good plunder targets |
| 25 | Formulas | Game formulas index |
| 26 | Fountain_of_knowledge | Spell: Fountain of Knowledge |
| 27 | Freeze_time | Freeze time mechanic |
| 28 | Game_Rules | Official game rules |
| 29 | Getting_Started_with_Utopia | Getting started guide |
| 30 | Guide | General strategy guide |
| 31 | Guide_Combo_Selection | Race/personality combo selection guide |
| 32 | Guides | Guide index |
| 33 | Island | Island system |
| 34 | Kingdoms | Kingdom mechanics |
| 35 | Land_Whorring_Tips_&_Tricks | Land whoring guide |
| 36 | Leadership_Logic | Leadership and KD management logic |
| 37 | Magic_Formulas | Magic formulas |
| 38 | Monarchy | Monarchy system |
| 39 | Multi-Attack_Protection_(MAP) | Multi-attack protection |
| 40 | Mystics_Spell_Table | Mystics spell table |
| 41 | Networth | Networth calculation |
| 42 | Offensive_Military_Efficiency | Offensive military efficiency |
| 43 | Overpop_Mitigation | Overpopulation mitigation |
| 44 | Overpopulation | Overpopulation mechanic |
| 45 | Paper_Utopia | The kingdom newspaper |
| 46 | Protection | Protection system |
| 47 | Province | Province overview |
| 48 | Quick_Tips | Quick tips |
| 49 | Recommended_Defense | Recommended defense |
| 50 | Relations | Kingdom relations system |
| 51 | Relations_Meter | Relations meter |
| 52 | Reservations | Reservations system |
| 53 | Ritual | Ritual mechanic |
| 54 | Rules | Game rules |
| 55 | Runes | Rune system |
| 56 | Science_Formulas | Science formulas |
| 57 | Scientists | Scientists system |
| 58 | Should_my_KD_Predetermine_a_Setup_ | Guide: predetermining a KD setup |
| 59 | SoM_translation | Sword of Might translation |
| 60 | Spell_Uses | Spell uses |
| 61 | Stances | Kingdom stances |
| 62 | The_Plague | Plague mechanic |
| 63 | Thievery_Formulas | Thievery formulas |
| 64 | Throne | Throne page |
| 65 | Time_in_Utopia | Time system in Utopia |
| 66 | Traditional_march | Attack type: Traditional March |
| 67 | Tutorials | Tutorial index |
| 68 | Unique_Abilities | Unique race abilities |
| 69 | Utopia | General game overview |
| 70 | Utopian_server | Game server info |
| 71 | War_Score | War score |
| 72 | Warleader_Guide_to_Attrition | Warleader's guide to attrition |
| 73 | Wizards | Wizards and units system |
| 74 | WoL_Personalities | World of Legends personalities |
| 75 | World_of_Legends | WoL server info |

## Output Structure

```
wiki_offline/
  index.html                 # Index with keep + special pages only
  page_config.json           # Configuration (current_age, page status)
  manual_notes.md            # Authoritative manual notes (Part 1 of export)
  utopia_wiki.md             # Exported markdown (generated by --export-md)
  scraper_progress.json      # Download state (for resume)
  css/
    style.css                # Stylesheet for offline browsing
  pages/                     # Keep pages (75 + 1 special)
    _Age_Details_Current.html
    Spells.html
    ...
  archived/                  # Ignored pages (~487 files)
  images/
```
