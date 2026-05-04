import csv
import datetime
import os

from app.db.base import SessionLocal
from app.models.book import Book, book_status


def parse_date(value: str) -> datetime.date | None:
    return datetime.date.fromisoformat(value) if value else None


def parse_float(value: str) -> float | None:
    return float(value) if value else None


def main():
    db = SessionLocal()

    try:
        csv_path = os.path.join(os.path.dirname(__file__), "data", "books.csv")

        with open(csv_path, mode="r", newline="") as file:
            data_reader = csv.DictReader(file)

            for row in data_reader:
                book = Book(
                    id=int(row["id"]),
                    user_id=int(row["user_id"]),
                    title=row["title"],
                    author=row["author"],
                    isbn=row["isbn"] or None,
                    status=book_status(row["status"]),
                    rating=parse_float(row["rating"]),
                    started_at=parse_date(row["started_at"]),
                    finished_at=parse_date(row["finished_at"]),
                )

                db.add(book)
        db.commit()
        print("Books seeded successfully.")
    except Exception as e:
        db.rollback()
        print(f"Failed to seed books: {e}")
    finally:
        db.close()


if __name__ == "__main__":
    main()
