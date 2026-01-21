import os
from dotenv import load_dotenv
from langchain_core.runnables import RunnablePassthrough
from langchain_google_genai import ChatGoogleGenerativeAI

from app.rag.retriever import build_clinical_retriever
from app.rag.prompts import PRESCRIPTION_VALIDATION_PROMPT

load_dotenv() 
def create_prescription_rag(db):
    retriever = build_clinical_retriever(db)

    llm = ChatGoogleGenerativeAI(
        model=os.environ.get("GEMINI_MODEL", "gemini-2.0-flash-exp"),
        temperature=float(os.environ.get("TEMPERATURE", 0.1)),
    )

    rag_pipeline = (
        {
            "context": retriever,
            "prescription": RunnablePassthrough(),
        }
        | PRESCRIPTION_VALIDATION_PROMPT
        | llm
    )

    return rag_pipeline
