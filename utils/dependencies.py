from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from typing import Annotated
from dotenv import load_dotenv
from os import getenv
import jwt

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
