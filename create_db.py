from database import Base, engine, user_engine
from models import Item, User

print("Creating database...")
Base.metadata.create_all(engine)
Base.metadata.create_all(user_engine)
print("Database created successfully")
