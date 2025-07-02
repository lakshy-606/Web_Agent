from vector_store import save_vector_store
from langchain_core.documents import Document
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS

SIMILARITY_THRESHOLD = 0.4
embedding = OpenAIEmbeddings()

def get_similar_result(store: FAISS, new_query: str) -> str:
    if not store:
        return None
    
    results = store.similarity_search_with_score(new_query, k=1)
    
    if results and results[0][1] < SIMILARITY_THRESHOLD:
        doc, score = results[0]
        print(f"Found similar result with score: {score}")
        return doc.page_content
    return None

def store_result(store: FAISS, query: str, answer: str):
    doc = Document(page_content=answer, metadata={"query": query})
    if store:
        store.add_documents([doc])
    else:
        store = FAISS.from_documents([doc], embedding)
    
    save_vector_store(store)
    return store
