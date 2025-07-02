from query_classifier import is_valid_query
from cache_handler import get_similar_result, store_result
from serpapi_scraper import get_top_links, scrape_links
from summarizer import summarize_texts
from vector_store import load_vector_store

def main():
    print("🧠 Web Query Agent (CLI)")
    vector_store = load_vector_store()

    while True:
        query = input("\nEnter your query (or type 'exit'): ").strip().lower()
        if query == 'exit':
            break

        if not is_valid_query(query):
            print("❌ This is not a valid query.")
            continue

        cached = get_similar_result(vector_store, query)
        if cached:
            print("📦 Retrieved from memory:")
            print("\n🧠 Answer:\n", cached)
            continue

        print("🌐 Searching the web...")
        links = get_top_links(query)

        print("🔍 Scraping top pages...")
        texts = scrape_links(links)

        print("✍️ Summarizing content...")
        summary = summarize_texts(query, texts)

        print("\n🧠 Answer:\n", summary)
        vector_store = store_result(vector_store, query, summary)  # Save after confirming it worked

if __name__ == "__main__":
    main()

