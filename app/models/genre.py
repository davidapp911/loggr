from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base
from app.models.association import book_genres

if TYPE_CHECKING:
    from app.models.book import Book


class Genre(Base):
    __tablename__ = "genres"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(unique=True, nullable=False)

    books: Mapped[list["Book"]] = relationship("Book", secondary=book_genres, back_populates="genres")
