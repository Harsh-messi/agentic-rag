import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from embeddings import get_embedding
from router import route_query
from rag import generate_answer
from llm import llm_call
from ingestion import load_all_docs
from vectorstore import VectorStore


# ---------- TEST SET ----------
test_set = [
    # Factual
    {"question": "What is AI regulation in the EU?", "type": "factual", "expected_route": "factual", "expected": "EU AI Act regulates AI systems"},
    {"question": "What is the purpose of AI laws?", "type": "factual", "expected_route": "factual", "expected": "Ensure safe AI usage"},
    {"question": "What are high-risk AI systems?", "type": "factual", "expected_route": "factual", "expected": "Systems with high impact"},
    {"question": "What does AI Act focus on?", "type": "factual", "expected_route": "factual", "expected": "Regulation of AI usage"},
    {"question": "What is AI governance?", "type": "factual", "expected_route": "factual", "expected": "Rules for AI systems"},

    # Synthesis
    {"question": "Compare AI regulations across countries", "type": "synthesis", "expected_route": "synthesis", "expected": "Different countries have different approaches"},
    {"question": "Summarize AI policies globally", "type": "synthesis", "expected_route": "synthesis", "expected": "Global policies vary"},
    {"question": "What are similarities in AI laws?", "type": "synthesis", "expected_route": "synthesis", "expected": "Common goals include safety"},
    {"question": "How do regions manage AI risk?", "type": "synthesis", "expected_route": "synthesis", "expected": "Risk-based approach"},
    {"question": "Analyze AI regulation differences", "type": "synthesis", "expected_route": "synthesis", "expected": "Different frameworks exist"},

    # Out of scope
    {"question": "What is quantum computing?", "type": "out_of_scope", "expected_route": "out_of_scope", "expected": "Information not available"},
    {"question": "Who is Elon Musk?", "type": "out_of_scope", "expected_route": "out_of_scope", "expected": "Information not available"},
    {"question": "What is cricket?", "type": "out_of_scope", "expected_route": "out_of_scope", "expected": "Information not available"},
    {"question": "Explain gravity", "type": "out_of_scope", "expected_route": "out_of_scope", "expected": "Information not available"},
    {"question": "What is blockchain?", "type": "out_of_scope", "expected_route": "out_of_scope", "expected": "Information not available"},
]


def evaluate():
    print("🔍 Running evaluation...\n")

    # Build DB
    chunks = load_all_docs("data")
    db = VectorStore()
    db.build(chunks)

    results = []

    correct_routes = 0

    for item in test_set:
        question = item["question"]

        retrieved = db.search(question)
        route = route_query(question, retrieved)
        answer = generate_answer(question, route, retrieved, llm_call)

        # Routing accuracy
        if route == item["expected_route"]:
            correct_routes += 1

        # Similarity score
        sim = cosine_similarity(
            [get_embedding(answer)],
            [get_embedding(item["expected"])]
        )[0][0]

        results.append({
            "question": question,
            "expected_route": item["expected_route"],
            "predicted_route": route,
            "similarity": round(sim, 2),
            "answer": answer[:100]
        })

    df = pd.DataFrame(results)

    print(df)

    print("\n📊 Routing Accuracy:",
          round(correct_routes / len(test_set), 2))

    df.to_csv("results.csv", index=False)

    print("\n✅ Results saved to results.csv")


if __name__ == "__main__":
    evaluate()
