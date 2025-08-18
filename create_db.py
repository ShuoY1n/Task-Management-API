from database import Base, engine
from models import Item, User

print("Creating database...")
Base.metadata.create_all(engine)
print("Database created successfully")
