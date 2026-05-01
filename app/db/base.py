from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from app.core.config import settings

engine = create_engine(settings.DATABASE_URL, echo=False, future=True)

# autocommit=False: commits must be explicit (we do this in deps.py)
# autoflush=False: SQLAlchemy won't auto-sync pending changes before queries — gives us full control
SessionLocal = sessionmaker(autoflush=False, autocommit=False)
SessionLocal.configure(bind=engine)

# All ORM models inherit from Base so SQLAlchemy and Alembic can discover them
Base = declarative_base()
