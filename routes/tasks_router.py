from fastapi import APIRouter, HTTPException, Depends
from models.tasks_model import Task, GetOutput, PostInput, PatchInput
from models.user_model import User
from typing import Annotated
from utils.db import tarefas
from utils.dependencies import oauth2_scheme, get_logged_user
from utils.functions import get_next_id

task_router = APIRouter(prefix="/tarefas", tags=["tarefas"])

@task_router.get("/", response_model=GetOutput)
def listar_tarefas(logged_user: Annotated[User, Depends(get_logged_user)]):
  tarefas_proprias = [t for t in tarefas if t.user_id == logged_user.id]

  return {
    "tarefas": tarefas_proprias
  }

@task_router.get("/{task_id}", response_model=Task, dependencies=[Depends(oauth2_scheme)])
def encontrar_tarefa(task_id: int):
  found_task = next((t for t in tarefas if t.id == task_id), None)

  if not found_task:
    raise HTTPException(status_code=404, detail=f"Tarefa {task_id} não encontrada")

  return found_task

@task_router.post("/", response_model=Task)
def criar_tarefa(task: PostInput, logged_user: Annotated[User, Depends(get_logged_user)]):
  next_id = get_next_id()

  new_task = Task(id=next_id, title=task.title, user_id=logged_user.id)
  tarefas.append(new_task)

  return new_task

@task_router.patch("/{task_id}")
def atualizar_tarefa(task_id: int, task: PatchInput, logged_user: Annotated[User, Depends(get_logged_user)]):

  found_index = next((i for i, t in enumerate(tarefas) if t.id == task_id), -1)

  if found_index == -1:
    raise HTTPException(status_code=404, detail=f"Tarefa {task_id} não encontrada")    

  owner_of_task = tarefas[found_index].user_id

  if owner_of_task != logged_user.id:
    raise HTTPException(status_code=422, detail="Você não pode atualizar uma tarefa que não é sua")

  task_dict = task.model_dump(exclude_unset=True)

  if not task_dict:
    raise HTTPException(status_code=422, detail=f"Escolha um campo válido para atualizar")    
  
  updated_task = { **tarefas[found_index].model_dump(), **task_dict }
  tarefas[found_index] = Task(**updated_task)

  return { "detail": f"Tarefa {task_id} atualizada com sucesso" }

@task_router.delete("/{task_id}", dependencies=[Depends(oauth2_scheme)])
def deletar_tarefa(task_id: int):
  found_index = next((i for i, t in enumerate(tarefas) if t.id == task_id), -1)

  if found_index == -1:
    raise HTTPException(status_code=404, detail=f"Tarefa {task_id} não encontrada")    

  del tarefas[found_index]

  return { "detail": f"Tarefa {task_id} excluída com sucesso" }
