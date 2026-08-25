from fastapi import APIRouter, Depends
from typing import Annotated
from models.user_model import GetUsersOutput
from utils.db import users
from utils.dependencies import verify_token

user_router = APIRouter(prefix="/users", tags=["users"])

@user_router.get("/me")
def get_current_user(decoded_token: Annotated[str, Depends(verify_token)]):
  username = decoded_token["sub"]
  current_user = next((u for u in users if u.username == username), None)

  return { "current_user": current_user }

@user_router.get("/", response_model=GetUsersOutput, dependencies=[Depends(verify_token)])
def list_users():
  return { "users": users }
