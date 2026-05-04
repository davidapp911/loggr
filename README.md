# Loggr

A REST API for managing a personal reading list. Users can add books, tag them with genres, track reading status, write reviews, and query their library.

Built as a foundational learning project covering FastAPI, SQLAlchemy 2.0, Pydantic v2, JWT auth, Alembic migrations, and Docker.

## Tech Stack

- **Framework** — FastAPI
- **Database** — PostgreSQL 16
- **ORM** — SQLAlchemy 2.0 (synchronous)
- **Migrations** — Alembic
- **Validation** — Pydantic v2
- **Auth** — JWT via PyJWT
- **Password Hashing** — bcrypt

## Requirements

- Python 3.12+
- Docker

## Setup

### 1. Clone the repo

```bash
git clone <repo-url>
cd loggr
```

### 2. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -e .
```

### 4. Configure environment variables

```bash
cp .env.example .env
```

Edit `.env` with your values:

```
DATABASE_URL=postgresql://loggr:loggr@localhost:5432/loggrdb
SECRET_KEY=your-secret-key
ACCESS_TOKEN_EXPIRE_MINUTES=60
BCRYPT_ROUNDS=12
```

### 5. Start the database

```bash
docker-compose up -d
```

### 6. Run migrations

```bash
alembic upgrade head
```

### 7. Start the server

```bash
uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`.  
Interactive docs at `http://localhost:8000/docs`.

## Seeding Data

To populate the database with sample data:

```bash
python -m seeds.run
```

To wipe all data and reset sequences:

```bash
python -m seeds.hard_reset
```

## API Endpoints

| Method | Endpoint | Auth | Description |
|--------|----------|------|-------------|
| POST | `/auth/login` | Public | Email + password → JWT |
| GET | `/users/me` | Bearer | Current user profile |
| GET | `/genres` | Bearer | List all genres |
| GET | `/books` | Bearer | List own books — filter by `status`, `genre_id`; paginate with `limit`, `offset` |
| POST | `/books` | Bearer | Add a book |
| GET | `/books/{id}` | Bearer | Get a single book |
| PATCH | `/books/{id}` | Bearer + owner | Update a book |
| DELETE | `/books/{id}` | Bearer + owner | Delete a book |
| POST | `/books/{id}/genres` | Bearer + owner | Assign genres to a book |
| DELETE | `/books/{id}/genres` | Bearer + owner | Remove a genre from a book |
| GET | `/books/{id}/reviews` | Bearer | List reviews for a book |
| POST | `/books/{id}/reviews` | Bearer | Write a review |
| PATCH | `/books/{id}/reviews/{rid}` | Bearer + owner | Edit a review |
| DELETE | `/books/{id}/reviews/{rid}` | Bearer + owner | Delete a review |

## Authentication

1. `POST /auth/login` with `{"email": "...", "password": "..."}` to receive a token
2. Click **Authorize** in Swagger UI and paste the token
3. All protected routes will use it automatically
