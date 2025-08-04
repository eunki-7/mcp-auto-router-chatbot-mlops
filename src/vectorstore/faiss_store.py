"""
FAISS Vector Store integration for semantic search.
Stores embeddings and retrieves relevant documents for given queries.
"""
import faiss
import numpy as np
from typing import List, Tuple

class VectorStore:
    def __init__(self, dim: int = 768):
        self.index = faiss.IndexFlatL2(dim)
        self.documents = []

    def add_documents(self, embeddings: np.ndarray, docs: List[str]):
        self.index.add(embeddings)
        self.documents.extend(docs)

    def search(self, query_vector: np.ndarray, top_k: int = 3) -> List[Tuple[str, float]]:
        distances, indices = self.index.search(query_vector, top_k)
        return [(self.documents[i], float(dist)) for i, dist in zip(indices[0], distances[0])]
