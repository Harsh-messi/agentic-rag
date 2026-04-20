import faiss
import numpy as np
from embeddings import get_embedding


class VectorStore:
    def __init__(self):
        self.index = None
        self.texts = []
        self.sources = []

    def build(self, chunks):
        embeddings = []

        for c in chunks:
            emb = get_embedding(c["text"])
            embeddings.append(emb)

            self.texts.append(c["text"])
            self.sources.append(c["source"])

        embeddings = np.array(embeddings).astype("float32")

        dim = embeddings.shape[1]
        self.index = faiss.IndexFlatL2(dim)
        self.index.add(embeddings)

    def search(self, query, k=3):
        q_emb = np.array([get_embedding(query)]).astype("float32")

        distances, indices = self.index.search(q_emb, k)

        results = []
        for i in indices[0]:
            results.append({
                "text": self.texts[i],
                "source": self.sources[i]
            })

        return results