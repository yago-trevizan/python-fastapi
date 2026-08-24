from fastapi import HTTPException
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

def get_task_index(task_id: int):
  found_index = next((i for i, t in enumerate(tarefas) if t.id == task_id), -1)
 
  if found_index == -1:
    raise HTTPException(status_code=404, detail=f"Tarefa {task_id} não encontrada")

  return found_index

def validate_ownership(task_index: int, logged_user_id: int, action: str):
  owner_id = tarefas[task_index].user_id
  
  if owner_id != logged_user_id:
    raise HTTPException(status_code=422, detail=f"Você não pode {action} uma tarefa que não é sua")
