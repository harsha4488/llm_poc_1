from pathlib import Path
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

DATA_DIR = "data"
VECTOR_DIR = "vector_store"

def ingest():
    documents = []

    for file in Path(DATA_DIR).glob("*.txt"):
        loader = TextLoader(str(file))
        documents.extend(loader.load())

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=300,
        chunk_overlap=50
    )
    chunks = splitter.split_documents(documents)

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    db = FAISS.from_documents(chunks, embeddings)
    db.save_local(VECTOR_DIR)

    print("✅ Vector store created successfully")

if __name__ == "__main__":
    ingest()