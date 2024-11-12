import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
from typing import List

class DocumentRetriever:
    """Class for managing document retrieval using FAISS and Sentence Transformers."""

    def __init__(self):
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        self.index = faiss.IndexFlatL2(384)  # Dimension based on model output
        self.embeddings = []
        self.documents = []

    def add_documents(self, documents: List[str]):
        """Add documents to the FAISS index."""
        for doc in documents:
            embedding = self.model.encode([doc])[0]
            self.embeddings.append(embedding)
            self.documents.append(doc)
        self.index.add(np.array(self.embeddings))

    def retrieve(self, query: str) -> str:
        """Retrieve the most relevant document for a given query."""
        query_vector = self.model.encode([query])[0]
        distances, indices = self.index.search(np.array([query_vector]), k=1)
        return self.documents[indices[0][0]]
