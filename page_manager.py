#!/usr/bin/env python3
"""
Utopia Wiki Page Manager
Classifies, archives and manages downloaded wiki pages.
"""

import os
import re
import sys
import json
import shutil
import argparse
from collections import defaultdict

from bs4 import BeautifulSoup

DEFAULT_OUTPUT_DIR = "wiki_offline"
CONFIG_FILE = "page_config.json"
DEFAULT_AGE = 114

SPECIAL_PAGES_DEFAULT = [
    {
        "url": "https://utopia-game.com/wol/chooser/age_details/",
        "name": "Age Details (Current Age)",
        "filename": "_Age_Details_Current",
    }
]

# Pages that are known external tools (not game rules/strategy)
EXTERNAL_TOOL_PAGES = {
    "Firefox", "Mozilla_Firefox", "Pimp_Agent", "Pimp_Agent_2",
    "UtopiaPimp", "UtopiaPimp_V2", "Metatron", "Metatron_Plus",
    "MunkBot", "Munk", "Angel", "Utopia_Angel", "Seraphim",
    "Utopia_Seraphim", "DragonPortal", "UTools", "UTimes",
    "Seraphiel", "PostUto", "Target_Finder", "Intel_Site",
    "MIRC",
}

IRC_PAGES = {
    "IRC", "IRC_Bots", "IRC_FAQ", "IRC_Modes", "IRC_Opers",
    "IRC_Scripts", "ChanServ", "NickServ", "Operators", "UtoNet",
    "Using_IRC", "Channel", "Channels", "Services", "Net_Safety",
    "Caution",
}

META_PAGES = {
    "Sandbox", "Redirects", "Changelog", "SpecialThanks",
    "Custom_Themes", "Contents", "Main_Page",
    "Welcome_to_the_Utopia_Wiki", "UtopiaWiki_About",
    "Commonly_Used_Acronyms", "Dictionary",
    "Activation_Code", "Master_Account", "Preferences",
    "Ingame", "Gold_Status", "Invitations", "Theme",
}


