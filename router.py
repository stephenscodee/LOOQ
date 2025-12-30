"""API v1 router"""

from fastapi import APIRouter

from app.api.v1.endpoints import recognition, products, outfits, complete

api_router = APIRouter()

# Include endpoint routers
api_router.include_router(
    recognition.router,
    prefix="/recognition",
    tags=["recognition"]
)

api_router.include_router(
    products.router,
    prefix="/products",
    tags=["products"]
)

api_router.include_router(
    outfits.router,
    prefix="/outfits",
    tags=["outfits"]
)

api_router.include_router(
    complete.router,
    prefix="/complete",
    tags=["complete"]
)

