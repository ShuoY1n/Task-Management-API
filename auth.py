from datetime import datetime, timedelta, timezone
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from typing import Annotated
from pydantic import BaseModel
from sqlalchemy.orm import Session
from starlette import status
from database import SessionLocal
from models import User as UserDB
from passlib.context import CryptContext
from jose import JWTError, jwt
import os

router = APIRouter(prefix="/auth", tags=["auth"])

secret_key = os.getenv("SECRET_KEY")
algorithm = os.getenv("ALGORITHM")

bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_bearer = OAuth2PasswordBearer(tokenUrl="auth/token")

class CreateUserRequest(BaseModel):
    username: str
    email: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

@router.post("/register", status_code=status.HTTP_201_CREATED)
async def register_user(db: db_dependency, create_user_request: CreateUserRequest):
    create_user_model = UserDB(
        username=create_user_request.username,
        email=create_user_request.email,
        password_hashed=bcrypt_context.hash(create_user_request.password),
        created_at=datetime.now(timezone.utc)
    )
    db.add(create_user_model)
    db.commit()
    db.refresh(create_user_model)