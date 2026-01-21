import os
import getpass
from dotenv import load_dotenv
from langchain_community.vectorstores import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_core.documents import Document
from app.models.Drug import Drug

load_dotenv()

CHROMA_DIR = "app/vectorstore/chroma"
COLLECTION_NAME = "clinical_drugs"
DEFAULT_EMBEDDING_MODEL = "models/embedding-001"  


def build_clinical_retriever(db):
    """
    Builds a context-aware retriever for clinical drugs using ChromaDB and Google Generative AI embeddings.

    Steps:
    1. Ensures GOOGLE_API_KEY is loaded.
    2. Initializes embedding function.
    3. Loads existing Chroma vectorstore if valid.
    4. Builds vectorstore from database if missing or invalid.
    5. Returns a retriever for RAG queries (top k results).
    """

    
    GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY")
    if not GOOGLE_API_KEY:
        GOOGLE_API_KEY = getpass.getpass("Enter your Google AI API key: ").strip()
        if not GOOGLE_API_KEY:
            raise RuntimeError("Missing GOOGLE_API_KEY. Cannot proceed.")
        os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY
    print("GOOGLE_API_KEY being used:", os.environ.get("GOOGLE_API_KEY"))
    
    try:
        embeddings = GoogleGenerativeAIEmbeddings(model=DEFAULT_EMBEDDING_MODEL)
        test_vec = embeddings.embed_query("test")
        if not test_vec or len(test_vec) == 0:
            raise RuntimeError("Embedding function failed. Check API key and model.")
    except Exception as e:
        raise RuntimeError(f"Failed to initialize embeddings: {e}")

   
    if os.path.exists(CHROMA_DIR) and os.listdir(CHROMA_DIR):
        try:
            vectorstore = Chroma(
                collection_name=COLLECTION_NAME,
                embedding_function=embeddings,
                persist_directory=CHROMA_DIR,
            )
            return vectorstore.as_retriever(search_kwargs={"k": 3})
        except Exception as e:
            print(f"Failed to load existing Chroma vectorstore: {e}. Rebuilding from DB...")

    chunk_size = 50  # Number of drugs to fetch per DB iteration  (instead feach all at once)
    docs = []
    # Use iterator for memory-efficient fetching
    drug_iterator = Drug.objects.all().iterator(chunk_size=chunk_size)
    has_drugs = False

    for drug in drug_iterator:
        has_drugs = True
        chunk_drug = f"""
    Drug Name: {drug.name}
    Description: {drug.description}
    Dosage Range: {drug.dosage_min}-{drug.dosage_max} {drug.dosage_unit}
    Side Effects: {drug.side_effects}
    Precautions: {drug.precautions}
    Interactions: {drug.interactions}
    """
        docs.append(Document(page_content=chunk_drug))

    if not has_drugs:
        raise RuntimeError("Clinical drug database is empty. Cannot build RAG index.")
    # Build the vector store
    
    vectorstore = Chroma.from_documents(
        documents=docs,
        embedding=embeddings,
        collection_name=COLLECTION_NAME,
        persist_directory=CHROMA_DIR,
    )
   
    vectorstore.persist()
    return vectorstore.as_retriever(search_kwargs={"k": 3})
