import csv
import datetime
import os

from app.db.base import SessionLocal
from app.models.review import Review


def parse_date(value: str) -> datetime.date | None:
    return datetime.date.fromisoformat(value) if value else None


def parse_float(value: str) -> float | None:
    return float(value) if value else None


def main():
    db = SessionLocal()

    try:
        csv_path = os.path.join(os.path.dirname(__file__), "data", "reviews.csv")

        with open(csv_path, mode="r", newline="") as file:
            data_reader = csv.DictReader(file)

            for row in data_reader:
                review = Review(
                    id=int(row["id"]),
                    content=row["content"],
                    book_id=int(row["book_id"]),
                    user_id=int(row["user_id"]),
                )

                db.add(review)
        db.commit()
        print("Reviews seeded successfully.")
    except Exception as e:
        db.rollback()
        print(f"Failed to seed review: {e}")
    finally:
        db.close()


if __name__ == "__main__":
    main()
