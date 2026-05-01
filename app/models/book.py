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
    from app.models.user import User


class book_status(enum.Enum):
    want_to_read = "want_to_read"
    reading = "reading"
    finished = "finished"


class Book(Base):
    __tablename__ = "books"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)  # id Integer PK, autoincrement Primary key
    title: Mapped[str] = mapped_column(String(300), nullable=False)  # title String(300) NOT NULL Book title
    author: Mapped[str] = mapped_column(String(200), nullable=False)  # author String(200) NOT NULL Author full name
    isbn: Mapped[Optional[str]] = mapped_column(String(20), nullable=True, unique=True)  # isbn String(20) nullable, UNIQUE ISBN-10 or ISBN-13
    total_pages: Mapped[Optional[int]] = mapped_column(nullable=True)  # total_pages Integer nullable Used to compute read %
    status: Mapped[book_status] = mapped_column(Enum(book_status), nullable=False)  # status Enum NOT NULL 'want_to_read', 'reading', 'finished'
    rating: Mapped[Optional[float]] = mapped_column(Float, nullable=True)  # rating Float nullable 1.0–5.0 — nullable until finished
    started_at: Mapped[Optional[datetime.date]] = mapped_column(Date, nullable=True)  # started_at Date nullable When the user started reading
    finished_at: Mapped[Optional[datetime.date]] = mapped_column(Date, nullable=True)  # finished_at Date nullable When the user finished
    created_at: Mapped[datetime.datetime] = mapped_column(DateTime, default=datetime.datetime.now)  # created_at DateTime default now()

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))  # user_id Integer FK → users.id Owner — CASCADE on delete
    user: Mapped["User"] = relationship(back_populates="books")

    genres: Mapped[list["Genre"]] = relationship("Genre", secondary=book_genres, back_populates="books")
