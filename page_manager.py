#!/usr/bin/env python3
"""
Utopia Wiki Page Manager
Classifica, archivia e gestisce le pagine scaricate dal wiki.
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
        """Trova tutti i file HTML in pages/ e archived/."""
        pages = {}
        for directory in [self.pages_dir, self.archive_dir]:
            if not os.path.exists(directory):
                continue
            for fname in os.listdir(directory):
                if fname.endswith(".html") and not fname.startswith("_"):
                    name = fname[:-5]  # rimuovi .html
                    pages[name] = os.path.join(directory, fname)
        return pages

    def _read_page_body(self, filepath):
        """Legge il corpo di una pagina HTML (senza titolo h1)."""
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
        """Classifica tutte le pagine secondo i criteri definiti."""
        all_pages = self._get_all_page_files()
        current_age = self.config.get("current_age", DEFAULT_AGE)

        # Preserva override manuali
        manual_overrides = {}
        for name, info in self.config.get("pages", {}).items():
            if info.get("reason") == "manual":
                manual_overrides[name] = info

        # Leggi contenuto di tutte le pagine
        page_bodies = {}
        for name, path in all_pages.items():
            page_bodies[name] = self._read_page_body(path)

        # Trova gruppi di duplicati
        content_groups = defaultdict(list)
        for name, body in page_bodies.items():
            key = body[:500] if body else ""
            content_groups[key].append(name)

        # Mappa duplicato -> pagina canonica (nome piu lungo)
        duplicate_map = {}
        for key, names in content_groups.items():
            if len(names) > 1 and key:
                canonical = max(names, key=len)
                for name in names:
                    if name != canonical:
                        duplicate_map[name] = canonical

        result = {}

        for name in sorted(all_pages.keys()):
            # Override manuale ha priorita
            if name in manual_overrides:
                result[name] = manual_overrides[name]
                continue

            body = page_bodies[name]

            # 1. Pagine vuote/placeholder
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

            # 2. Redirect
            if body[:50].startswith("Redirect to:"):
                result[name] = {"status": "ignore", "reason": "redirect"}
                continue

            # 3. Age specifiche
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

            # 4. Alliance
            if name.startswith("Alliance_"):
                result[name] = {"status": "ignore", "reason": "alliance_page"}
                continue
            if body[:20].startswith("Alliance:") or body[:30].startswith("This refers to a Disbanded"):
                result[name] = {"status": "ignore", "reason": "alliance_page"}
                continue

            # 5. Kingdom
            if name.startswith("Kingdom_"):
                result[name] = {"status": "ignore", "reason": "kingdom_page"}
                continue
            if body[:20].startswith("Kingdom -"):
                result[name] = {"status": "ignore", "reason": "kingdom_page"}
                continue

            # 6. Profili giocatori
            if "Player Information" in body[:100] and "Kingdoms" in body[:300]:
                result[name] = {"status": "ignore", "reason": "player_profile"}
                continue

            # 7. IRC/obsolete
            if name in IRC_PAGES or name.startswith("IRC_"):
                result[name] = {"status": "ignore", "reason": "irc_obsolete"}
                continue

            # 8. Tools/External
            if name in EXTERNAL_TOOL_PAGES:
                result[name] = {"status": "ignore", "reason": "external_tool"}
                continue

            # 9. Meta pages
            if name in META_PAGES:
                result[name] = {"status": "ignore", "reason": "meta_page"}
                continue

            # 10. Duplicati
            if name in duplicate_map:
                result[name] = {"status": "ignore", "reason": f"duplicate_of:{duplicate_map[name]}"}
                continue

            # 11. Default: keep
            result[name] = {"status": "keep", "reason": "core_content"}

        self.config["pages"] = result
        self._save_config()

        keep_count = sum(1 for v in result.values() if v["status"] == "keep")
        ignore_count = sum(1 for v in result.values() if v["status"] == "ignore")
        print(f"Classificazione completata: {keep_count} keep, {ignore_count} ignore ({len(result)} totali)")
        print(f"Configurazione salvata in {self.config_path}")

    def review(self):
        """Mostra un riepilogo delle classificazioni per categoria."""
        pages = self.config.get("pages", {})
        if not pages:
            print("Nessuna classificazione trovata. Esegui prima --classify.")
            return

        # Raggruppa per reason
        by_reason = defaultdict(list)
        for name, info in pages.items():
            key = f"{info['status']}:{info['reason'].split(':')[0]}"
            by_reason[key].append(name)

        print(f"=== Riepilogo classificazione ===")
        print(f"Age corrente: {self.config.get('current_age', '?')}")
        print(f"Totale pagine: {len(pages)}")
        print()

        # Keep first
        print("--- KEEP ---")
        for key in sorted(by_reason.keys()):
            if not key.startswith("keep:"):
                continue
            reason = key.split(":", 1)[1]
            names = by_reason[key]
            print(f"  {reason}: {len(names)} pagine")

        print()
        print("--- IGNORE ---")
        for key in sorted(by_reason.keys()):
            if not key.startswith("ignore:"):
                continue
            reason = key.split(":", 1)[1]
            names = by_reason[key]
            print(f"  {reason}: {len(names)} pagine")

        print()
        keep_total = sum(1 for v in pages.values() if v["status"] == "keep")
        ignore_total = sum(1 for v in pages.values() if v["status"] == "ignore")
        print(f"Totale keep: {keep_total}")
        print(f"Totale ignore: {ignore_total}")

    def list_pages(self, status_filter):
        """Lista le pagine per status."""
        pages = self.config.get("pages", {})
        if not pages:
            print("Nessuna classificazione trovata. Esegui prima --classify.")
            return

        for name in sorted(pages.keys()):
            info = pages[name]
            if status_filter == "all" or info["status"] == status_filter:
                print(f"  [{info['status']:6s}] {name}  ({info['reason']})")

    def archive(self):
        """Sposta le pagine ignore in archived/."""
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

        print(f"Archiviate {moved} pagine in {self.archive_dir}/")

        # Rigenera indice con sole pagine keep
        self._regenerate_index()

    def restore(self, page_name):
        """Ripristina una pagina dall'archivio."""
        src = os.path.join(self.archive_dir, page_name + ".html")
        dst = os.path.join(self.pages_dir, page_name + ".html")

        if not os.path.exists(src):
            print(f"Pagina '{page_name}' non trovata in archivio.")
            return

        shutil.move(src, dst)
        if page_name in self.config.get("pages", {}):
            self.config["pages"][page_name] = {"status": "keep", "reason": "manual"}
        self._save_config()
        self._regenerate_index()
        print(f"Ripristinata: {page_name}")

    def set_status(self, page_name, status):
        """Imposta manualmente lo status di una pagina."""
        pages = self.config.get("pages", {})
        if page_name not in pages:
            print(f"Pagina '{page_name}' non trovata nella configurazione.")
            return
        pages[page_name] = {"status": status, "reason": "manual"}
        self._save_config()
        print(f"Impostato: {page_name} -> {status}")

    def set_age(self, age_number):
        """Aggiorna la current_age e riclassifica."""
        self.config["current_age"] = age_number
        self._save_config()
        print(f"Age aggiornata a {age_number}. Riclassifico...")
        self.classify()

    def _regenerate_index(self):
        """Rigenera index.html con sole pagine keep + special pages."""
        pages = self.config.get("pages", {})
        special = self.config.get("special_pages", [])

        # Special pages in cima
        special_links = []
        for sp in special:
            fname = sp.get("filename", "_special") + ".html"
            fpath = os.path.join(self.pages_dir, fname)
            if os.path.exists(fpath):
                special_links.append(
                    f'        <li class="special"><a href="pages/{fname}">{sp["name"]}</a></li>'
                )

        # Pagine keep
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
        <p>{total} pagine disponibili (Age {self.config.get('current_age', '?')})</p>
    </header>
    <main>
        <h2>Indice delle pagine</h2>
        <input type="text" id="search" placeholder="Cerca una pagina..." onkeyup="filterPages()">
