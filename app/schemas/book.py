import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict

from app.models.book import book_status
from app.schemas.genre import GenreOut


class BookCreate(BaseModel):
    title: str
    author: str
    isbn: Optional[str] = None
    total_pages: Optional[int] = None
    status: book_status
    rating: Optional[float] = None
    started_at: Optional[datetime.date] = None
    finished_at: Optional[datetime.date] = None


# all fields Optional so PATCH only updates what the client actually sends
class BookUpdate(BaseModel):
    title: Optional[str] = None
    author: Optional[str] = None
    isbn: Optional[str] = None
    total_pages: Optional[int] = None
    status: Optional[book_status] = None
    rating: Optional[float] = None
    started_at: Optional[datetime.date] = None
    finished_at: Optional[datetime.date] = None


class BookOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    title: str
    author: str
    isbn: Optional[str]
    total_pages: Optional[int]
    status: book_status
    rating: Optional[float]
    started_at: Optional[datetime.date]
    finished_at: Optional[datetime.date]
    created_at: datetime.datetime
    user_id: int
    genres: list[GenreOut]
