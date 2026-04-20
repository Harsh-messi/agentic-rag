def route_query(query, retrieved_chunks):
    q = query.lower()

    synthesis_keywords = [
        "compare", "difference", "contrast",
        "analyze", "combine", "summary", "summarize"
    ]

    # If no chunks retrieved → out of scope
    if not retrieved_chunks:
        return "out_of_scope"

    # If user asks comparison → synthesis
    if any(word in q for word in synthesis_keywords):
        return "synthesis"

    # If multiple sources → synthesis
    sources = set([c["source"] for c in retrieved_chunks])
    if len(sources) > 1:
        return "synthesis"

    return "factual"