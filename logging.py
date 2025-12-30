"""Logging configuration"""

from loguru import logger
import sys


def setup_logging():
    """Configure application logging"""
    logger.remove()  # Remove default handler
    
    # Add console handler with custom format
    logger.add(
        sys.stdout,
        format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan> - <level>{message}</level>",
        level="DEBUG",
        colorize=True,
    )
    
    # Add file handler for production
    logger.add(
        "logs/app_{time:YYYY-MM-DD}.log",
        rotation="00:00",
        retention="30 days",
        level="INFO",
        format="{time:YYYY-MM-DD HH:mm:ss} | {level: <8} | {name}:{function} - {message}",
    )
    
    logger.info("Logging configured successfully")

