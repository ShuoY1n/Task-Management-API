from database import Base
from sqlalchemy import Column, Integer, String, Date

class Item(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    status = Column(String, nullable=False)
    due_date = Column(Date, nullable=False)
    user_id = Column(Integer, nullable=False)

    def __repr__(self):
        return f"<Item(id={self.id}, title={self.title}, description={self.description}, status={self.status}, due_date={self.due_date}, user_id={self.user_id})>"

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    email = Column(String, nullable=False)
    password_hashed = Column(String, nullable=False)
    created_at = Column(Date, nullable=False)

    def __repr__(self):
        return f"<User(id={self.id}, username={self.username}, email={self.email}, password={self.password_hashed}, created_at={self.created_at})>"