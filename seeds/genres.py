import csv
import datetime
import os

from app.db.base import SessionLocal
from app.models.genre import Genre


def parse_date(value: str) -> datetime.date | None:
    return datetime.date.fromisoformat(value) if value else None


def parse_float(value: str) -> float | None:
    return float(value) if value else None


def main():
    db = SessionLocal()

    try:
        csv_path = os.path.join(os.path.dirname(__file__), "data", "genres.csv")

        with open(csv_path, mode="r", newline="") as file:
            data_reader = csv.DictReader(file)

            for row in data_reader:
                genre = Genre(
                    id=int(row["id"]),
                    name=row["name"],
                )

                db.add(genre)
        db.commit()
        print("Genres seeded successfully.")
    except Exception as e:
        db.rollback()
        print(f"Failed to seed genre: {e}")
    finally:
        db.close()


if __name__ == "__main__":
    main()
