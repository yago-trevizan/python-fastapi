from fastapi import APIRouter, Cookie, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from typing import Annotated
from models.user_model import GetUsersOutput
from db import usuarios
import jwt
from os import getenv

SECRET_KEY = getenv("SECRET_KEY")
ALGORITHM = getenv("ALGORITHM")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

user_router = APIRouter(prefix="/users", tags=["Usuários"])

@user_router.get("/me")
def me(token: Annotated[str, Depends(oauth2_scheme)]):
  try:
    decoded = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
  except jwt.ExpiredSignatureError:
    raise HTTPException(status_code=401, detail="Token expired")

  username = decoded["sub"]
  current_user = next((u for u in usuarios if u.username == username), None)

  return { "current_user": current_user }

@user_router.get("/", response_model=GetUsersOutput)
def get_users(token: Annotated[str, Depends(oauth2_scheme)]):
  try:
    jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
  except jwt.ExpiredSignatureError:
    raise HTTPException(status_code=401, detail="Token expired")
  
  return { "users": usuarios }
