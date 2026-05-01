from collections.abc import Iterator

from sqlalchemy.orm import Session

from app.db.base import SessionLocal


def database_session() -> Iterator[Session]:
    db = SessionLocal()

    try:
        yield db  # FastAPI injects db into the route; everything after yield runs after the response
        db.commit()  # auto-commit if the route completed without raising
    except:
        db.rollback()  # undo any partial writes if the route raised an exception
        raise
    finally:
        db.close()  # always release the connection back to the pool
