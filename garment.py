from sqlalchemy import Column, String, Float, JSON, DateTime, ForeignKey, UUID
from sqlalchemy.orm import declarative_base
from sqlalchemy.sql import func
import uuid
from pgvector.sqlalchemy import Vector

Base = declarative_base()

class Garment(Base):
    __tablename__ = "garments"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), index=True)
    image_url = Column(String, nullable=False)
    category = Column(String, nullable=False)
    attributes = Column(JSON)
    embedding = Column(Vector(512))  # Matches CLIP embedding dimension
    created_at = Column(DateTime, server_default=func.now())

class Product(Base):
    __tablename__ = "products"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    provider = Column(String, nullable=False)
    external_id = Column(String, nullable=False, unique=True)
    name = Column(String, nullable=False)
    price = Column(Float)
    currency = Column(String(3))
    image_url = Column(String)
    affiliate_link = Column(String)
    metadata_json = Column(JSON)
    embedding = Column(Vector(512))
    created_at = Column(DateTime, server_default=func.now())
