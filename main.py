from fastapi import FastAPI, status, HTTPException, Depends
from pydantic import BaseModel
from datetime import date
from database import SessionLocal
from typing import List, Optional
from models import Item as ItemDB, User as UserDB
from auth import router as auth_router, get_current_user, get_db
from sqlalchemy.orm import Session
from typing import Annotated

db_dependency = Annotated[Session, Depends(get_db)]
user_dependency = Annotated[dict, Depends(get_current_user)]

app = FastAPI()
app.include_router(auth_router)

class Item(BaseModel):
    id: int | None = None
    title: str
    description: str
    status: str
    due_date: date
    user_id: int

    class Config:
        orm_mode = True

class User(BaseModel):
    id: int | None = None
    username: str
    email: str
    password_hashed: str
    created_at: date

    class Config:
        orm_mode = True

db = SessionLocal()

@app.get("/")
def index():
    return {"message": "welcome to the task management API!"}

@app.get("/items", response_model=list[Item], status_code=status.HTTP_200_OK)
def get_all_items(user: user_dependency, db: db_dependency, status: Optional[str] = None, due_date: Optional[date] = None):
    if status:
        items = db.query(ItemDB).filter(ItemDB.user_id == user["id"], ItemDB.status == status).all()
    elif due_date:
        items = db.query(ItemDB).filter(ItemDB.user_id == user["id"], ItemDB.due_date == due_date).all()
    else:
        items = db.query(ItemDB).filter(ItemDB.user_id == user["id"]).all()

    return items

@app.get("/items/{item_id}", response_model=Item, status_code=status.HTTP_200_OK)
def get_item(item_id: int, user: user_dependency, db: db_dependency):
    item = db.query(ItemDB).filter(ItemDB.id == item_id, ItemDB.user_id == user["id"]).first()
    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
    return item

@app.post("/items", response_model=Item, status_code=status.HTTP_201_CREATED)
def create_item(item: Item, user: user_dependency, db: db_dependency):
    new_item = ItemDB(
        title=item.title,
        description=item.description,
        status="incomplete",
        due_date=item.due_date,
        user_id=user["id"]
    )

    db.add(new_item)
    db.commit()
    db.refresh(new_item)

    return new_item

@app.put("/items/{item_id}", response_model=Item, status_code=status.HTTP_200_OK)
def update_item(item_id: int, item: Item, user: user_dependency, db: db_dependency):
    item_to_update = db.query(ItemDB).filter(ItemDB.id == item_id, ItemDB.user_id == user["id"]).first()
    if not item_to_update:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")

    item_to_update.title = item.title
    item_to_update.description = item.description
    item_to_update.due_date = item.due_date

    db.commit()

    return item_to_update

@app.patch("/items/{item_id}/start", response_model=Item, status_code=status.HTTP_200_OK)
def start_item(item_id: int, user: user_dependency, db: db_dependency):
    item_to_start = db.query(ItemDB).filter(ItemDB.id == item_id, ItemDB.user_id == user["id"]).first()
    if not item_to_start:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")

    item_to_start.status = "in progress"
    db.commit()

    return item_to_start

@app.patch("/items/{item_id}/complete", response_model=Item, status_code=status.HTTP_200_OK)
def complete_item(item_id: int, user: user_dependency, db: db_dependency):
    item_to_complete = db.query(ItemDB).filter(ItemDB.id == item_id, ItemDB.user_id == user["id"]).first()
    if not item_to_complete:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")

    item_to_complete.status = "completed"
    db.commit()

    return item_to_complete