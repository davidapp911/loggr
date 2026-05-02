from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.core.deps import database_session
from app.models.genre import Genre
from app.schemas.genre import GenreOut

router = APIRouter()


@router.get("/", response_model=list[GenreOut], status_code=200)
def get_genres(db: Session = Depends(database_session)):
    return db.execute(select(Genre)).scalars().all()
