from __future__ import annotations

import datetime
import enum
from typing import TYPE_CHECKING, Optional

from sqlalchemy import Date, DateTime, Enum, Float, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base
from app.models.association import book_genres

if TYPE_CHECKING:
    from app.models.genre import Genre
    from app.models.review import Review
    from app.models.user import User


class book_status(enum.Enum):
    want_to_read = "want_to_read"
    reading = "reading"
    finished = "finished"


class Book(Base):
    __tablename__ = "books"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String(300), nullable=False)
    author: Mapped[str] = mapped_column(String(200), nullable=False)
    isbn: Mapped[Optional[str]] = mapped_column(String(20), nullable=True, unique=True)
    status: Mapped[book_status] = mapped_column(Enum(book_status), nullable=False)
    rating: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    started_at: Mapped[Optional[datetime.date]] = mapped_column(Date, nullable=True)
    finished_at: Mapped[Optional[datetime.date]] = mapped_column(Date, nullable=True)
    # datetime.now without () passes the function itself — SQLAlchemy calls it at insert time, not at class definition time
    created_at: Mapped[datetime.datetime] = mapped_column(DateTime, default=datetime.datetime.now)

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    user: Mapped["User"] = relationship(back_populates="books")

    # secondary tells SQLAlchemy to use book_genres as the join table — no manual inserts needed
    genres: Mapped[list["Genre"]] = relationship("Genre", secondary=book_genres, back_populates="books")
    reviews: Mapped[list["Review"]] = relationship("Review", back_populates="book", cascade="all, delete-orphan")
