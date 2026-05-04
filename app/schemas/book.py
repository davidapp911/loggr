import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field, field_validator

from app.models.book import book_status
from app.schemas.genre import GenreOut


class BookCreate(BaseModel):
    title: str
    author: str
    isbn: Optional[str] = None
    status: book_status
    started_at: Optional[datetime.date] = None
    finished_at: Optional[datetime.date] = None

    rating: Optional[float] = Field(default=None, ge=0, le=5)

    @field_validator("rating")
    @classmethod
    def round_rating(cls, v):
        if v is not None:
            return round(v, 1)
        return v


# all fields Optional so PATCH only updates what the client actually sends
class BookUpdate(BaseModel):
    title: Optional[str] = None
    author: Optional[str] = None
    isbn: Optional[str] = None
    status: Optional[book_status] = None
    started_at: Optional[datetime.date] = None
    finished_at: Optional[datetime.date] = None

    rating: Optional[float] = Field(default=None, ge=0, le=5)

    @field_validator("rating")
    @classmethod
    def round_rating(cls, v):
        if v is not None:
            return round(v, 1)
        return v


class BookOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    title: str
    author: str
    isbn: Optional[str]
    status: book_status
    rating: Optional[float]
    started_at: Optional[datetime.date]
    finished_at: Optional[datetime.date]
    created_at: datetime.datetime
    user_id: int
    genres: list[GenreOut]
