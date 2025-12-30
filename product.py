"""Product database model"""

from sqlalchemy import Column, String, DateTime, Numeric, Text, UniqueConstraint
from sqlalchemy.dialects.postgresql import UUID, JSONB
from datetime import datetime
import uuid

from app.infrastructure.database import Base


class Product(Base):
    """Product model - items from e-commerce providers"""
    __tablename__ = "products"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    provider = Column(String(50), nullable=False, index=True)  # amazon, zalando, etc.
    external_id = Column(String(255), nullable=False, index=True)
    name = Column(Text, nullable=False)
    description = Column(Text, nullable=True)
    price = Column(Numeric(10, 2), nullable=True)
    currency = Column(String(3), default="EUR")
    image_url = Column(Text, nullable=False)
    product_url = Column(Text, nullable=False)
    affiliate_link = Column(Text, nullable=True)
    category = Column(String(50), nullable=False, index=True)
    attributes = Column(JSONB, nullable=True)  # brand, color, size, etc.
    metadata = Column(JSONB, nullable=True)  # provider-specific data
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Unique constraint on provider + external_id
    __table_args__ = (
        UniqueConstraint('provider', 'external_id', name='uq_product_provider_external'),
    )
    
    def __repr__(self):
        return f"<Product(id={self.id}, name={self.name[:50]}, provider={self.provider})>"

