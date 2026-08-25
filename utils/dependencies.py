from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from typing import Annotated
from pydantic import BaseModel
from dotenv import load_dotenv
from os import getenv
from utils.db import usuarios
import jwt

class Token(BaseModel):
  sub: str
  exp: int

load_dotenv()

SECRET_KEY = getenv("SECRET_KEY")
ALGORITHM = getenv("ALGORITHM")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

def verify_token(token: Annotated[str, Depends(oauth2_scheme)]):
  try:
    decoded_token = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
  except jwt.ExpiredSignatureError:
    raise HTTPException(status_code=401, detail="Expired Token")
  except jwt.DecodeError:
    raise HTTPException(status_code=401, detail="Invalid Token")
  else:
    return decoded_token


def get_logged_user(decoded_token: Annotated[Token, Depends(verify_token)]):
  username = decoded_token["sub"]

  found_user = next((u for u in usuarios if u.username == username), None)

  if not found_user:
    raise HTTPException(status_code=401, detail="User not found")

  return found_user
