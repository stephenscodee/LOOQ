from sqlalchemy.orm import Session
from app.models.garment import Product
from pgvector.sqlalchemy import Vector
from typing import List

class VectorSearchService:
    def __init__(self, db: Session):
        self.db = db

    def find_similar_products(self, query_embedding: List[float], limit: int = 10):
        """
        Find products similar to the query embedding using cosine distance
        """
        # <-> is Euclidean distance, <=> is cosine distance in pgvector
        results = self.db.query(Product).order_by(
            Product.embedding.cosine_distance(query_embedding)
        ).limit(limit).all()
        
        return results