"""
        if special_links:
            html += """        <h3>Pagine speciali</h3>
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
        print(f"Indice rigenerato: {total} pagine.")

    def export_md(self, output_file=None):
        """Esporta tutte le pagine keep + special in un unico file Markdown."""
        pages = self.config.get("pages", {})
        special = self.config.get("special_pages", [])
        current_age = self.config.get("current_age", "?")

        if output_file is None:
            output_file = os.path.join(self.output_dir, "utopia_wiki.md")

        sections = []

        # Header
        sections.append(f"# Utopia Wiki - Age {current_age}\n")

        # Special pages first
        for sp in special:
            fname = sp.get("filename", "_special") + ".html"
            fpath = os.path.join(self.pages_dir, fname)
            if os.path.exists(fpath):
                title = sp["name"]
                body = self._html_to_markdown(fpath)
                sections.append(f"---\n\n## {title}\n\n{body}\n")

        # Keep pages
        for name in sorted(pages.keys()):
            if pages[name]["status"] != "keep":
                continue
            fpath = os.path.join(self.pages_dir, name + ".html")
            if not os.path.exists(fpath):
                continue
            title = name.replace("_", " ")
            body = self._html_to_markdown(fpath)
            sections.append(f"---\n\n## {title}\n\n{body}\n")

        content = "\n".join(sections)

        with open(output_file, "w", encoding="utf-8") as f:
            f.write(content)

        size_kb = os.path.getsize(output_file) / 1024
        page_count = len([n for n, i in pages.items() if i["status"] == "keep"])
        special_count = sum(1 for sp in special
                           if os.path.exists(os.path.join(self.pages_dir, sp.get("filename", "_special") + ".html")))
        print(f"Esportato: {output_file}")
        print(f"  {page_count + special_count} pagine, {size_kb:.0f} KB")

    def _html_to_markdown(self, filepath):
        """Converte una pagina HTML in testo Markdown semplificato."""
        with open(filepath, "r", encoding="utf-8") as f:
            soup = BeautifulSoup(f.read(), "html.parser")

        article = soup.find("article")
        if not article:
            article = soup.find("body") or soup

        # Rimuovi il titolo h1 (lo aggiungiamo noi come ##)
        h1 = article.find("h1")
        if h1:
            h1.decompose()

        # Converti headers
        for tag in article.find_all(["h2", "h3", "h4", "h5", "h6"]):
            level = int(tag.name[1])
            prefix = "#" * (level + 1)  # h2 -> ###, h3 -> ####
            tag.replace_with(f"\n{prefix} {tag.get_text().strip()}\n")

        # Converti tabelle in formato leggibile
        for table in article.find_all("table"):
            rows = []
            for tr in table.find_all("tr"):
                cells = [td.get_text().strip().replace("\n", " ")
                         for td in tr.find_all(["td", "th"])]
                if cells:
                    rows.append(" | ".join(cells))
            if rows:
                # Aggiungi separator dopo header
                table_text = rows[0] + "\n" + " | ".join(["---"] * rows[0].count("|") + ["---"]) if len(rows) > 0 else ""
                if len(rows) > 1:
                    table_text += "\n" + "\n".join(rows[1:])
                table.replace_with(f"\n{table_text}\n")

        # Converti liste
        for li in article.find_all("li"):
            li.replace_with(f"- {li.get_text().strip()}\n")

        # Converti bold/italic
        for b in article.find_all(["b", "strong"]):
            b.replace_with(f"**{b.get_text()}**")
        for i in article.find_all(["i", "em"]):
            i.replace_with(f"*{i.get_text()}*")

        # Estrai testo
        text = article.get_text()

        # Pulisci whitespace eccessivo
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
    parser = argparse.ArgumentParser(description="Gestisci le pagine scaricate del wiki di Utopia")
    parser.add_argument("-o", "--output", default=DEFAULT_OUTPUT_DIR,
                        help=f"Directory wiki offline (default: {DEFAULT_OUTPUT_DIR})")

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--classify", action="store_true",
                       help="Classifica automaticamente tutte le pagine")
    group.add_argument("--review", action="store_true",
                       help="Mostra riepilogo delle classificazioni")
    group.add_argument("--list", choices=["keep", "ignore", "all"],
                       help="Lista pagine per status")
    group.add_argument("--archive", action="store_true",
                       help="Sposta pagine ignore in archived/")
    group.add_argument("--restore", metavar="PAGINA",
                       help="Ripristina una pagina dall'archivio")
    group.add_argument("--set", nargs=2, metavar=("PAGINA", "STATUS"),
                       help="Imposta manualmente lo status (keep/ignore)")
    group.add_argument("--set-age", type=int, metavar="NUMERO",
                       help="Aggiorna la current_age e riclassifica")
    group.add_argument("--export-md", nargs="?", const=True, default=None,
                       metavar="FILE",
                       help="Esporta le pagine keep in un unico file Markdown (default: wiki_offline/utopia_wiki.md)")

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
            print("Status deve essere 'keep' o 'ignore'.")
            sys.exit(1)
        mgr.set_status(page, status)
    elif args.set_age is not None:
        mgr.set_age(args.set_age)
    elif args.export_md is not None:
        output_file = args.export_md if isinstance(args.export_md, str) else None
        mgr.export_md(output_file)


if __name__ == "__main__":
    main()
