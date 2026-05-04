import csv
import os

from app.core.security import hash_password
from app.db.base import SessionLocal
from app.models.user import User


def main():
    db = SessionLocal()

    try:
        csv_path = os.path.join(os.path.dirname(__file__), "data", "users.csv")

        with open(csv_path, mode="r", newline="") as file:
            data_reader = csv.DictReader(file)

            for row in data_reader:
                user = User(
                    id=int(row["id"]),
                    email=row["email"],
                    username=row["username"],
                    hashed_password=hash_password(row["password"]),
                )

                db.add(user)
        db.commit()
        print("Users seeded successfully.")
    except Exception as e:
        db.rollback()
        print(f"Failed to seed user: {e}")
    finally:
        db.close()


if __name__ == "__main__":
    main()
