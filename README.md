# Web Browser Query Agent

This project is a command-line interface (CLI) agent that can answer queries by searching the web. It features a query classifier, a caching mechanism to store and retrieve results for similar queries, and a web scraper to gather and summarize information from the web.

## Architecture and Flow

The agent follows a specific workflow to handle user queries:

1.  **Query Classification:** The agent first classifies the user's query as either "valid" or "invalid." Invalid queries are typically commands or requests that cannot be answered by a web search (e.g., "buy an apple for me").
2.  **Cache Lookup:** If the query is valid, the agent checks its local cache (a FAISS vector store) to see if a similar query has been answered before.
3.  **Web Search and Scrape:** If the query is new, the agent uses the SerpAPI to perform a Google search and get the top 5 search results. It then scrapes the content of these web pages.
4.  **Summarization:** The scraped content is then summarized using a large language model (LLM) to provide a concise answer to the user's query.
5.  **Cache Storage:** The newly generated answer is stored in the cache for future use.

### Flowchart

```
+------------------+
|   User Query     |
+------------------+
        |
        v
+----------------------+      (Invalid)     +-------------------------+
|  Query Classifier    |------------------->| Respond "Invalid Query" |
+----------------------+      (Query)       +-------------------------+
        |
      (Valid)
        |
        v
+----------------------+   (Similar Found)  +-------------------------+
|    Cache Handler     |------------------->|  Return Cached Result   |
+----------------------+   (in Vector DB)   +-------------------------+
        |
      (New Query)
        |
        v
+----------------------+
|   SerpAPI Scraper    |
+----------------------+
        |
        v
+----------------------+
|      Summarizer      |
+----------------------+
        |
        v
+----------------------+
|    Return Summary    |
+----------------------+
        |
        v
+----------------------+
|   Store in Cache     |
+----------------------+
```

## File Breakdown

*   **`main.py`**: This is the main entry point for the application. It contains the main loop that prompts the user for input, orchestrates the calls to the other modules, and prints the final result.

*   **`query_classifier.py`**: This module is responsible for determining if a user's query is valid. It uses a list of regular expressions to identify and filter out invalid queries, such as commands or personal requests.

*   **`cache_handler.py`**: This module manages the caching of query results. It uses a FAISS vector store to find similar queries and retrieve their corresponding answers. It also handles the storing of new results.

*   **`vector_store.py`**: This module is responsible for loading and saving the FAISS vector store to and from the local disk.

*   **`serpapi_scraper.py`**: This module handles all interactions with the SerpAPI and the web scraping process. It fetches the top search results from Google and then uses Playwright to scrape the content of those pages.

*   **`summarizer.py`**: This module takes the scraped web content and uses a large language model to generate a concise and relevant summary that answers the user's original query.

*   **`requirements.txt`**: This file lists all the Python dependencies required to run the project.

*   **`.env`**: This file is used to store sensitive information, such as the SerpAPI API key.

## How to Run

1.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

2.  **Install Playwright Browsers:**
    ```bash
    python -m playwright install
    ```

3.  **Set API Key:**
    *   Open the `.env` file.
    *   Replace `"your_serpapi_api_key"` with your actual SerpAPI key.

4.  **Run the Agent:**
    ```bash
    python main.py
    ```
