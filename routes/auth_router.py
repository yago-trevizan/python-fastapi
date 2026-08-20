from fastapi import APIRouter, Response, Cookie
from typing import Annotated
from models.auth_model import Credentials, User, GetUsersOutput
from db import usuarios
from utils.functions import hash_password

auth_router = APIRouter(prefix="/auth", tags=["authentication"])

@auth_router.post("/signin", status_code=201)
def signin(new_user: User):
  hashed_password = hash_password(new_user.password)
  new_user.password = hashed_password

  usuarios.append(new_user)

  return { "msg": f"Usuário '{new_user.username}' criado com sucesso" }


@auth_router.post("/login")
def login(credentials: Credentials ,response: Response):
  response.set_cookie("token", f"token-{credentials.username}")

  return { "msg": "Login realizado com sucesso" }

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
def get_users():
  return { "users": usuarios }