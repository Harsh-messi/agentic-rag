def generate_answer(query, route, retrieved_chunks, llm_call):

    if route == "out_of_scope":
        return "Information not available in the provided documents."

    context = "\n\n".join([c["text"] for c in retrieved_chunks])

    if route == "factual":
        prompt = f"""
Answer ONLY using the context below.

Context:
{context}

Question: {query}
"""

    elif route == "synthesis":
        prompt = f"""
You are an AI assistant. Combine and synthesize information.

Context:
{context}

Question: {query}
"""

    return llm_call(prompt)