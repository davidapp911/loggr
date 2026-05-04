import seeds.book_genres as book_genres
import seeds.books as books
import seeds.genres as genres
import seeds.reviews as reviews
import seeds.users as users

if __name__ == "__main__":
    users.main()
    genres.main()
    books.main()
    book_genres.main()
    reviews.main()
