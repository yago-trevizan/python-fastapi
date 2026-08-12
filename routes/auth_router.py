from fastapi import APIRouter, Response, Cookie
from typing import Annotated
from models.auth_model import Credentials

auth_router = APIRouter(prefix="/auth", tags=["authentication"])

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
