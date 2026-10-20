# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Offline scraper for the Utopia game wiki (https://wiki.utopia-game.com). Downloads wiki pages, classifies them as keep/ignore based on relevance (game rules and strategy only), and exports a single Markdown file for LLM grounding.

**Current Age:** 117 (Devoted Pursuits Crowned Promise) — update with `--set-age` when ages change

## Common Commands

### Full Workflow (Initial Setup)
```bash
python3 scraper.py                          # 1. Download all wiki pages
python3 page_manager.py --classify          # 2. Classify pages as keep/ignore
python3 page_manager.py --review            # 3. Review classification
python3 page_manager.py --archive           # 4. Move ignored pages to archived/
python3 page_manager.py --export-md         # 5. Export to utopia_wiki.md
```

### Regular Updates (After Age Change)
```bash
python3 page_manager.py --set-age 117       # Update age and reclassify
python3 scraper.py --update-keep            # Re-download keep pages + age_details
python3 page_manager.py --export-md         # Regenerate export
```

**IMPORTANT — Age Details (Part 2) can be buggy at the source.** The live
`age_details/` page is often programmed from the "prefinal changes" design doc
and can ship with known errors (wrong signs, leftover/removed rituals or
dragons, duplicate spells). When this happens:
1. Cross-check the scraped page against the official changes PDF for that age.
2. Apply the corrections **directly in the downloaded HTML**
   `wiki_offline/pages/_Age_Details_Current.html` so Part 2 is internally
   consistent (no values that contradict the manual notes).
3. Also record the same corrections as present-tense facts in
   `manual_notes.md` (Part 1) so they survive and reinforce the priority order.
4. Re-run `--export-md`.

Any `scraper.py --update-keep` (or re-download of the special page) overwrites
the HTML with the buggy live version, so these HTML corrections must be
re-applied afterwards. Age 117 required 10 such corrections — see the
"Age 117 Authoritative Data" section of `manual_notes.md` for the exact list.

**Dependencies:** `scraper.py`/`page_manager.py` need `requests` and
`beautifulsoup4`. There is no venv checked in; create one with
`python3 -m venv .venv && .venv/bin/pip install requests beautifulsoup4` and
run the scripts via `.venv/bin/python`.

### Other Useful Commands
```bash
python3 scraper.py --status                 # Show download progress
python3 page_manager.py --list keep         # List keep pages
python3 page_manager.py --set Dragons keep  # Manual override
python3 page_manager.py --restore Dragons   # Restore from archive
```

## Architecture

### Two-Script Design

**scraper.py** — Download engine
- Uses MediaWiki API to enumerate pages
- Aggressive retry mechanism (10 attempts, exponential backoff) for 502 errors
- Resumable downloads via `scraper_progress.json`
- Downloads both wiki pages and special pages (e.g., age details from main site)
- Converts wiki HTML to offline-browsable pages with local links

**page_manager.py** — Classification and export engine
- Classifies pages using rule-based filters (age-specific, duplicates, alliances, IRC, etc.)
- Supports manual overrides preserved across reclassifications
- Archives ignored pages to keep `pages/` clean
- Exports keep pages to `utopia_wiki.md` in 3-part structure

### Classification System

Pages are classified as `keep` (game rules/strategy) or `ignore` (alliances, kingdoms, profiles, old ages, IRC, duplicates, etc.).

**Classification rules** (in `page_manager.py:classify()`):
1. Empty/placeholder pages → ignore
2. Redirects → ignore
3. Age-specific pages → keep only if current age, otherwise ignore
4. Alliance/kingdom/player profile pages → ignore
5. IRC/external tool pages → ignore
6. Meta pages → ignore
7. Duplicates → ignore (keep canonical)
8. Default → keep (core content)

**Manual overrides:** Use `--set PAGE keep` to override classification. Manual overrides have `"reason": "manual"` and are preserved across reclassifications.

### Export Structure (utopia_wiki.md)

Three parts ordered by authority, each with LLM guidance blockquotes:

1. **Part 1: Manual Notes (Authoritative)** — `wiki_offline/manual_notes.md`
   - PRIORITY: HIGHEST
   - Overrides everything else
   - Manually maintained corrections for obsolete wiki data

2. **Part 2: Age Details (Current Age)** — Special page from https://utopia-game.com/wol/chooser/age_details/
   - PRIORITY: HIGH
   - Authoritative source for current age races, personalities, unique abilities, war doctrines
   - Scraped directly from game

3. **Part 3: Wiki Pages** — 56 keep pages from wiki
   - PRIORITY: MEDIUM
   - Reliable for formulas and mechanics
   - Unreliable for age-specific data (races, abilities, balance values)

### Key Data Structures

**wiki_offline/page_config.json:**
```json
{
  "current_age": 117,
  "special_pages": [
    {"url": "...", "name": "...", "filename": "_Age_Details_Current"}
  ],
  "pages": {
    "Dragons": {"status": "ignore", "reason": "obsolete"},
    "Spells": {"status": "keep", "reason": "core_content"}
  }
}
```

**wiki_offline/scraper_progress.json:**
```json
{
  "downloaded_pages": ["Spells", "..."],
  "downloaded_images": ["https://...", "..."],
  "failed_pages": []
}
```

### Obsolescence Management

When ages change (~every few months):
- Age-specific pages become obsolete (old age mechanics, old race/personality stats)
- Use `--set-age <N>` to update and reclassify
- Obsolete pages are moved to `archived/`
- Manual notes in `manual_notes.md` override obsolete wiki content
- Age details special page is re-downloaded with `--update-keep`

### Retry Logic

The wiki site frequently returns 502 Bad Gateway errors. `scraper.py` handles this with:
- Base retry delay: 3 seconds
- Exponential backoff: `3 * attempt_number` seconds
- Max retries: 10 (configurable with `--retries`)
- Also handles 503 and connection errors

Progress is saved after each page, so downloads are fully resumable.

## Output Structure

```
wiki_offline/
  index.html                 # Index with keep + special pages only
  page_config.json           # Configuration (current_age, page status)
  manual_notes.md            # Authoritative manual notes (Part 1 of export)
  utopia_wiki.md             # Exported markdown (generated by --export-md)
  scraper_progress.json      # Download state (for resume)
  css/style.css              # Stylesheet for offline browsing
  pages/                     # Keep pages (56 + 1 special)
    _Age_Details_Current.html
    Spells.html
    ...
  archived/                  # Ignored pages (~487 files)
  images/                    # Downloaded images
```

## Key Constraints

- Site reliability: Aggressive retry needed due to frequent 502 errors
- Age lifecycle: Pages become obsolete every few months when ages change
- LLM grounding: Export must guide LLMs on which source to trust (manual notes > age details > wiki)
- Classification persistence: Manual overrides must survive reclassifications
- Resumability: Long downloads must be resumable (progress tracking)

## Testing

No automated tests. Manual verification:
- After classification: `--review` to check counts by category
- After archiving: verify `archived/` has ignored pages, `pages/` has only keep pages
- After export: check `utopia_wiki.md` has all 3 parts with blockquote guidance
- After age change: verify age-specific pages moved to correct status
