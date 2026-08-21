from fastapi import APIRouter, Depends
from typing import Annotated
from models.user_model import GetUsersOutput
from utils.db import usuarios
from utils.dependencies import verify_token

user_router = APIRouter(prefix="/users", tags=["Usuários"])

@user_router.get("/me")
def me(decoded_token: Annotated[str, Depends(verify_token)]):
  username = decoded_token["sub"]
  current_user = next((u for u in usuarios if u.username == username), None)

  return { "current_user": current_user }

@user_router.get("/", response_model=GetUsersOutput, dependencies=[Depends(verify_token)])
def get_users():
  return { "users": usuarios }
