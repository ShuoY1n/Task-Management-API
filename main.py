from fastapi import FastAPI, status
from pydantic import BaseModel
from datetime import date
from database import SessionLocal
from typing import List
from models import Item, User

app = FastAPI()

class Item(BaseModel):
    id: int
    title: str
    description: str
    priority: int
    status: str
    due_date: date
    user_id: int

    class Config:
        orm_mode = True

class User(BaseModel):
    id: int
    username: str
    email: str
    password_hashed: str
    created_at: date

    class Config:
        orm_mode = True

session = SessionLocal()

@app.get("/")
def index():
    return {"message": "welcome to the task management API!"}

@app.get("/items", response_model=list[Item], status_code=status.HTTP_200_OK)
def get_all_items():
    items = session.query(Item).all()

    return items

@app.get("/items/{item_id}")
def get_item(item_id: int):
    return {"message": f"task {item_id}"}

@app.post("/items", response_model=Item, status_code=status.HTTP_201_CREATED)
def create_item(item: Item):
    new_item = Item(
        title=item.title,
        description=item.description,
        priority=item.priority,
        status="incomplete",
        due_date=item.due_date,
        user_id=item.user_id
    )

    session.add(new_item)
    session.commit()

    return new_item

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"message": "task updated"}

@app.patch("/items/{item_id}/start")
def start_item(item_id: int):
    return {"message": "task started"}

@app.patch("/items/{item_id}/complete")
def complete_item(item_id: int):
    return {"message": "task completed"}




@app.post("/users/register")
def register_user(user: User):
    return {"message": "user created"}

@app.post("/users/login")
def login_user(user: User):
    return {"access_token": "token"}

@app.post("/users/change-password")
def change_password(user: User):
    return {"message": "password changed"}