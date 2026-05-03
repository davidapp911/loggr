from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.core.deps import database_session, get_current_user
from app.models.review import Review
from app.models.user import User
from app.routers.books import fetch_book
from app.schemas.review import ReviewCreate, ReviewOut, ReviewUpdate

router = APIRouter()


@router.post("/books/{book_id}/reviews", response_model=ReviewOut, status_code=201)
def create_review(book_id: int, body: ReviewCreate, db: Session = Depends(database_session), current_user: User = Depends(get_current_user)):
    book = fetch_book(book_id, db, current_user)
    review = Review(content=body.content, book_id=book.id, user_id=current_user.id)
    db.add(review)
    db.flush()
    return review


@router.get("/books/{book_id}/reviews", response_model=list[ReviewOut], status_code=200)
def get_reviews(book_id: int, db: Session = Depends(database_session), current_user: User = Depends(get_current_user)):
    book = fetch_book(book_id, db, current_user)

    return db.execute(select(Review).where(Review.book_id == book.id)).scalars().all()


@router.patch("/books/{book_id}/reviews/{review_id}", response_model=ReviewOut, status_code=200)
def update_review(book_id: int, review_id: int, body: ReviewUpdate, db: Session = Depends(database_session), current_user: User = Depends(get_current_user)):
    review = fetch_review(book_id, review_id, db, current_user)

    if not body.content or body.content.strip() == "":
        raise HTTPException(status_code=422, detail="No content provided")

    review.content = body.content

    return review


@router.delete("/books/{book_id}/reviews/{review_id}", status_code=204)
def delete_review(book_id: int, review_id: int, db: Session = Depends(database_session), current_user: User = Depends(get_current_user)):
    review = fetch_review(book_id, review_id, db, current_user)

    db.delete(review)


def fetch_review(book_id: int, review_id: int, db: Session, current_user: User) -> Review:
    book = fetch_book(book_id, db, current_user)

    review = db.get(Review, review_id)

    if review:
        if review.user_id != current_user.id:
            raise HTTPException(status_code=403, detail="Access forbidden")
        elif review.book_id != book.id:
            raise HTTPException(status_code=404, detail="Review not found")
    else:
        raise HTTPException(status_code=404, detail="Review not found")

    return review
