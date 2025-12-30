"""Outfit database model"""

from sqlalchemy import Column, String, DateTime, ForeignKey, Float, ARRAY
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from datetime import datetime
import uuid

from app.infrastructure.database import Base


class Outfit(Base):
    """Outfit model - clothing combinations"""
    __tablename__ = "outfits"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=True, index=True)
    items = Column(ARRAY(UUID), nullable=False)  # Array of product/garment IDs
    occasion = Column(String(50), nullable=True)  # casual, formal, party, etc.
    season = Column(String(20), nullable=True)  # spring, summer, fall, winter
    compatibility_score = Column(Float, nullable=True)  # ML-generated score
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    
    # Relationships
    user = relationship("User", backref="outfits")
    
    def __repr__(self):
        return f"<Outfit(id={self.id}, items_count={len(self.items) if self.items else 0})>"

