from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

# DATABASE_URL = "postgresql://postgres:password@localhost:5432/item_db"
# USER_DATABASE_URL = "postgresql://postgres:password@localhost:5432/user_db"

DATABASE_URL = "sqlite:///./items.db"
USER_DATABASE_URL = "sqlite:///./users.db"

engine = create_engine(DATABASE_URL, echo=True)
user_engine = create_engine(USER_DATABASE_URL, echo=True)

SessionLocal = sessionmaker(bind=engine)
user_SessionLocal = sessionmaker(bind=user_engine)

Base = declarative_base()