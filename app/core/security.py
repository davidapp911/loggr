import datetime

import bcrypt
import jwt

from app.core.config import settings


def hash_password(password: str) -> str:
    # gensalt() generates a random salt each time, so identical passwords produce different hashes
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")


def verify_password(plain: str, hashed: str) -> bool:
    # bcrypt extracts the salt from the stored hash automatically before comparing
    return bcrypt.checkpw(plain.encode("utf-8"), hashed.encode("utf-8"))


def create_access_token(user_id: int) -> str:
    payload = {
        "sub": str(user_id),  # "sub" (subject) is the standard JWT claim for the user identifier
        "exp": datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES),
    }

    return jwt.encode(payload, settings.SECRET_KEY, algorithm="HS256")
