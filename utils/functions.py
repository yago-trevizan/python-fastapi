from utils.db import tarefas
from pwdlib import PasswordHash

password_hash = PasswordHash.recommended()

def get_next_id() -> int:
  next_id = 1

  if tarefas:
    next_id = tarefas[-1].id + 1

  return next_id

def hash_password(password: str):
  return password_hash.hash(password)

def verify_password(password: str, hashed_password: str):
  return password_hash.verify(password, hashed_password)
