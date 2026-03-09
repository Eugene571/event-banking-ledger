from fastapi import FastAPI

app = FastAPI(
    title="Event Banking Ledger",
    description="Личный финансовый трекер на основе событий (event sourcing light)",
    version="0.1.0",
    docs_url="/docs",  # Swagger UI
    redoc_url="/redoc",
    openapi_url="/openapi.json"
)


@app.get("/health")
async def health():
    return {"status": "ok", "version": app.version}
