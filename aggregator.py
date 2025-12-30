"""Product aggregator - combines results from multiple providers"""

from typing import List
import asyncio
from loguru import logger

from app.domain.entities.product import Product as ProductEntity
from app.domain.entities.garment import GarmentPrediction
from app.infrastructure.external_apis.product_provider import ProductProvider
from app.infrastructure.external_apis.amazon import AmazonProvider
from app.infrastructure.external_apis.zalando import ZalandoProvider


class ProductAggregator:
    """Aggregates products from multiple e-commerce providers"""
    
    def __init__(self):
        """Initialize aggregator with providers"""
        self.providers: List[ProductProvider] = [
            AmazonProvider(),
            ZalandoProvider(),
        ]
        logger.info(f"Initialized ProductAggregator with {len(self.providers)} providers")
    
    async def search_products(
        self, 
        prediction: GarmentPrediction,
        limit: int = 20
    ) -> List[ProductEntity]:
        """
        Search across all providers and aggregate results
        
        Args:
            prediction: Garment prediction
            limit: Max total results
            
        Returns:
            Aggregated and deduplicated list of products
        """
        # Search all providers in parallel
        tasks = [
            provider.search_products(prediction, limit=limit) 
            for provider in self.providers
        ]
        
        results = await asyncio.gather(*tasks, return_exceptions=True)
        
        # Flatten results and handle errors
        all_products = []
        for result in results:
            if isinstance(result, Exception):
                logger.error(f"Error from provider: {result}")
                continue
            all_products.extend(result)
        
        # Deduplicate (simple approach - by name similarity)
        deduplicated = self._deduplicate_products(all_products)
        
        # Sort by relevance (for MVP: by price or random)
        sorted_products = sorted(deduplicated, key=lambda p: p.price or 999999)
        
        # Return top N
        return sorted_products[:limit]
    
    def _deduplicate_products(self, products: List[ProductEntity]) -> List[ProductEntity]:
        """
        Deduplicate products (simple approach for MVP)
        In production, use more sophisticated similarity matching
        """
        seen = set()
        unique = []
        
        for product in products:
            # Simple dedup by name + provider
            key = (product.name.lower(), product.provider)
            if key not in seen:
                seen.add(key)
                unique.append(product)
        
        return unique

