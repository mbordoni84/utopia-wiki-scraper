#!/usr/bin/env python3
"""
Utopia Wiki Offline Scraper
Scarica tutte le pagine del wiki di Utopia per la consultazione offline.
Usa l'API MediaWiki per elencare le pagine e salva sia l'HTML che il testo.
"""

import os
import re
import sys
import json
import time
import argparse
import hashlib
from urllib.parse import urljoin, urlparse, parse_qs, unquote

import requests
from bs4 import BeautifulSoup

WIKI_BASE = "https://wiki.utopia-game.com"
API_URL = f"{WIKI_BASE}/api.php"
INDEX_URL = f"{WIKI_BASE}/index.php"

DEFAULT_OUTPUT_DIR = "wiki_offline"
DEFAULT_DELAY = 1.0  # secondi tra le richieste
MAX_RETRIES = 10  # il sito da spesso 502, serve insistere
RETRY_BASE_DELAY = 3  # secondi di base per il backoff
PROGRESS_FILE = "scraper_progress.json"


class UtopiaWikiScraper:
    def __init__(self, output_dir=DEFAULT_OUTPUT_DIR, delay=DEFAULT_DELAY, download_images=True, max_retries=MAX_RETRIES):
        self.output_dir = output_dir
        self.delay = delay
        self.download_images = download_images
        self.max_retries = max_retries
        self.session = requests.Session()
        self.session.headers.update({
            "User-Agent": "UtopiaWikiScraper/1.0 (offline personal use)"
        })
        self.downloaded_pages = set()
        self.downloaded_images = set()
        self.failed_pages = []
        self.progress_file = os.path.join(self.output_dir, PROGRESS_FILE)

        os.makedirs(self.output_dir, exist_ok=True)
        os.makedirs(os.path.join(self.output_dir, "pages"), exist_ok=True)
        os.makedirs(os.path.join(self.output_dir, "images"), exist_ok=True)
        os.makedirs(os.path.join(self.output_dir, "css"), exist_ok=True)

        # Carica progresso precedente per riprendere download interrotti
        self._load_progress()

    def _load_progress(self):
        """Carica il progresso da un file per riprendere download interrotti."""
        if os.path.exists(self.progress_file):
            try:
                with open(self.progress_file, "r") as f:
                    data = json.load(f)
                self.downloaded_pages = set(data.get("downloaded_pages", []))
                self.downloaded_images = set(data.get("downloaded_images", []))
                if self.downloaded_pages:
                    print(f"Riprendendo download precedente: {len(self.downloaded_pages)} pagine gia' scaricate.")
            except (json.JSONDecodeError, KeyError):
                pass

    def _save_progress(self):
        """Salva il progresso su file."""
        data = {
            "downloaded_pages": sorted(self.downloaded_pages),
            "downloaded_images": sorted(self.downloaded_images),
            "failed_pages": sorted(set(self.failed_pages)),
        }
        with open(self.progress_file, "w") as f:
            json.dump(data, f, indent=2)

    @staticmethod
    def show_status(output_dir=DEFAULT_OUTPUT_DIR):
        """Mostra lo stato del download."""
        progress_file = os.path.join(output_dir, PROGRESS_FILE)
        if not os.path.exists(progress_file):
            print("Nessun download precedente trovato.")
            return

        with open(progress_file, "r") as f:
            data = json.load(f)

        downloaded = data.get("downloaded_pages", [])
        images = data.get("downloaded_images", [])
        failed = data.get("failed_pages", [])

        print(f"=== Stato download wiki ===")
        print(f"Pagine scaricate:  {len(downloaded)}")
        print(f"Immagini scaricate: {len(images)}")
        print(f"Pagine fallite:    {len(failed)}")

        if failed:
            print(f"\nPagine non scaricate:")
            for p in failed:
                print(f"  - {p}")

        print(f"\nRilancia lo script per riprendere il download delle pagine mancanti.")

    def _request_with_retry(self, url, params=None, timeout=30, binary=False):
        """Effettua una richiesta HTTP con retry aggressivo per gestire i 502."""
        last_error = None
        for attempt in range(1, self.max_retries + 1):
            try:
                resp = self.session.get(url, params=params, timeout=timeout)
                if resp.status_code == 502:
                    wait = RETRY_BASE_DELAY * attempt
                    print(f"    502 Bad Gateway (tentativo {attempt}/{MAX_RETRIES}), riprovo tra {wait}s...")
                    time.sleep(wait)
                    continue
                if resp.status_code == 503:
                    wait = RETRY_BASE_DELAY * attempt
                    print(f"    503 Service Unavailable (tentativo {attempt}/{MAX_RETRIES}), riprovo tra {wait}s...")
                    time.sleep(wait)
                    continue
                resp.raise_for_status()
                return resp
            except requests.exceptions.ConnectionError as e:
                last_error = e
                wait = RETRY_BASE_DELAY * attempt
                print(f"    Errore connessione (tentativo {attempt}/{MAX_RETRIES}), riprovo tra {wait}s...")
                time.sleep(wait)
            except requests.exceptions.Timeout as e:
                last_error = e
                wait = RETRY_BASE_DELAY * attempt
                print(f"    Timeout (tentativo {attempt}/{MAX_RETRIES}), riprovo tra {wait}s...")
                time.sleep(wait)
            except requests.RequestException as e:
                raise  # errori non recuperabili (es. 404)

        raise requests.RequestException(f"Fallito dopo {self.max_retries} tentativi: {last_error}")

    def get_all_pages(self):
        """Usa l'API MediaWiki per ottenere la lista di tutte le pagine."""
        pages = []
        params = {
            "action": "query",
            "list": "allpages",
            "aplimit": "500",
            "format": "json",
        }

        print("Recupero lista pagine dal wiki...")
        while True:
            try:
                resp = self._request_with_retry(API_URL, params=params)
                data = resp.json()
            except requests.RequestException as e:
                print(f"Errore API: {e}")
                print("Provo metodo alternativo (scraping di Special:AllPages)...")
                return self._get_all_pages_fallback()

            for page in data.get("query", {}).get("allpages", []):
                pages.append(page["title"])

            # Paginazione
            if "continue" in data:
                params["apcontinue"] = data["continue"]["apcontinue"]
                time.sleep(0.5)
            else:
                break

        print(f"Trovate {len(pages)} pagine.")
        return pages

    def _get_all_pages_fallback(self):
        """Fallback: scraping della pagina Special:AllPages."""
        pages = set()
        url = f"{INDEX_URL}?title=Special:AllPages"

        while url:
            try:
                resp = self._request_with_retry(url)
            except requests.RequestException as e:
                print(f"Errore nel fallback: {e}")
                break

            soup = BeautifulSoup(resp.text, "html.parser")
            content = soup.find("div", {"class": "mw-allpages-body"})
            if content:
                for link in content.find_all("a"):
                    title = link.get("title")
                    if title:
                        pages.add(title)

            # Controlla se c'e' un link "next"
            nav = soup.find("div", {"class": "mw-allpages-nav"})
            url = None
            if nav:
                for link in nav.find_all("a"):
                    if "next" in link.text.lower() or "prossim" in link.text.lower():
                        url = urljoin(WIKI_BASE, link["href"])
                        break

            time.sleep(0.5)

        print(f"Trovate {len(pages)} pagine (fallback).")
        return sorted(pages)

    def safe_filename(self, title):
        """Converte un titolo di pagina in un nome file sicuro."""
        name = re.sub(r'[<>:"/\\|?*]', '_', title)
        name = name.replace(' ', '_')
        if len(name) > 200:
            name = name[:180] + '_' + hashlib.md5(title.encode()).hexdigest()[:8]
        return name

    def download_page(self, title):
        """Scarica una singola pagina wiki."""
        if title in self.downloaded_pages:
            return

        filename = self.safe_filename(title) + ".html"
        filepath = os.path.join(self.output_dir, "pages", filename)

        params = {
            "title": title,
            "action": "render",  # solo il contenuto, senza chrome del sito
        }

        try:
            resp = self._request_with_retry(INDEX_URL, params=params)
        except requests.RequestException as e:
            print(f"  ERRORE: {title} - {e}")
            self.failed_pages.append(title)
            return

        soup = BeautifulSoup(resp.text, "html.parser")

        # Scarica immagini se richiesto
        if self.download_images:
            self._process_images(soup)

        # Aggiorna i link interni per puntare ai file locali
        self._fix_internal_links(soup)

        # Genera HTML completo con stile base
        html_content = self._wrap_html(title, str(soup))

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(html_content)

        self.downloaded_pages.add(title)

    def _process_images(self, soup):
        """Scarica le immagini e aggiorna i src."""
        for img in soup.find_all("img"):
            src = img.get("src")
            if not src:
                continue

            img_url = urljoin(WIKI_BASE, src)

            if img_url in self.downloaded_images:
                img["src"] = "../images/" + self._img_filename(img_url)
                continue

            try:
                resp = self._request_with_retry(img_url, timeout=15)
            except requests.RequestException:
                continue

            img_name = self._img_filename(img_url)
            img_path = os.path.join(self.output_dir, "images", img_name)

            with open(img_path, "wb") as f:
                f.write(resp.content)

            img["src"] = "../images/" + img_name
            self.downloaded_images.add(img_url)
            time.sleep(0.2)

    def _img_filename(self, url):
        """Genera un nome file per un'immagine a partire dall'URL."""
        parsed = urlparse(url)
        basename = os.path.basename(unquote(parsed.path))
        if not basename or len(basename) > 150:
            basename = hashlib.md5(url.encode()).hexdigest() + ".png"
        return re.sub(r'[<>:"/\\|?*]', '_', basename)

    def _fix_internal_links(self, soup):
        """Converte i link interni del wiki in link ai file locali."""
        for a in soup.find_all("a", href=True):
            href = a["href"]

            # Link interni del wiki
            if href.startswith("/index.php"):
                parsed = urlparse(href)
                params = parse_qs(parsed.query)
                if "title" in params:
                    title = params["title"][0]
                    a["href"] = self.safe_filename(title) + ".html"
                continue

            if href.startswith("/wiki/"):
                title = unquote(href.split("/wiki/", 1)[1])
                a["href"] = self.safe_filename(title) + ".html"
                continue

    def _wrap_html(self, title, body_content):
        """Avvolge il contenuto in un documento HTML completo con stile."""
        return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - Utopia Wiki</title>
    <link rel="stylesheet" href="../css/style.css">