class PageManager:
    def __init__(self, output_dir=DEFAULT_OUTPUT_DIR):
        self.output_dir = output_dir
        self.pages_dir = os.path.join(output_dir, "pages")
        self.archive_dir = os.path.join(output_dir, "archived")
        self.config_path = os.path.join(output_dir, CONFIG_FILE)
        self.config = self._load_config()

    def _load_config(self):
        if os.path.exists(self.config_path):
            with open(self.config_path, "r") as f:
                return json.load(f)
        return {
            "current_age": DEFAULT_AGE,
            "special_pages": SPECIAL_PAGES_DEFAULT,
            "pages": {},
        }

    def _save_config(self):
        with open(self.config_path, "w") as f:
            json.dump(self.config, f, indent=2, ensure_ascii=False)

    def _get_all_page_files(self):
        """Find all HTML files in pages/ and archived/."""
        pages = {}
        for directory in [self.pages_dir, self.archive_dir]:
            if not os.path.exists(directory):
                continue
            for fname in os.listdir(directory):
                if fname.endswith(".html") and not fname.startswith("_"):
                    name = fname[:-5]  # remove .html
                    pages[name] = os.path.join(directory, fname)
        return pages

    def _read_page_body(self, filepath):
        """Read the body of an HTML page (without the h1 title)."""
        with open(filepath, "r", encoding="utf-8") as f:
            soup = BeautifulSoup(f.read(), "html.parser")
        article = soup.find("article")
        if not article:
            return ""
        h1 = article.find("h1")
        if h1:
            h1.decompose()
        return article.get_text().strip()

    def classify(self):
        """Classify all pages according to defined criteria."""
        all_pages = self._get_all_page_files()
        current_age = self.config.get("current_age", DEFAULT_AGE)

        # Preserve manual overrides
        manual_overrides = {}
        for name, info in self.config.get("pages", {}).items():
            if info.get("reason") == "manual":
                manual_overrides[name] = info

        # Read content of all pages
        page_bodies = {}
        for name, path in all_pages.items():
            page_bodies[name] = self._read_page_body(path)

        # Find duplicate groups
        content_groups = defaultdict(list)
        for name, body in page_bodies.items():
            key = body[:500] if body else ""
            content_groups[key].append(name)

        # Map duplicate -> canonical page (longest name)
        duplicate_map = {}
        for key, names in content_groups.items():
            if len(names) > 1 and key:
                canonical = max(names, key=len)
                for name in names:
                    if name != canonical:
                        duplicate_map[name] = canonical

        result = {}

        for name in sorted(all_pages.keys()):
            # Manual override takes priority
            if name in manual_overrides:
                result[name] = manual_overrides[name]
                continue

            body = page_bodies[name]

            # 1. Empty/placeholder pages
            if len(body) < 50 or "UNDER CONSTRUCTION" in body or "flag:delete" in body:
                if body.strip() in ("", "TBD"):
                    result[name] = {"status": "ignore", "reason": "empty"}
                    continue
                if "flag:delete" in body or "UNDER CONSTRUCTION" in body:
                    result[name] = {"status": "ignore", "reason": "empty"}
                    continue
                if len(body) < 50:
                    result[name] = {"status": "ignore", "reason": "empty"}
                    continue

            # 2. Redirects
            if body[:50].startswith("Redirect to:"):
                result[name] = {"status": "ignore", "reason": "redirect"}
                continue

            # 3. Age-specific pages
            age_num_match = re.match(r"^Age_(\d+)$", name)
            age_sub_match = re.match(r"^Age_(\d+)_(Mechanics|Personalities|Races)$", name)
            age_name_match = re.match(r"^Age_of_", name)
            wol_age_match = re.match(r"^WoL_(Personalities|Races)_\(Age_(\d+)\)$", name)
            genesis_match = re.match(r"^Genesis_(Mechanics|Personalities|Races|Change_Log)$", name)

            age_number = None
            if age_num_match:
                age_number = int(age_num_match.group(1))
            elif age_sub_match:
                age_number = int(age_sub_match.group(1))
            elif wol_age_match:
                age_number = int(wol_age_match.group(2))

            if age_number is not None:
                if age_number == current_age:
                    result[name] = {"status": "keep", "reason": "current_age"}
                else:
                    result[name] = {"status": "ignore", "reason": "obsolete_age"}
                continue

            if age_name_match:
                result[name] = {"status": "ignore", "reason": "obsolete_age"}
                continue

            if genesis_match:
                result[name] = {"status": "ignore", "reason": "obsolete_age"}
                continue

            # 4. Alliance pages
            if name.startswith("Alliance_"):
                result[name] = {"status": "ignore", "reason": "alliance_page"}
                continue
            if body[:20].startswith("Alliance:") or body[:30].startswith("This refers to a Disbanded"):
                result[name] = {"status": "ignore", "reason": "alliance_page"}
                continue

            # 5. Kingdom pages
            if name.startswith("Kingdom_"):
                result[name] = {"status": "ignore", "reason": "kingdom_page"}
                continue
            if body[:20].startswith("Kingdom -"):
                result[name] = {"status": "ignore", "reason": "kingdom_page"}
                continue

            # 6. Player profiles
            if "Player Information" in body[:100] and "Kingdoms" in body[:300]:
                result[name] = {"status": "ignore", "reason": "player_profile"}
                continue

            # 7. IRC/obsolete
            if name in IRC_PAGES or name.startswith("IRC_"):
                result[name] = {"status": "ignore", "reason": "irc_obsolete"}
                continue

            # 8. External tools
            if name in EXTERNAL_TOOL_PAGES:
                result[name] = {"status": "ignore", "reason": "external_tool"}
                continue

            # 9. Meta pages
            if name in META_PAGES:
                result[name] = {"status": "ignore", "reason": "meta_page"}
                continue

            # 10. Duplicates
            if name in duplicate_map:
                result[name] = {"status": "ignore", "reason": f"duplicate_of:{duplicate_map[name]}"}
                continue

            # 11. Default: keep
            result[name] = {"status": "keep", "reason": "core_content"}

        self.config["pages"] = result
        self._save_config()

        keep_count = sum(1 for v in result.values() if v["status"] == "keep")
        ignore_count = sum(1 for v in result.values() if v["status"] == "ignore")
        print(f"Classification complete: {keep_count} keep, {ignore_count} ignore ({len(result)} total)")
        print(f"Configuration saved to {self.config_path}")

    def review(self):
        """Show a classification summary by category."""
        pages = self.config.get("pages", {})
        if not pages:
            print("No classification found. Run --classify first.")
            return

        # Group by reason
        by_reason = defaultdict(list)
        for name, info in pages.items():
            key = f"{info['status']}:{info['reason'].split(':')[0]}"
            by_reason[key].append(name)

        print(f"=== Classification summary ===")
        print(f"Current age: {self.config.get('current_age', '?')}")
        print(f"Total pages: {len(pages)}")
        print()

        print("--- KEEP ---")
        for key in sorted(by_reason.keys()):
            if not key.startswith("keep:"):
                continue
            reason = key.split(":", 1)[1]
            names = by_reason[key]
            print(f"  {reason}: {len(names)} pages")

        print()
        print("--- IGNORE ---")
        for key in sorted(by_reason.keys()):
            if not key.startswith("ignore:"):
                continue
            reason = key.split(":", 1)[1]
            names = by_reason[key]
            print(f"  {reason}: {len(names)} pages")

        print()
        keep_total = sum(1 for v in pages.values() if v["status"] == "keep")
        ignore_total = sum(1 for v in pages.values() if v["status"] == "ignore")
        print(f"Total keep: {keep_total}")
        print(f"Total ignore: {ignore_total}")

    def list_pages(self, status_filter):
        """List pages by status."""
        pages = self.config.get("pages", {})
        if not pages:
            print("No classification found. Run --classify first.")
            return

        for name in sorted(pages.keys()):
            info = pages[name]
            if status_filter == "all" or info["status"] == status_filter:
                print(f"  [{info['status']:6s}] {name}  ({info['reason']})")

    def archive(self):
        """Move ignored pages to archived/."""
        os.makedirs(self.archive_dir, exist_ok=True)
        pages = self.config.get("pages", {})
        moved = 0

        for name, info in pages.items():
            if info["status"] != "ignore":
                continue
            src = os.path.join(self.pages_dir, name + ".html")
            dst = os.path.join(self.archive_dir, name + ".html")
            if os.path.exists(src):
                shutil.move(src, dst)
                moved += 1

        print(f"Archived {moved} pages to {self.archive_dir}/")

        # Regenerate index with keep pages only
        self._regenerate_index()

    def restore(self, page_name):
        """Restore a page from the archive."""
        src = os.path.join(self.archive_dir, page_name + ".html")
        dst = os.path.join(self.pages_dir, page_name + ".html")

        if not os.path.exists(src):
            print(f"Page '{page_name}' not found in archive.")
            return

        shutil.move(src, dst)
        if page_name in self.config.get("pages", {}):
            self.config["pages"][page_name] = {"status": "keep", "reason": "manual"}
        self._save_config()
        self._regenerate_index()
        print(f"Restored: {page_name}")

    def set_status(self, page_name, status):
        """Manually set a page's status."""
        pages = self.config.get("pages", {})
        if page_name not in pages:
            print(f"Page '{page_name}' not found in configuration.")
            return
        pages[page_name] = {"status": status, "reason": "manual"}
        self._save_config()
        print(f"Set: {page_name} -> {status}")

    def set_age(self, age_number):
        """Update the current_age and reclassify."""
        self.config["current_age"] = age_number
        self._save_config()
        print(f"Age updated to {age_number}. Reclassifying...")
        self.classify()

    def _regenerate_index(self):
        """Regenerate index.html with keep + special pages only."""
        pages = self.config.get("pages", {})
        special = self.config.get("special_pages", [])

        # Special pages at the top
        special_links = []
        for sp in special:
            fname = sp.get("filename", "_special") + ".html"
            fpath = os.path.join(self.pages_dir, fname)
            if os.path.exists(fpath):
                special_links.append(
                    f'        <li class="special"><a href="pages/{fname}">{sp["name"]}</a></li>'
                )

        # Keep pages
        keep_links = []
        for name in sorted(pages.keys()):
            if pages[name]["status"] != "keep":
                continue
            fpath = os.path.join(self.pages_dir, name + ".html")
            if os.path.exists(fpath):
                display = name.replace("_", " ")
                keep_links.append(
                    f'        <li><a href="pages/{name}.html">{display}</a></li>'
                )

        total = len(special_links) + len(keep_links)

        html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Utopia Wiki - Offline</title>
    <link rel="stylesheet" href="css/style.css">
