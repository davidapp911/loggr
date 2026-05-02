from fastapi import FastAPI

from app.routers import auth, books

app = FastAPI(title="Loggr API")

app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(books.router, prefix="/books", tags=["book"])


@app.get("/health")
def health():
    return {"status": "ok"}
