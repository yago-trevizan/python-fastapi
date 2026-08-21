from fastapi import APIRouter, Response, Cookie, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from typing import Annotated
from models.auth_model import Credentials, User, GetUsersOutput
from db import usuarios
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

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

@auth_router.post("/signin", status_code=201)
def signin(new_user: User):
  hashed_password = hash_password(new_user.password)
  new_user.password = hashed_password

  usuarios.append(new_user)

  return { "msg": f"Usuário '{new_user.username}' criado com sucesso" }

@auth_router.post("/login")
def login(credentials: Annotated[OAuth2PasswordRequestForm, Depends()]):
  user = next((u for u in usuarios if u.username == credentials.username), None)

  if not user:
    raise HTTPException(status_code=401, detail="Username or password invalid")

  if not verify_password(credentials.password, user.password):
    raise HTTPException(status_code=401, detail="Username or password invalid")

  expires_at = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

  token = jwt.encode({ "sub": user.username, "exp": expires_at }, SECRET_KEY, algorithm=ALGORITHM)

  return { "access_token": token, "token_type": "bearer" }

@auth_router.post("/logout")
def logout(response: Response):
  response.delete_cookie("token")

  return { "msg": "Você foi deslogado" }

@auth_router.get("/me")
def me(token: Annotated[str, Cookie()] = ""):
  if token:
    username = token[6:]

    return { "msg": f"Logado com: {username}"}

  return { "msg": "Deslogado" }

@auth_router.get("/users", response_model=GetUsersOutput)
def get_users(token: Annotated[str, Depends(oauth2_scheme)]):
  try:
    jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
  except jwt.ExpiredSignatureError:
    raise HTTPException(status_code=401, detail="Token expired")
  
  return { "users": usuarios }
