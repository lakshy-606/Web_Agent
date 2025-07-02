# serpapi_scraper.py

import os
from serpapi import GoogleSearch
from typing import List
from playwright.sync_api import sync_playwright
import time

SERPAPI_API_KEY = os.getenv("SERPAPI_API_KEY")

def get_top_links(query: str, num_results: int = 5) -> List[str]:
    search = GoogleSearch({
        "q": query,
        "api_key": SERPAPI_API_KEY,
        "num": num_results
    })
    results = search.get_dict()
    links = [res["link"] for res in results.get("organic_results", []) if "link" in res]
    return links[:num_results]


def scrape_page(url: str) -> str:
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        try:
            page.goto(url, timeout=15000)
            time.sleep(2)  # Let JS render
            content = page.locator("body").inner_text()
            return content.strip()
        except Exception as e:
            print(f"❌ Error scraping {url}: {e}")
            return ""
        finally:
            browser.close()


def scrape_links(links: List[str]) -> List[str]:
    texts = []
    for link in links:
        print(f"🔗 Scraping: {link}")
        content = scrape_page(link)
        if content:
            texts.append(content[:4000])  # Limit to avoid token overload
    return texts