</head>
<body>
    <nav class="breadcrumb">
        <a href="../index.html">Home</a> &raquo; {title}
    </nav>
    <article>
        <h1>{title}</h1>
        {body_content}
    </article>
</body>
</html>"""

    def create_index(self, pages):
        """Crea la pagina indice con link a tutte le pagine scaricate."""
        links = []
        for title in sorted(pages):
            if title in self.downloaded_pages:
                filename = self.safe_filename(title) + ".html"
                links.append(f'        <li><a href="pages/{filename}">{title}</a></li>')

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
        <p>{len(self.downloaded_pages)} pagine scaricate</p>
    </header>
    <main>
        <h2>Indice delle pagine</h2>
        <input type="text" id="search" placeholder="Cerca una pagina..." onkeyup="filterPages()">
        <ul id="page-list">
{chr(10).join(links)}
        </ul>
    </main>
    <script>
    function filterPages() {{
        const query = document.getElementById('search').value.toLowerCase();
        const items = document.querySelectorAll('#page-list li');
        items.forEach(item => {{
            const text = item.textContent.toLowerCase();
            item.style.display = text.includes(query) ? '' : 'none';
        }});
    }}
    </script>
</body>
</html>"""

        with open(os.path.join(self.output_dir, "index.html"), "w", encoding="utf-8") as f:
            f.write(html)

    def create_css(self):
        """Crea un foglio di stile base per la consultazione offline."""
        css = """body {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    max-width: 960px;
    margin: 0 auto;
    padding: 20px;
    background: #f8f9fa;
    color: #222;
    line-height: 1.6;
}

header {
    border-bottom: 2px solid #3366cc;
    padding-bottom: 10px;
    margin-bottom: 20px;
}

h1 { color: #1a1a2e; }
h2 { color: #2c3e50; border-bottom: 1px solid #ddd; padding-bottom: 5px; }

a { color: #3366cc; text-decoration: none; }
a:hover { text-decoration: underline; }

.breadcrumb {
    background: #e8e8e8;
    padding: 8px 15px;
    border-radius: 4px;
    margin-bottom: 20px;
    font-size: 0.9em;
}

article {
    background: #fff;
    padding: 20px 30px;
    border-radius: 6px;
    box-shadow: 0 1px 3px rgba(0,0,0,0.1);
}

table {
    border-collapse: collapse;
    width: 100%;
    margin: 15px 0;
}

th, td {
    border: 1px solid #ccc;
    padding: 8px 12px;
    text-align: left;
}

th { background: #e8e8e8; }
tr:nth-child(even) { background: #f5f5f5; }

img { max-width: 100%; height: auto; }

#search {
    width: 100%;
    padding: 10px;
    font-size: 16px;
    border: 1px solid #ccc;
    border-radius: 4px;
    margin-bottom: 15px;
    box-sizing: border-box;
}

ul { list-style: none; padding: 0; }
ul li {
    padding: 6px 0;
    border-bottom: 1px solid #eee;
}

code, pre {
    background: #f0f0f0;
    padding: 2px 6px;
    border-radius: 3px;
    font-size: 0.9em;
}

pre {
    padding: 15px;
    overflow-x: auto;
}
"""
        with open(os.path.join(self.output_dir, "css", "style.css"), "w", encoding="utf-8") as f:
            f.write(css)

    def run(self):
        """Esegue lo scraping completo."""
        self.create_css()

        pages = self.get_all_pages()
        if not pages:
            print("Nessuna pagina trovata. Il sito potrebbe essere offline.")
            sys.exit(1)

        total = len(pages)
        skipped = 0
        for i, title in enumerate(pages, 1):
            if title in self.downloaded_pages:
                skipped += 1
                continue
            print(f"[{i}/{total}] Scaricando: {title}" + (f" (saltate {skipped})" if skipped and i == skipped + 1 else ""))
            self.download_page(title)
            self._save_progress()
            time.sleep(self.delay)

        # Secondo passaggio: ritenta le pagine fallite
        if self.failed_pages:
            print(f"\n--- Secondo passaggio: ritento {len(self.failed_pages)} pagine fallite ---")
            retry_list = list(self.failed_pages)
            self.failed_pages = []
            for i, title in enumerate(retry_list, 1):
                print(f"[retry {i}/{len(retry_list)}] {title}")
                self.download_page(title)
                self._save_progress()
                time.sleep(self.delay * 2)  # attesa doppia nel retry

        self.create_index(pages)
        self._save_progress()

        # Report finale
        print(f"\n{'='*50}")
        print(f"Download completato!")
        print(f"Pagine scaricate: {len(self.downloaded_pages)}/{total}")
        print(f"Immagini scaricate: {len(self.downloaded_images)}")
        if self.failed_pages:
            print(f"Pagine fallite: {len(self.failed_pages)}")
            for p in self.failed_pages:
                print(f"  - {p}")
            print(f"\nRilancia lo script per ritentare le pagine mancanti (il progresso e' salvato).")
        print(f"\nApri {self.output_dir}/index.html nel browser per consultare il wiki offline.")

    def update_keep(self):
        """Riscarica solo le pagine con status 'keep' dal page_config.json + special pages."""
        config_path = os.path.join(self.output_dir, "page_config.json")
        if not os.path.exists(config_path):
            print("page_config.json non trovato. Esegui prima: python3 page_manager.py --classify")
            sys.exit(1)

        with open(config_path, "r") as f:
            config = json.load(f)

        keep_pages = [name for name, info in config.get("pages", {}).items()
                      if info["status"] == "keep"]

        print(f"Aggiornamento di {len(keep_pages)} pagine keep...")
        self.create_css()

        # Forza il re-download ignorando il progress per queste pagine
        for i, title in enumerate(keep_pages, 1):
            print(f"[{i}/{len(keep_pages)}] Aggiornando: {title}")
            self.downloaded_pages.discard(title)
            self.download_page(title)
            self._save_progress()
            time.sleep(self.delay)

        # Scarica special pages
        special_pages = config.get("special_pages", [])
        for sp in special_pages:
            url = sp["url"]
            filename = sp.get("filename", "_special") + ".html"
            filepath = os.path.join(self.output_dir, "pages", filename)
            print(f"Scaricando pagina speciale: {sp['name']}")
            try:
                resp = self._request_with_retry(url)
                soup = BeautifulSoup(resp.text, "html.parser")
                if self.download_images:
                    self._process_images(soup)
                html_content = self._wrap_html(sp["name"], str(soup))
                with open(filepath, "w", encoding="utf-8") as f:
                    f.write(html_content)
                print(f"  Salvata: {filename}")
            except Exception as e:
                print(f"  ERRORE scaricando {sp['name']}: {e}")

        # Rigenera indice tramite page_manager
        try:
            from page_manager import PageManager
            mgr = PageManager(output_dir=self.output_dir)
            mgr._regenerate_index()
        except ImportError:
            self.create_index(keep_pages)

        # Report
        print(f"\n{'='*50}")
        print(f"Aggiornamento completato!")
        print(f"Pagine aggiornate: {len(keep_pages)}")
        if self.failed_pages:
            print(f"Pagine fallite: {len(self.failed_pages)}")
            for p in self.failed_pages:
                print(f"  - {p}")


