from vector_store import load_vector_store

def ask(question: str):
    db = load_vector_store()
    results = db.similarity_search(question, k=3)

    print("\n🔍 Question:", question)
    print("\n📄 Retrieved Context:\n")

    for i, doc in enumerate(results, 1):
        print(f"{i}. {doc.page_content}")

if __name__ == "__main__":
    while True:
        q = input("\nAsk a question (or 'exit'): ")
        if q.lower() == "exit":
            break
        ask(q)