from sqlalchemy import text

from app.db.base import SessionLocal


def main():
    db = SessionLocal()
    try:
        db.execute(text("TRUNCATE TABLE reviews, book_genres, books, users, genres RESTART IDENTITY CASCADE"))
        db.commit()
        print("All tables cleared and sequences reset.")
    except Exception as e:
        db.rollback()
        print(f"Failed: {e}")
    finally:
        db.close()


if __name__ == "__main__":
    main()
