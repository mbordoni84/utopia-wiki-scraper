"""Re-download ONLY the Age Details special page(s).

Use this at an age change when the wiki pages (Part 3) are unchanged and you
only need a fresh Part 2: it avoids re-hitting the wiki for all keep pages and
refreshes only the special page(s) listed in page_config.json. Mirrors the
special-page block of scraper.update_keep().

Run with: .venv/bin/python update_special_page.py

NOTE: this overwrites wiki_offline/pages/_Age_Details_Current.html with the
live (possibly buggy) version. Re-apply any manual Part 2 corrections and
re-run --export-md afterwards. See CLAUDE.md "Regular Updates".
"""
import json
import os

from bs4 import BeautifulSoup

from scraper import UtopiaWikiScraper

OUTPUT_DIR = "wiki_offline"


def main():
    config_path = os.path.join(OUTPUT_DIR, "page_config.json")
    with open(config_path) as f:
        config = json.load(f)

    scraper = UtopiaWikiScraper(output_dir=OUTPUT_DIR)
    scraper.create_css()

    for sp in config.get("special_pages", []):
        url = sp["url"]
        filename = sp.get("filename", "_special") + ".html"
        filepath = os.path.join(OUTPUT_DIR, "pages", filename)
        print(f"Downloading special page: {sp['name']}\n  URL: {url}")
        resp = scraper._request_with_retry(url)
        soup = BeautifulSoup(resp.text, "html.parser")
        if scraper.download_images:
            scraper._process_images(soup)
        html_content = scraper._wrap_html(sp["name"], str(soup))
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(html_content)
        print(f"  Saved: {filename} ({os.path.getsize(filepath)/1024:.1f} KB)")


if __name__ == "__main__":
    main()
