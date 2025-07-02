# vector_store.py

import os
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

STORE_PATH = "query_store"
os.makedirs(STORE_PATH, exist_ok=True)

embedding_model = OpenAIEmbeddings()

def load_vector_store() -> FAISS:
    index_path = os.path.join(STORE_PATH, "index.faiss")
    if os.path.exists(index_path):
        return FAISS.load_local(
            folder_path=STORE_PATH,
            embeddings=embedding_model,
            allow_dangerous_deserialization=True 
        )

    else:
        # Instead of creating an empty FAISS index, we return None
        return None


def save_vector_store(store: FAISS):
    store.save_local(STORE_PATH)
