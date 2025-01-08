from fastapi import FastAPI
from pydantic import BaseModel
from datetime import date

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

@app.get("/")
def index():
    return {"message": "welcome to the task management API!"}

@app.get("/items")
def get_all_items():
    return {"message": "all tasks"}

@app.get("/items/{item_id}")
def get_item(item_id: int):
    return {"message": f"task {item_id}"}

@app.post("/items")
def create_item(item: Item):
    return {"message": "task created", "name": item.title}

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