</head>
<body>
    <header>
        <h1>Utopia Wiki - Offline</h1>
        <p>{total} pages available (Age {self.config.get('current_age', '?')})</p>
    </header>
    <main>
        <h2>Page Index</h2>
        <input type="text" id="search" placeholder="Search for a page..." onkeyup="filterPages()">
"""
        if special_links:
            html += """        <h3>Special Pages</h3>
        <ul id="special-list">
"""
            html += "\n".join(special_links) + "\n"
            html += "        </ul>\n"

        html += """        <h3>Wiki</h3>
        <ul id="page-list">
"""
        html += "\n".join(keep_links) + "\n"
        html += """        </ul>
    </main>
    <script>
    function filterPages() {
        const query = document.getElementById('search').value.toLowerCase();
        document.querySelectorAll('#page-list li, #special-list li').forEach(item => {
            const text = item.textContent.toLowerCase();
            item.style.display = text.includes(query) ? '' : 'none';
        });
    }
    </script>
</body>
</html>"""

        with open(os.path.join(self.output_dir, "index.html"), "w", encoding="utf-8") as f:
            f.write(html)
        print(f"Index regenerated: {total} pages.")

    def export_md(self, output_file=None):
        """Export all keep + special pages into a single Markdown file."""
        pages = self.config.get("pages", {})
        special = self.config.get("special_pages", [])
        current_age = self.config.get("current_age", "?")

        # Age confirmation prompt
        print(f"Current age is set to: {current_age}")
        answer = input("Is this correct? (y/N): ").strip().lower()
        if answer not in ("y", "yes"):
            print("Aborted. Use --set-age <NUMBER> to update the age first.")
            return

        if output_file is None:
            output_file = os.path.join(self.output_dir, "utopia_wiki.md")

        # Check for manual notes
        manual_notes_path = os.path.join(self.output_dir, "manual_notes.md")
        if os.path.exists(manual_notes_path):
            with open(manual_notes_path, "r", encoding="utf-8") as f:
                manual_notes_content = f.read().strip()
            print("Manual notes: found (wiki_offline/manual_notes.md)")
        else:
            manual_notes_content = None
            print("Manual notes: not found (wiki_offline/manual_notes.md)")

        sections = []

        # Header
        sections.append(f"# Utopia Wiki - Age {current_age}\n")

        # Part 1: Manual Notes
        sections.append(
            "---\n\n"
            "# Part 1: Manual Notes (Authoritative)\n\n"
            "> **PRIORITY: HIGHEST — Overrides everything else.**\n"
            "> These notes are manually maintained and reflect the current age's confirmed rules.\n"
            "> If any information in Part 2 or Part 3 conflicts with this section, discard it and trust Part 1.\n"
        )
        if manual_notes_content:
            sections.append(f"{manual_notes_content}\n")
        else:
            sections.append("_No manual notes file found (wiki_offline/manual_notes.md)._\n")

        # Part 2: Age Details (special pages)
        sections.append(
            "---\n\n"
            "# Part 2: Age Details — Races & Personalities\n\n"
            "> **PRIORITY: HIGH — Current age data, second only to Part 1.**\n"
            "> This page is scraped directly from the game for the current age.\n"
            "> It is the authoritative source for race stats, personality stats, war doctrines, and unique abilities.\n"
            "> If Part 3 contradicts this section on any race or personality detail, trust Part 2.\n"
        )
        for sp in special:
            url = sp.get("url", "")
            fname = sp.get("filename", "_special") + ".html"
            fpath = os.path.join(self.pages_dir, fname)
            if url:
                sections.append(f"Source: {url}\n")
                print(f"Special page URL: {url}")
                print("  ⚠  Double-check this URL is still correct — it may change between ages.")
            if os.path.exists(fpath):
                body = self._html_to_markdown(fpath)
                sections.append(f"{body}\n")

        # Part 3: Wiki Pages
        sections.append(
            "---\n\n"
            "# Part 3: Wiki Pages\n\n"
            "> **PRIORITY: MEDIUM — Reliable for mechanics, formulas, and concepts. Unreliable for current-age specifics.**\n"
            "> These are scraped wiki pages. They are valuable for game formulas, mechanics explanations, and strategic guides.\n"
            "> However, they may reference races, personalities, abilities, or balance values from past ages.\n"
            "> Do NOT use Part 3 as the source of truth for race/personality stats, unique abilities, or any data\n"
            "> that changes between ages. For those, defer to Part 1 and Part 2.\n"
        )
        for name in sorted(pages.keys()):
            if pages[name]["status"] != "keep":
                continue
            fpath = os.path.join(self.pages_dir, name + ".html")
            if not os.path.exists(fpath):
                continue
            title = name.replace("_", " ")
            body = self._html_to_markdown(fpath)
            sections.append(f"## {title}\n\n{body}\n")

        content = "\n".join(sections)

        with open(output_file, "w", encoding="utf-8") as f:
            f.write(content)

        size_kb = os.path.getsize(output_file) / 1024
        page_count = len([n for n, i in pages.items() if i["status"] == "keep"])
        special_count = sum(1 for sp in special
                           if os.path.exists(os.path.join(self.pages_dir, sp.get("filename", "_special") + ".html")))
        print(f"Exported: {output_file}")
        print(f"  {page_count + special_count} pages, {size_kb:.0f} KB")

    def _html_to_markdown(self, filepath):
        """Convert an HTML page to simplified Markdown text."""
        with open(filepath, "r", encoding="utf-8") as f:
            soup = BeautifulSoup(f.read(), "html.parser")

        article = soup.find("article")
        if not article:
            article = soup.find("body") or soup

        # Remove h1 title (we add it ourselves as ##)
        h1 = article.find("h1")
        if h1:
            h1.decompose()

        # Remove navigation footer tables (MediaWiki templates)
        nav_titles = {
            "The Utopia Guide",
            "Races & Personalities",
            "Races &amp; Personalities",
            "The Thieves' Toolbox",
            "The Thieves&#39; Toolbox",
            "The Spellbook",
            "Ages",
        }
        for table in article.find_all("table"):
            # Check for nav template tables by header text
            for th in table.find_all("th"):
                if th.get_text().strip() in nav_titles:
                    table.decompose()
                    break
            else:
                # Check for « Previous: navigation tables
                table_text = table.get_text()
                if "« Previous:" in table_text or "\u00ab Previous:" in table_text:
                    table.decompose()

        # Convert headers
        for tag in article.find_all(["h2", "h3", "h4", "h5", "h6"]):
            level = int(tag.name[1])
            prefix = "#" * (level + 1)  # h2 -> ###, h3 -> ####
            tag.replace_with(f"\n{prefix} {tag.get_text().strip()}\n")

        # Convert tables to readable format
        for table in article.find_all("table"):
            rows = []
            for tr in table.find_all("tr"):
                cells = [td.get_text().strip().replace("\n", " ")
                         for td in tr.find_all(["td", "th"])]
                if cells:
                    rows.append(" | ".join(cells))
            if rows:
                # Add separator after header
                table_text = rows[0] + "\n" + " | ".join(["---"] * rows[0].count("|") + ["---"]) if len(rows) > 0 else ""
                if len(rows) > 1:
                    table_text += "\n" + "\n".join(rows[1:])
                table.replace_with(f"\n{table_text}\n")

        # Convert lists
        for li in article.find_all("li"):
            li.replace_with(f"- {li.get_text().strip()}\n")

        # Convert bold/italic
        for b in article.find_all(["b", "strong"]):
            b.replace_with(f"**{b.get_text()}**")
        for i in article.find_all(["i", "em"]):
            i.replace_with(f"*{i.get_text()}*")

        # Extract text
        text = article.get_text()

        # Clean excessive whitespace
        lines = []
        prev_empty = False
        for line in text.split("\n"):
            line = line.rstrip()
            if not line:
                if not prev_empty:
                    lines.append("")
                prev_empty = True
            else:
                lines.append(line)
                prev_empty = False

        return "\n".join(lines).strip()


def main():
    parser = argparse.ArgumentParser(description="Manage downloaded Utopia wiki pages")
    parser.add_argument("-o", "--output", default=DEFAULT_OUTPUT_DIR,
                        help=f"Offline wiki directory (default: {DEFAULT_OUTPUT_DIR})")

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--classify", action="store_true",
                       help="Automatically classify all pages")
    group.add_argument("--review", action="store_true",
                       help="Show classification summary")
    group.add_argument("--list", choices=["keep", "ignore", "all"],
                       help="List pages by status")
    group.add_argument("--archive", action="store_true",
                       help="Move ignored pages to archived/")
    group.add_argument("--restore", metavar="PAGE",
                       help="Restore a page from the archive")
    group.add_argument("--set", nargs=2, metavar=("PAGE", "STATUS"),
                       help="Manually set page status (keep/ignore)")
    group.add_argument("--set-age", type=int, metavar="NUMBER",
                       help="Update the current_age and reclassify")
    group.add_argument("--export-md", nargs="?", const=True, default=None,
                       metavar="FILE",
                       help="Export keep pages to a single Markdown file (default: wiki_offline/utopia_wiki.md)")

    args = parser.parse_args()
    mgr = PageManager(output_dir=args.output)

    if args.classify:
        mgr.classify()
    elif args.review:
        mgr.review()
    elif args.list:
        mgr.list_pages(args.list)
    elif args.archive:
        mgr.archive()
    elif args.restore:
        mgr.restore(args.restore)
    elif args.set:
        page, status = args.set
        if status not in ("keep", "ignore"):
            print("Status must be 'keep' or 'ignore'.")
            sys.exit(1)
        mgr.set_status(page, status)
    elif args.set_age is not None:
        mgr.set_age(args.set_age)
    elif args.export_md is not None:
        output_file = args.export_md if isinstance(args.export_md, str) else None
        mgr.export_md(output_file)


if __name__ == "__main__":
    main()
