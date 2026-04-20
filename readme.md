Failure Case 1: Incorrect Routing

Query:
“Compare AI regulations across countries”

Expected Route:
synthesis

Actual Route:
factual

Issue:
The system classified a synthesis query as factual.

Why it failed:
The router relies heavily on keyword matching and failed to detect that “compare” implies combining multiple sources.

Improvement:
Enhance routing logic by:

adding keyword rules (compare, analyze, difference → synthesis)
checking number of retrieved chunks
using similarity diversity across chunks


Case 2: Poor Answer Quality

Query:
“What is AI regulation in the EU?”

Expected:
Clear explanation of EU AI Act

Actual:
Generic or incomplete answer

Issue:
Answer lacked depth and accuracy.

Why it failed:
The free LLM (GPT-2 / small model) has limited reasoning ability and cannot fully utilize retrieved context.

Improvement:

Use stronger LLM (GPT-4 / better HF model)
Improve prompt engineering
Add structured context formatting


Failure Case 3: Wrong Out-of-Scope Detection

Query:
“What is quantum computing?”

Expected Route:
out_of_scope

Actual Route:
synthesis

Issue:
System attempted to answer an unrelated query.

Why it failed:
The retriever returned loosely related chunks due to embedding similarity noise.

Improvement:

Add similarity threshold (if score < threshold → out_of_scope)
Check if retrieved content is actually relevant
Add fallback rule for unknown topics




These failures highlight limitations in routing heuristics, retrieval quality, and LLM capability. Future improvements would focus on hybrid routing, better embeddings, and stronger language models