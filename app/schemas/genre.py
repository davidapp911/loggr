from pydantic import BaseModel, ConfigDict


class GenreIdIn(BaseModel):
    id: int


class GenreIdsIn(BaseModel):
    ids: list[int]


class GenreOut(BaseModel):
    # from_attributes=True lets Pydantic read from SQLAlchemy ORM objects, not just dicts
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
