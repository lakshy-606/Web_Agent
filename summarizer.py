# summarizer.py

from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda, RunnableParallel
from typing import List
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(temperature=0.3)

SUMMARY_PROMPT = PromptTemplate(
    input_variables=["context", "question"],
    template =
    """
    You are a helpful AI assistant.

    Given the following web search results, answer the question as accurately and concisely as possible.

    Context:{context}

    Question:{question}

    Only answer if relevant information is found. If not, say "I don't know."
    """
)

def summarize_texts(question: str, documents: List[str]) -> str:
    context = "\n\n".join(documents[:5])  # Limit to top 5 pages to avoid overload

    chain = (
        RunnableParallel({
            "context": RunnableLambda(lambda _: context),
            "question": RunnableLambda(lambda _: question)
        })
        | SUMMARY_PROMPT
        | llm
        | StrOutputParser()
    )

    return chain.invoke({})
