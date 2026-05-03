import datetime
from typing import TYPE_CHECKING

from sqlalchemy import DateTime, ForeignKey, Text, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base

if TYPE_CHECKING:
    from app.models.book import Book
    from app.models.user import User


class Review(Base):
    __tablename__ = "reviews"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    content: Mapped[str] = mapped_column(Text, nullable=False)
    created_at: Mapped[datetime.datetime] = mapped_column(DateTime, default=func.now())
    updated_at: Mapped[datetime.datetime] = mapped_column(DateTime, default=func.now(), onupdate=func.now())

    book_id: Mapped[int] = mapped_column(ForeignKey("books.id"))
    book: Mapped["Book"] = relationship(back_populates="reviews")

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    user: Mapped["User"] = relationship(back_populates="reviews")
