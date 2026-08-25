from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from typing import Annotated
from models.user_model import User
from utils.db import users
from utils.functions import hash_password, verify_password
import jwt
from datetime import datetime, timedelta, timezone
from dotenv import load_dotenv
from os import getenv

load_dotenv()

SECRET_KEY = getenv("SECRET_KEY")
ALGORITHM = getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = int(getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))

auth_router = APIRouter(prefix="/auth", tags=["authentication"])

@auth_router.post("/signin", status_code=201)
def signin(new_user: User):
  existing_user = next((u for u in users if u.username == new_user.username), None)

  if existing_user:
    raise HTTPException(status_code=422, detail=f"Username '{new_user.username}' already exists")

  hashed_password = hash_password(new_user.password)
  new_user.password = hashed_password

  users.append(new_user)

  return { "msg": f"User '{new_user.username}' successfully created" }

@auth_router.post("/login")
def login(credentials: Annotated[OAuth2PasswordRequestForm, Depends()]):
  user = next((u for u in users if u.username == credentials.username), None)

  if not user:
    raise HTTPException(status_code=401, detail="Username or password invalid")

  if not verify_password(credentials.password, user.password):
    raise HTTPException(status_code=401, detail="Username or password invalid")

  expires_at = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

  token = jwt.encode({ "sub": user.username, "exp": expires_at }, SECRET_KEY, algorithm=ALGORITHM)

  return { "access_token": token, "token_type": "bearer" }
