"""Application configuration settings"""

from pydantic_settings import BaseSettings
from typing import List


class Settings(BaseSettings):
    """Application settings"""
    
    # App
    APP_NAME: str = "LOOQ API"
    ENVIRONMENT: str = "development"
    SECRET_KEY: str = "change-me-in-production"
    DEBUG: bool = True
    
    # Database
    DATABASE_URL: str = "postgresql://looq_user:looq_pass@localhost:5432/looq_db"
    
    # Redis
    REDIS_URL: str = "redis://localhost:6379/0"
    REDIS_CACHE_TTL: int = 3600  # 1 hour
    
    # CORS
    CORS_ORIGINS: List[str] = [
        "http://localhost:3000",
        "http://localhost:8080",
        "http://127.0.0.1:8080",
        "http://localhost:8000",
    ]
    
    # ML Models
    MODEL_CACHE_DIR: str = "./models"
    CLIP_MODEL_NAME: str = "sentence-transformers/clip-ViT-B-32"
    RECOGNITION_MODEL_PATH: str = "./models/fashion_classifier.pt"
    
    # E-commerce APIs
    AMAZON_ACCESS_KEY: str = ""
    AMAZON_SECRET_KEY: str = ""
    AMAZON_ASSOCIATE_TAG: str = ""
    ZALANDO_API_KEY: str = ""
    
    # Image processing
    MAX_IMAGE_SIZE: int = 10 * 1024 * 1024  # 10MB
    ALLOWED_IMAGE_TYPES: List[str] = ["image/jpeg", "image/png", "image/webp"]
    
    # Outfit recommendations
    MAX_OUTFITS_PER_ITEM: int = 10
    SIMILAR_PRODUCTS_LIMIT: int = 20
    
    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()

