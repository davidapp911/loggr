from sqlalchemy import Column, ForeignKey, Integer, Table

from app.db.base import Base

# Plain Table (not an ORM model class) because this table carries no extra data —
# it only links books to genres. SQLAlchemy uses it via the `secondary` argument on the relationship.
book_genres = Table(
    "book_genres",
    Base.metadata,
    Column("book_id", Integer, ForeignKey("books.id"), primary_key=True),
    Column("genre_id", Integer, ForeignKey("genres.id"), primary_key=True),
)
