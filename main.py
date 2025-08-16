from fastapi import FastAPI
from pydantic import BaseModel
from datetime import date

app = FastAPI()

class Item(BaseModel):
    id: id
    title: str
    description: str
    priority: int
    status: str
    due_date: date
    user_id: int

@app.get("/")
def index():
    return {"message": "hello"}

@app.get("/items")
def get_items():
    return {"message": "items"}