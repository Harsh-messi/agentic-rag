# Agentic RAG System

## 📌 Overview

This project implements an **Agentic Retrieval-Augmented Generation (RAG)** system that intelligently decides how to answer a query instead of blindly retrieving and generating responses.

The system classifies each query into:

* **Factual** → Direct answer from documents
* **Synthesis** → Combine multiple sources
* **Out-of-Scope** → Decline if information not available

---

## 🏗️ Architecture

```
User Query
   ↓
Query Router (Agent)
   ↓
Vector Store (FAISS)
   ↓
Relevant Chunks Retrieved
   ↓
LLM (Answer Generation)
   ↓
Final Answer
```

### Components:

* **Ingestion Pipeline** → Loads and chunks documents
* **Embeddings** → Converts text into vectors
* **Vector Store** → Stores embeddings (FAISS)
* **Router** → Decides query type
* **RAG Module** → Generates final answer

---

## 📚 Dataset

* 4 documents on **AI Regulation**
* Includes:

  * overlapping information
  * formatting inconsistencies
  * partial contradictions

👉 This ensures realistic retrieval challenges.

---

## ✂️ Chunking Strategy

* **Chunk Size:** ~300–500 words
* **Overlap:** ~50 words

### Why?

* Maintains context continuity
* Improves retrieval accuracy
* Reduces information loss at boundaries

---

## 🧭 Routing Logic (Agentic Behavior)

The system uses **explicit rule-based routing**:

### Factual

* Query asks for definition or direct fact
* Retrieved chunks are highly similar

### Synthesis

* Query contains keywords like:

  * *compare, analyze, summarize, difference*
* Multiple relevant chunks retrieved

### Out-of-Scope

* No relevant chunks found
* Low similarity scores

👉 This ensures **no hallucination** for unknown queries.

---

## 🤖 Answer Generation

* Uses **HuggingFace local model (GPT-2)**
* Generates answers based on retrieved context

### Behavior:

* Factual → concise grounded answer
* Synthesis → combined multi-source response
* Out-of-scope →

  > "Information not available in the provided documents."

---

## 📊 Evaluation Framework

### Test Set:

* 15 total questions:

  * 5 factual
  * 5 synthesis
  * 5 out-of-scope

### Metrics Used:

* **Routing Accuracy**
* **Cosine Similarity (Answer Quality)**

### Example Output:

| Question                     | Expected Route | Predicted Route | Similarity |
| ---------------------------- | -------------- | --------------- | ---------- |
| What is AI regulation in EU? | factual        | factual         | 0.82       |
| Compare AI laws              | synthesis      | synthesis       | 0.75       |
| What is quantum computing?   | out_of_scope   | synthesis       | 0.20       |

---

## 📉 Failure Analysis

### ❌ Failure Case 1: Incorrect Routing

**Query:** Compare AI regulations across countries
**Expected:** synthesis
**Actual:** factual

**Reason:**
Router failed to detect "compare" intent.

**Fix:**
Add keyword-based rules for synthesis detection.

---

### ❌ Failure Case 2: Poor Answer Quality

**Query:** What is AI regulation in the EU?

**Reason:**
Free LLM (GPT-2) has limited reasoning capability.

**Fix:**
Use stronger model (GPT-4 / better HF models).

---

### ❌ Failure Case 3: Out-of-Scope Misclassification

**Query:** What is quantum computing?

**Reason:**
Retriever returned loosely related chunks.

**Fix:**
Add similarity threshold to filter irrelevant results.

---

## 🚀 How to Run

### 1. Install dependencies

```
pip install -r requirements.txt
```

### 2. Run main system

```
python main.py
```

### 3. Run evaluation

```
python evaluation.py
```

---

## 📁 Project Structure

```
agentic-rag/
├── data/
├── ingestion.py
├── embeddings.py
├── vectorstore.py
├── router.py
├── rag.py
├── evaluation.py
├── main.py
├── requirements.txt
└── README.md
```

---

## 🔒 Notes

* OpenAI API was replaced with **free HuggingFace model** due to quota limitations
* Core RAG pipeline remains unchanged

---

## 💡 Future Improvements

* Use stronger LLM (GPT-4 / Mistral)
* Improve routing with ML classifier
* Handle contradictory information
* Add re-ranking for better retrieval

---

## 🎥 Demo

The demo video shows:

* All 3 query types
* Evaluation pipeline
* One failure case

---

## 🏁 Conclusion

This project demonstrates:

* Agentic decision-making in RAG systems
* Reliable retrieval-based answering
* Robust evaluation and failure analysis

---
