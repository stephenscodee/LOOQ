"""
Outfit Recommendation Engine
Generates outfit combinations based on style rules (MVP: basic rules)
"""

from typing import List
from loguru import logger
from decimal import Decimal

from app.domain.entities.product import Product as ProductEntity
from app.domain.entities.outfit import OutfitRecommendation, OutfitItem
from app.domain.entities.garment import GarmentPrediction
import uuid


class OutfitRecommendationEngine:
    """Engine for generating outfit recommendations"""
    
    def __init__(self):
        """Initialize outfit recommendation engine"""
        logger.info("Initialized OutfitRecommendationEngine")
        self._style_rules = StyleRuleEngine()
    
    async def generate_outfits(
        self,
        anchor_item: ProductEntity,
        prediction: GarmentPrediction,
        available_products: List[ProductEntity],
        limit: int = 10
    ) -> List[OutfitRecommendation]:
        """
        Generate outfit recommendations
        
        Args:
            anchor_item: The main item to build outfit around
            prediction: Garment prediction for the anchor
            available_products: List of available products to combine
            limit: Max number of outfits to generate
            
        Returns:
            List of outfit recommendations
        """
        logger.info(f"Generating outfits for {anchor_item.category}")
        
        # MVP: Simple rule-based outfit generation
        # Filter compatible items
        compatible_items = self._filter_compatible_items(
            anchor_item, 
            prediction,
            available_products
        )
        
        # Generate combinations
        outfits = []
        for combo in self._generate_basic_combinations(anchor_item, compatible_items, limit):
            outfit = OutfitRecommendation(
                id=uuid.uuid4(),
                items=[OutfitItem(
                    id=item.id,
                    name=item.name,
                    image_url=item.image_url,
                    price=item.price,
                    product_url=item.product_url
                ) for item in combo],
                occasion="casual",
                season=self._current_season(),
                total_price=sum(item.price or Decimal(0) for item in combo),
                compatibility_score=0.8,  # MVP: fixed score
                description=self._generate_outfit_description(combo)
            )
            outfits.append(outfit)
        
        return outfits[:limit]
    
    def _filter_compatible_items(
        self,
        anchor: ProductEntity,
        prediction: GarmentPrediction,
        products: List[ProductEntity]
    ) -> List[ProductEntity]:
        """Filter products compatible with anchor item"""
        compatible = []
        
        for product in products:
            # Skip the anchor itself
            if product.id == anchor.id:
                continue
            
            # MVP: Basic compatibility rules
            # Tops go with bottoms (jeans, pants, shorts)
            if anchor.category in ["shirt", "t-shirt", "blouse", "sweater", "hoodie"]:
                if product.category in ["jeans", "pants", "shorts"]:
                    compatible.append(product)
                # Also compatible with shoes
                elif product.category in ["sneakers", "shoes", "boots"]:
                    compatible.append(product)
        
        return compatible
    
    def _generate_basic_combinations(
        self,
        anchor: ProductEntity,
        compatible: List[ProductEntity],
        limit: int
    ) -> List[List[ProductEntity]]:
        """Generate basic outfit combinations"""
        combinations = []
        
        # Separate by category
        bottoms = [p for p in compatible if p.category in ["jeans", "pants", "shorts"]]
        shoes = [p for p in compatible if p.category in ["sneakers", "shoes", "boots"]]
        
        # Generate combinations: anchor + bottom + shoe
        for bottom in bottoms[:3]:  # Max 3 bottoms
            for shoe in shoes[:3]:  # Max 3 shoes
                combinations.append([anchor, bottom, shoe])
                if len(combinations) >= limit:
                    return combinations
        
        # If not enough combinations, add simpler ones
        for bottom in bottoms[:limit]:
            combinations.append([anchor, bottom])
            if len(combinations) >= limit:
                break
        
        return combinations[:limit]
    
    def _generate_outfit_description(self, items: List[ProductEntity]) -> str:
        """Generate a description for the outfit"""
        categories = [item.category for item in items]
        return f"Complete look with {', '.join(set(categories))}"
    
    def _current_season(self) -> str:
        """Get current season (simplified)"""
        from datetime import datetime
        month = datetime.now().month
        if month in [12, 1, 2]:
            return "winter"
        elif month in [3, 4, 5]:
            return "spring"
        elif month in [6, 7, 8]:
            return "summer"
        else:
            return "fall"


class StyleRuleEngine:
    """Basic style rule engine (placeholder for future ML-based rules)"""
    
    def __init__(self):
        """Initialize style rules"""
        # MVP: Empty, rules are hardcoded in outfit engine
        pass

