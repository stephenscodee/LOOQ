from typing import List, Dict

class OutfitService:
    def __init__(self):
        # Basic rules: category -> list of compatible categories
        self.rules = {
            "top": ["pants", "shorts", "skirts"],
            "shirt": ["trousers", "jeans"],
            "t-shirt": ["shorts", "jeans", "joggers"],
            "pants": ["shirt", "t-shirt", "sweater"],
        }
        
        # Color harmony rules (very basic)
        self.color_rules = {
            "white": ["black", "blue", "grey", "navy"],
            "black": ["white", "grey", "red", "beige"],
            "blue": ["white", "grey", "beige"],
        }

    async def get_recommended_outfits(self, category: str, attributes: Dict) -> List[Dict]:
        # Anchor item category
        anchors = self.rules.get(category, ["pants"])
        
        # Mocking some products for the outfit
        outfits = []
        for anchor in anchors:
            outfits.append({
                "name": f"Classic {anchor}",
                "items": [
                    {"category": anchor, "name": f"Suggested {anchor}", "price": 29.99},
                    {"category": "shoes", "name": "Basic Sneakers", "price": 59.99}
                ]
            })
        
        return outfits
