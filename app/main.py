from fastapi import FastAPI
from app.core.config import settings

app = FastAPI(
    title="Event Banking Ledger",
    description="Личный финансовый трекер на основе событий (event sourcing light)",
    version="0.1.0",
    docs_url="/docs",  # Swagger UI
    redoc_url="/redoc",
    openapi_url="/openapi.json"
)

print(f"Запускаюсь на  http://{settings.app_host}:{settings.app_port}")


@app.get("/health")
async def health():
    return {
        "status": "ok",
        "version": app.version,
        "environment": "development" if settings.app_reload else "production"
    }
