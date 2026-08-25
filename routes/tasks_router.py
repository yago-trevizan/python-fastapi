from fastapi import APIRouter, HTTPException, Depends
from models.task_model import Task, GetOutput, PostInput, PatchInput
from models.user_model import User
from typing import Annotated
from utils.db import tarefas
from utils.dependencies import get_logged_user
from utils.functions import get_next_id, get_task_index, validate_ownership

task_router = APIRouter(prefix="/tarefas", tags=["tarefas"])

@task_router.get("/", response_model=GetOutput)
def listar_tarefas(logged_user: Annotated[User, Depends(get_logged_user)]):
  tarefas_proprias = [t for t in tarefas if t.user_id == logged_user.id]

  return {
    "tasks": tarefas_proprias
  }

@task_router.post("/", response_model=Task)
def criar_tarefa(task: PostInput, logged_user: Annotated[User, Depends(get_logged_user)]):
  next_id = get_next_id()

  new_task = Task(id=next_id, title=task.title, user_id=logged_user.id)
  tarefas.append(new_task)

  return new_task

@task_router.patch("/{task_id}")
def atualizar_tarefa(task_id: int, task: PatchInput, logged_user: Annotated[User, Depends(get_logged_user)]):
  found_index = get_task_index(task_id)

  validate_ownership(found_index, logged_user.id, "atualizar")

  task_dict = task.model_dump(exclude_unset=True)

  if not task_dict:
    raise HTTPException(status_code=422, detail=f"Escolha um campo válido para atualizar")    
  
  updated_task = { **tarefas[found_index].model_dump(), **task_dict }
  tarefas[found_index] = Task(**updated_task)

  return { "detail": f"Tarefa {task_id} atualizada com sucesso" }

@task_router.delete("/{task_id}")
def deletar_tarefa(task_id: int, logged_user: Annotated[User, Depends(get_logged_user)]):
  found_index = get_task_index(task_id) 

  validate_ownership(found_index, logged_user.id, "excluir")

  del tarefas[found_index]

  return { "detail": f"Tarefa {task_id} excluída com sucesso" }
