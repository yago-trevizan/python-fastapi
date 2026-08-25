from fastapi import APIRouter, HTTPException, Depends
from models.task_model import Task, GetOutput, PostInput, PatchInput
from models.user_model import User
from typing import Annotated
from utils.db import tasks
from utils.dependencies import get_logged_user
from utils.functions import get_next_id, get_task_index, validate_ownership

task_router = APIRouter(prefix="/tasks", tags=["tasks"])

@task_router.get("/", response_model=GetOutput)
def list_tasks(logged_user: Annotated[User, Depends(get_logged_user)]):
  owned_tasks = [t for t in tasks if t.user_id == logged_user.id]

  return {
    "tasks": owned_tasks
  }

@task_router.post("/", response_model=Task)
def create_task(task: PostInput, logged_user: Annotated[User, Depends(get_logged_user)]):
  next_id = get_next_id()

  new_task = Task(id=next_id, title=task.title, user_id=logged_user.id)
  tasks.append(new_task)

  return new_task

@task_router.patch("/{task_id}")
def update_task(task_id: int, task: PatchInput, logged_user: Annotated[User, Depends(get_logged_user)]):
  found_index = get_task_index(task_id)

  validate_ownership(found_index, logged_user.id, "update")

  task_dict = task.model_dump(exclude_unset=True)

  if not task_dict:
    raise HTTPException(status_code=422, detail=f"Choose a valid field to update")    
  
  updated_task = { **tasks[found_index].model_dump(), **task_dict }
  tasks[found_index] = Task(**updated_task)

  return { "detail": f"Task {task_id} successfully updated" }

@task_router.delete("/{task_id}")
def delete_task(task_id: int, logged_user: Annotated[User, Depends(get_logged_user)]):
  found_index = get_task_index(task_id) 

  validate_ownership(found_index, logged_user.id, "excluir")

  del tasks[found_index]

  return { "detail": f"Task {task_id} successfully deleted" }
