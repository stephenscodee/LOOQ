import torch
from PIL import Image
from transformers import CLIPProcessor, CLIPModel
import numpy as np

from app.domain.entities.garment import GarmentPrediction, GarmentCategory
from app.services.outfits import OutfitService
from app.services.vector_search import VectorSearchService
from app.core.config import settings
from sqlalchemy.orm import Session

class RecognitionService:
    def __init__(self, db: Session = None):
        # We will initialize the models here. 
        # Using CLIP as the primary feature extractor.
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.model = CLIPModel.from_pretrained(settings.CLIP_MODEL_NAME).to(self.device)
        self.processor = CLIPProcessor.from_pretrained(settings.CLIP_MODEL_NAME)
        self.outfit_service = OutfitService()
        self.vector_search = VectorSearchService(db) if db else None

    async def recognize(self, image: Image.Image) -> GarmentPrediction:
        # 1. Extract features using CLIP
        inputs = self.processor(images=image, return_tensors="pt").to(self.device)
        with torch.no_grad():
            image_features = self.model.get_image_features(**inputs)
        
        # Normalize features
        image_features /= image_features.norm(p=2, dim=-1, keepdim=True)
        features_list = image_features.cpu().numpy().tolist()[0]
        
        # 2. Classify (currently mock)
        category = GarmentCategory.SHIRT
        
        # 3. Get outfits and similar products
        outfits = await self.outfit_service.get_recommended_outfits(category.value, {"features": features_list})
        
        similar_products = []
        if self.vector_search:
            similar_products_objs = self.vector_search.find_similar_products(features_list)
            similar_products = [
                {"name": p.name, "price": p.price, "image_url": p.image_url} 
                for p in similar_products_objs
            ]
        else:
            # Fallback to mocks if no DB
            similar_products = [
                {"name": "Similar Shirt 1", "price": 45.00, "image_url": "https://via.placeholder.com/150"},
                {"name": "Similar Shirt 2", "price": 38.50, "image_url": "https://via.placeholder.com/150"}
            ]
        
        return GarmentPrediction(
            category=category,
            confidence=0.95,
            attributes={"features_extracted": True},
            outfits=outfits,
            similar_products=similar_products
        )
