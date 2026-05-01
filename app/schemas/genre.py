from pydantic import BaseModel, ConfigDict


class GenreOut(BaseModel):
    # from_attributes=True lets Pydantic read from SQLAlchemy ORM objects, not just dicts
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
