from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.core.deps import database_session, get_current_user
from app.models.book import Book
from app.models.user import User
from app.schemas.book import BookCreate, BookOut, BookUpdate

router = APIRouter()


@router.post("/", response_model=BookOut, status_code=201)
def create_book(body: BookCreate, db: Session = Depends(database_session), current_user: User = Depends(get_current_user)):
    book = Book(**body.model_dump(), user_id=current_user.id)
    db.add(book)
    db.flush()
    return book


@router.get("/", response_model=list[BookOut], status_code=200)
def get_books(db: Session = Depends(database_session), current_user: User = Depends(get_current_user)):
    return db.execute(select(Book).where(Book.user_id == current_user.id)).scalars().all()


@router.get("/{id}", response_model=BookOut, status_code=200)
def get_book(id: int, db: Session = Depends(database_session), current_user: User = Depends(get_current_user)):
    book = db.get(Book, id)

    if not book:
        raise HTTPException(status_code=404, detail="Book not found")

    if book.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Access forbidden")

    return book


@router.patch("/{id}", response_model=BookOut, status_code=200)
def update_book(id: int, update: BookUpdate, db: Session = Depends(database_session), current_user: User = Depends(get_current_user)):
    book = db.get(Book, id)

    if not book:
        raise HTTPException(status_code=404, detail="Book not found")

    if book.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Access forbidden")

    update_data = update.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        setattr(book, key, value)

    return book


@router.delete("/{id}", status_code=204)
def delete_book(id: int, db: Session = Depends(database_session), current_user: User = Depends(get_current_user)):
    book = db.get(Book, id)

    if not book:
        raise HTTPException(status_code=404, detail="Book not found")

    if book.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Access forbidden")

    db.delete(book)


# POST /books/{id}/genres — assign genres
# DELETE /books/{id}/genres/{genre_id} — remove a genre
