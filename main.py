from ingestion import load_all_docs
from vectorstore import VectorStore
from router import route_query
from rag import generate_answer
from llm import llm_call


def build_system():
    print("\n📦 Loading documents from /data ...")

    chunks = load_all_docs("data")

    print(f"✅ Total chunks loaded: {len(chunks)}")

    print("\n🧠 Building vector database...")

    db = VectorStore()
    db.build(chunks)

    print("✅ System ready!\n")

    return db


def ask_question(db, query):
    print("\n" + "-" * 60)
    print("❓ Question:", query)

    # Step 1: Retrieve relevant chunks
    retrieved = db.search(query)

    # Step 2: Route query (Agent decision)
    route = route_query(query, retrieved)

    print("🧭 Route:", route)

    # Step 3: Generate answer
    answer = generate_answer(query, route, retrieved, llm_call)

    print("\n💡 Answer:\n")
    print(answer)

    print("\n" + "-" * 60)

    return {
        "query": query,
        "route": route,
        "answer": answer
    }


def main():
    db = build_system()

    while True:
        query = input("\nAsk a question (type 'exit' to quit): ")

        if query.lower() == "exit":
            print("\n👋 Exiting system. Goodbye!")
            break

        ask_question(db, query)


if __name__ == "__main__":
    main()