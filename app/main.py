from fastapi import FastAPI

from app.routers import auth

app = FastAPI(title="Loggr API")

app.include_router(auth.router, prefix="/auth", tags=["auth"])


@app.get("/health")
def health():
    return {"status": "ok"}
