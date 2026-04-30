from collections.abc import Iterator

from sqlalchemy.orm import Session

from app.db.base import SessionLocal


def database_session() -> Iterator[Session]:
    db = SessionLocal()

    try:
        yield db
        db.commit()
    except:
        db.rollback()
        raise
    finally:
        db.close()
