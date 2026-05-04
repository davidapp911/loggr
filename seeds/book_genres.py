import csv
import os

from app.db.base import SessionLocal
from app.models.genre import Genre
from app.models.book import Book


def main():
    db = SessionLocal()

    try:
        csv_path = os.path.join(os.path.dirname(__file__), "data", "book_genres.csv")

        with open(csv_path, mode="r", newline="") as file:
            data_reader = csv.DictReader(file)

            for row in data_reader:
                book = db.get(Book, int(row["book_id"]))
                genre = db.get(Genre, int(row["genre_id"]))

                if book and genre and genre not in book.genres:
                    book.genres.append(genre)

        db.commit()
        print("Book genres seeded successfully.")
    except Exception as e:
        db.rollback()
        print(f"Failed to seed book genres: {e}")
    finally:
        db.close()


if __name__ == "__main__":
    main()
