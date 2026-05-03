import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict


class ReviewCreate(BaseModel):
    content: str


class ReviewUpdate(BaseModel):
    content: Optional[str] = None


class ReviewOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    content: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    book_id: int
    user_id: int
