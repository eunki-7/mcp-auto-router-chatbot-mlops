"""
Initialize FAISS vector store with sample FAQ-like content.
This is just a sample for demonstration purposes.
"""

import os
import numpy as np
import faiss
from sentence_transformers import SentenceTransformer

# Sample FAQ content
docs = [
    "How to reset my password?",
    "What is the refund policy?",
    "How to contact customer support?",
    "What are the working hours?",
    "How to delete my account?"
]

# Load embedding model (CPU only)
model = SentenceTransformer("all-MiniLM-L6-v2")

# Create embeddings
embeddings = model.encode(docs)

# Create FAISS index
dim = embeddings.shape[1]
index = faiss.IndexFlatL2(dim)
index.add(np.array(embeddings))

# Save index
os.makedirs("data/processed", exist_ok=True)
faiss.write_index(index, "data/processed/faiss_index.bin")

# Save documents as metadata
with open("data/processed/docs.txt", "w") as f:
    for doc in docs:
        f.write(doc + "\n")

print("FAISS vector store initialized and saved to data/processed/")
