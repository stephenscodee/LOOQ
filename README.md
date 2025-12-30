# LOOQ Backend

FastAPI backend for fashion recognition and outfit recommendations.

## Features

- 🎯 Garment recognition (MVP: tops only)
- 🛍️ Product search from multiple e-commerce providers
- 👔 Outfit recommendation engine
- 🚀 Fast, async API with FastAPI
- 📊 PostgreSQL database with pgvector
- 🔄 Redis caching
- 📝 OpenAPI/Swagger documentation

## Quick Start

### 1. Setup Environment

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Configure Environment

Copy `.env.example` to `.env` and configure:

```bash
cp .env.example .env
# Edit .env with your settings
```

### 3. Start Services

Using Docker Compose (recommended):
```bash
docker-compose up -d postgres redis
```

Or manually start PostgreSQL and Redis.

### 4. Run Database Migrations

```bash
alembic upgrade head
```

### 5. Start Server

```bash
uvicorn app.main:app --reload
```

Visit:
- API: http://localhost:8000
- Docs: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Project Structure

```
app/
├── api/              # API endpoints
│   └── v1/
│       ├── endpoints/  # Route handlers
│       └── router.py   # Router configuration
├── core/             # Core configuration
│   ├── config.py      # Settings
│   └── logging.py     # Logging setup
├── domain/           # Business logic
│   ├── entities/      # Domain entities
│   └── services/      # Domain services
└── infrastructure/   # External integrations
    ├── database/      # Database models & session
    ├── ml/            # ML models & services
    └── external_apis/ # E-commerce APIs
```

## API Endpoints

### Main Endpoint

**POST** `/api/v1/complete/analyze`

Upload an image and get:
- Garment recognition
- Similar products
- Outfit recommendations

See [API Documentation](../docs/API.md) for details.

## Development

### Running Tests

```bash
pytest
```

### Code Formatting

```bash
black app/
isort app/
```

### Database Migrations

```bash
# Create migration
alembic revision --autogenerate -m "Description"

# Apply migrations
alembic upgrade head

# Rollback
alembic downgrade -1
```

## MVP Limitations

Current MVP focuses on:
- ✅ Tops only (shirts, t-shirts, blouses, etc.)
- ✅ Basic rule-based outfit generation
- ✅ Mock e-commerce providers (configure real APIs in production)
- ✅ Simple heuristic-based recognition (replace with trained ML model)

## Next Steps for Production

1. Train/fine-tune garment recognition model (ViT or ResNet)
2. Implement CLIP embeddings for visual search
3. Set up FAISS index for similarity search
4. Integrate real e-commerce APIs (Amazon PA-API, Zalando)
5. Implement ML-based outfit recommendation model
6. Add user authentication (Firebase Auth)
7. Set up production infrastructure (AWS/GCP)
8. Implement monitoring and logging

