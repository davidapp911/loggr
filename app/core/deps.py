from collections.abc import Iterator

import jwt
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from app.core.config import settings
from app.db.base import SessionLocal
from app.models.user import User

# tells FastAPI where clients obtain a token — used to render the Authorize button in Swagger UI
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")


def database_session() -> Iterator[Session]:
    db = SessionLocal()

    try:
        yield db  # FastAPI injects db into the route; everything after yield runs after the response
        db.commit()  # auto-commit if the route completed without raising
    except:
        db.rollback()  # undo any partial writes if the route raised an exception
        raise
    finally:
        db.close()  # always release the connection back to the pool


def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(database_session)) -> User:
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
        user_id: int = int(payload["sub"])  # KeyError/ValueError caught below if "sub" is missing or non-numeric
    except (jwt.ExpiredSignatureError, jwt.InvalidTokenError, KeyError, ValueError):
        raise HTTPException(status_code=401, detail="Invalid or expired token")

    user = db.get(User, user_id)

    if not user or not user.is_active:
        raise HTTPException(status_code=401, detail="User not found or inactive")

    return user