def main():
    parser = argparse.ArgumentParser(description="Scarica il wiki di Utopia per consultazione offline")
    parser.add_argument("-o", "--output", default=DEFAULT_OUTPUT_DIR,
                        help=f"Directory di output (default: {DEFAULT_OUTPUT_DIR})")
    parser.add_argument("-d", "--delay", type=float, default=DEFAULT_DELAY,
                        help=f"Ritardo in secondi tra le richieste (default: {DEFAULT_DELAY})")
    parser.add_argument("--no-images", action="store_true",
                        help="Non scaricare le immagini")
    parser.add_argument("--status", action="store_true",
                        help="Mostra lo stato del download e le pagine mancanti")
    parser.add_argument("--update-keep", action="store_true",
                        help="Riscarica solo le pagine con status 'keep' + special pages")
    parser.add_argument("--reset", action="store_true",
                        help="Ignora il progresso precedente e ricomincia da zero")
    parser.add_argument("--retries", type=int, default=MAX_RETRIES,
                        help=f"Numero massimo di retry per richiesta (default: {MAX_RETRIES})")
    args = parser.parse_args()

    if args.status:
        UtopiaWikiScraper.show_status(args.output)
        return

    scraper = UtopiaWikiScraper(
        output_dir=args.output,
        delay=args.delay,
        download_images=not args.no_images,
        max_retries=args.retries,
    )

    if args.reset:
        scraper.downloaded_pages = set()
        scraper.downloaded_images = set()
        print("Progresso resettato.")

    if args.update_keep:
        scraper.update_keep()
    else:
        scraper.run()


if __name__ == "__main__":
    main()
