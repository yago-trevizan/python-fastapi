from fastapi import HTTPException
from utils.db import tasks
from pwdlib import PasswordHash

password_hash = PasswordHash.recommended()

def get_next_id() -> int:
  next_id = 1

  if tasks:
    next_id = tasks[-1].id + 1

  return next_id


def hash_password(password: str):
  return password_hash.hash(password)


def verify_password(password: str, hashed_password: str):
  return password_hash.verify(password, hashed_password)


def get_task_index(task_id: int):
  found_index = next((i for i, t in enumerate(tasks) if t.id == task_id), -1)
 
  if found_index == -1:
    raise HTTPException(status_code=404, detail=f"Task {task_id} not found")

  return found_index


def validate_ownership(task_index: int, logged_user_id: int, action: str):
  owner_id = tasks[task_index].user_id
  
  if owner_id != logged_user_id:
    raise HTTPException(status_code=422, detail=f"You can't {action} a task that is not yours")
