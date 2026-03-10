from fastapi import FastAPI, Depends
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.config import settings
from app.infrastructure.database import get_db

app = FastAPI(
    title="Event Banking Ledger",
    description="Личный финансовый трекер на основе событий (event sourcing light)",
    version="0.1.0",
    docs_url="/docs",  # Swagger UI
    redoc_url="/redoc",
    openapi_url="/openapi.json"
)

print(f"Запускаюсь на  http://{settings.app_host}:{settings.app_port}")


@app.get("/test-db")
async def test_db(db: AsyncSession = Depends(get_db)):
    result = await db.execute(text("SELECT version();"))
    version = result.scalar()
    return {"status": "ok", "postgres_version": version}


@app.get("/health")
async def health():
    return {
        "status": "ok",
        "version": app.version,
        "environment": "development" if settings.app_reload else "production"
    }
