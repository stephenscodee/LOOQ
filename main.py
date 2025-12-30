"""
LOOQ Backend - Main Application Entry Point
FastAPI application for fashion recognition and outfit recommendations
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from contextlib import asynccontextmanager
import uvicorn

from app.core.config import settings
from app.core.logging import setup_logging
from app.api.v1.router import api_router
from app.infrastructure.database import init_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Lifespan context manager for startup and shutdown events"""
    # Startup
    setup_logging()
    await init_db()
    yield
    # Shutdown
    # Any cleanup code here


# Create FastAPI app
app = FastAPI(
    title="Fashion AI API",
    description="API for garment recognition and outfit recommendations",
    version="0.1.0",
    lifespan=lifespan,
    docs_url="/docs",
    redoc_url="/redoc",
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API router
app.include_router(api_router, prefix="/api/v1")


@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "message": "LOOQ API - Fashion Recognition & Shopping",
        "version": "1.0.0",
        "docs": "/docs"
    }


@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return JSONResponse(
        content={"status": "healthy", "service": "looq-api"},
        status_code=200
    )


if __name__ == "__main__":
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=settings.ENVIRONMENT == "development"
    )
