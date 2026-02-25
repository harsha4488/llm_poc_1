# llm_poc_1
LLM RAG PROOF OF CONCEPT (SINGLE FILE)

This project is a minimal Proof of Concept (PoC) for a Retrieval-Augmented
Generation (RAG) system using local embeddings and a vector database.

The goal of this project is to demonstrate the core building blocks of an
LLM-powered system without relying on external APIs or cloud services.


WHAT THIS PROJECT DOES
----------------------
- Loads text documents from a local folder
- Splits text into smaller overlapping chunks
- Converts text chunks into vector embeddings (offline)
- Stores embeddings in a FAISS vector index
- Retrieves relevant context using semantic similarity search
- Allows interactive querying from the terminal


WHY THIS PROJECT
----------------
This PoC focuses on the retrieval layer, which is the most critical and reusable
part of modern LLM applications. The retrieval pipeline can later be connected
to any LLM (OpenAI, Azure OpenAI, Llama, etc.).

The project is intentionally:
- Offline-first
- Simple
- Easy to explain in interviews
- Easy to extend into a production system


TECH STACK
----------
- Python 3.11 (recommended)
- LangChain (modular packages)
- FAISS (vector database)
- Sentence Transformers (all-MiniLM-L6-v2)
- Local execution (no API keys required)


PROJECT STRUCTURE
-----------------
rag_poc.py        -> Single Python file containing all logic
data/
  faq.txt         -> Sample text documents


PREREQUISITES
-------------
- macOS or Linux
- Python 3.11 installed

IMPORTANT:
LLM frameworks are not yet compatible with Python 3.14+. Use Python 3.11.


SETUP INSTRUCTIONS
------------------
1. Create a Python 3.11 virtual environment:

   python3.11 -m venv .venv
   source .venv/bin/activate

2. Install dependencies:

   pip install langchain langchain-community langchain-text-splitters \
               langchain-huggingface sentence-transformers faiss-cpu

3. Create a data folder and add text files:

   mkdir data

   Example data/faq.txt:
   Refunds are processed within 5 business days.
   Orders are shipped within 48 hours.
   Customer support is available Monday to Friday.


RUNNING THE PROJECT
-------------------
Run the application:

   python rag_poc.py

The first run will:
- Build the FAISS vector store
- Save it locally

You can then ask questions interactively:

   Question: how long for refund?


HOW IT WORKS (HIGH LEVEL)
------------------------
1. Documents are loaded from disk
2. Text is split into overlapping chunks
3. Each chunk is converted into an embedding
4. Embeddings are stored in FAISS
5. User queries are embedded and matched using similarity search


EXTENSIONS (FUTURE WORK)
-----------------------
This PoC can be extended with:
- LLM-based answer generation
- Planner–Executor agents
- Confidence scoring and fallback logic
- FastAPI REST endpoints
- Dockerized deployment
- Cloud document ingestion (S3, GCS, etc.)


TALKING POINT
-----------------------
"This project demonstrates a clean RAG retrieval pipeline using local
embeddings and FAISS. The retrieval layer is model-agnostic and can be reused
across different LLMs and deployment environments."


