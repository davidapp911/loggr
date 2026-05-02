from fastapi import FastAPI

from app.routers import auth, books, genres

app = FastAPI(title="Loggr API")

app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(books.router, prefix="/books", tags=["book"])
app.include_router(genres.router, prefix="/genres", tags=["genre"])


@app.get("/health")
def health():
    return {"status": "ok"}
