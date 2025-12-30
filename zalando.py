"""Zalando API integration"""

from typing import List
from loguru import logger

from app.domain.entities.product import Product as ProductEntity
from app.domain.entities.garment import GarmentPrediction
from app.infrastructure.external_apis.product_provider import ProductProvider
from app.core.config import settings
import uuid


class ZalandoProvider(ProductProvider):
    """Zalando API provider"""
    
    def __init__(self):
        """Initialize Zalando provider"""
        self.api_key = settings.ZALANDO_API_KEY
        
        if not self.api_key:
            logger.warning("Zalando API key not configured - provider will return mock data")
            self._mock_mode = True
        else:
            self._mock_mode = False
            # TODO: Initialize Zalando API client
    
    async def search_products(
        self, 
        prediction: GarmentPrediction,
        limit: int = 20
    ) -> List[ProductEntity]:
        """
        Search Zalando products
        
        Args:
            prediction: Garment prediction
            limit: Max results
            
        Returns:
            List of products
        """
        if self._mock_mode:
            return self._mock_search(prediction, limit)
        
        # TODO: Implement actual Zalando API call
        return self._mock_search(prediction, limit)
    
    async def get_product(self, product_id: str) -> ProductEntity:
        """Get product by ID"""
        # TODO: Implement actual API call
        raise NotImplementedError("Zalando product lookup not yet implemented")
    
    def _mock_search(
        self, 
        prediction: GarmentPrediction, 
        limit: int
    ) -> List[ProductEntity]:
        """Mock search results for MVP/testing"""
        logger.info(f"Mock Zalando search for {prediction.category}")
        
        mock_products = []
        for i in range(min(limit, 5)):
            product = ProductEntity(
                id=uuid.uuid4(),
                provider="zalando",
                name=f"{prediction.category.value.title()} {prediction.color or 'Style'} - Zalando Mock {i+1}",
                description=f"Trendy {prediction.category.value} from Zalando",
                price=39.99 + (i * 15),
                currency="EUR",
                image_url=f"https://via.placeholder.com/300?text=Zalando+{prediction.category.value}",
                product_url=f"https://zalando.com/mock-product-{i+1}",
                category=prediction.category.value,
                attributes={
                    "color": prediction.color,
                    "pattern": prediction.pattern,
                    "brand": f"Brand{i+1}"
                }
            )
            mock_products.append(product)
        
        return mock_products

