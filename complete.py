"""
Complete workflow endpoint
Recognizes garment, finds products, and generates outfits in one call
"""

from fastapi import APIRouter, UploadFile, File, HTTPException
from PIL import Image
import io
from typing import Dict, Any
from loguru import logger

from app.domain.entities.garment import GarmentPrediction
from app.infrastructure.ml.recognition import GarmentRecognitionService
from app.infrastructure.external_apis.aggregator import ProductAggregator
from app.domain.services.outfit_engine import OutfitRecommendationEngine
from app.core.config import settings

router = APIRouter()

recognition_service = GarmentRecognitionService()
product_aggregator = ProductAggregator()
outfit_engine = OutfitRecommendationEngine()


@router.post("/analyze")
async def complete_analysis(file: UploadFile = File(...)) -> Dict[str, Any]:
    """
    Complete analysis: recognize garment, find products, and generate outfits
    
    This is the main endpoint for the mobile app - one call does everything!
    
    Args:
        file: Image file
        
    Returns:
        Dictionary with:
        - prediction: GarmentPrediction
        - products: List of similar products
        - outfits: List of outfit recommendations
    """
    try:
        # 1. Validate and load image
        if file.content_type not in settings.ALLOWED_IMAGE_TYPES:
            raise HTTPException(
                status_code=400,
                detail=f"Unsupported image type: {file.content_type}"
            )
        
        contents = await file.read()
        if len(contents) > settings.MAX_IMAGE_SIZE:
            raise HTTPException(
                status_code=400,
                detail=f"Image too large. Max: {settings.MAX_IMAGE_SIZE / 1024 / 1024}MB"
            )
        
        image = Image.open(io.BytesIO(contents))
        
        # 2. Recognize garment
        prediction = await recognition_service.recognize(image)
        logger.info(f"Recognized: {prediction.category} (confidence: {prediction.confidence:.2f})")
        
        # 3. Search for products
        products = await product_aggregator.search_products(
            prediction,
            limit=settings.SIMILAR_PRODUCTS_LIMIT
        )
        logger.info(f"Found {len(products)} products")
        
        # 4. Generate outfits (using first product as anchor)
        outfits = []
        if products:
            anchor = products[0]
            outfits = await outfit_engine.generate_outfits(
                anchor_item=anchor,
                prediction=prediction,
                available_products=products,
                limit=settings.MAX_OUTFITS_PER_ITEM
            )
            logger.info(f"Generated {len(outfits)} outfits")
        
        # 5. Return complete result
        return {
            "prediction": prediction.model_dump(),
            "products": [p.model_dump() for p in products],
            "outfits": [o.model_dump() for o in outfits]
        }
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error in complete analysis: {e}")
        raise HTTPException(status_code=500, detail=f"Error processing image: {str(e)}")
