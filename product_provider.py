"""Base class for product providers"""

from abc import ABC, abstractmethod
from typing import List
from app.domain.entities.product import Product as ProductEntity
from app.domain.entities.garment import GarmentPrediction


class ProductProvider(ABC):
    """Abstract base class for e-commerce product providers"""
    
    @abstractmethod
    async def search_products(
        self, 
        prediction: GarmentPrediction,
        limit: int = 20
    ) -> List[ProductEntity]:
        """
        Search for products based on garment prediction
        
        Args:
            prediction: Garment recognition prediction
            limit: Maximum number of results
            
        Returns:
            List of Product entities
        """
        pass
    
    @abstractmethod
    async def get_product(self, product_id: str) -> ProductEntity:
        """
        Get product details by ID
        
        Args:
            product_id: Product identifier
            
        Returns:
            Product entity
        """
        pass

