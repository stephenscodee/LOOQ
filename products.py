"""Products endpoints"""

from fastapi import APIRouter, HTTPException
from typing import List
from loguru import logger

from app.domain.entities.product import Product as ProductEntity
from app.domain.entities.garment import GarmentPrediction, GarmentCategory
from app.infrastructure.external_apis.aggregator import ProductAggregator
from app.core.config import settings

router = APIRouter()
aggregator = ProductAggregator()


@router.post("/search", response_model=List[ProductEntity])
async def search_products(prediction: GarmentPrediction):
    """
    Search for products based on garment prediction
    
    Args:
        prediction: Garment recognition prediction
        
    Returns:
        List of products from various e-commerce providers
    """
    try:
        # Validate category for MVP (tops only)
        if prediction.category not in [
            GarmentCategory.SHIRT,
            GarmentCategory.T_SHIRT,
            GarmentCategory.BLOUSE,
            GarmentCategory.TANK_TOP,
            GarmentCategory.SWEATER,
            GarmentCategory.HOODIE,
        ]:
            raise HTTPException(
                status_code=400,
                detail=f"Category {prediction.category} not supported in MVP. Only tops are supported."
            )
        
        # Search products
        products = await aggregator.search_products(
            prediction,
            limit=settings.SIMILAR_PRODUCTS_LIMIT
        )
        
        logger.info(f"Found {len(products)} products for category {prediction.category}")
        
        return products
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error searching products: {e}")
        raise HTTPException(status_code=500, detail=f"Error searching products: {str(e)}")

