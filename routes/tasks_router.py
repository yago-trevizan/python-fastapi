from fastapi import APIRouter, HTTPException
from models.tasks_model import Task, GetOutput, PostInput, PatchInput
from db import tarefas
from utils.functions import get_next_id

task_router = APIRouter(prefix="/tarefas", tags=["tarefas"])

@task_router.get("/", response_model=GetOutput)
def listar_tarefas() :
  return {
    "tarefas": tarefas
  }

@task_router.get("/{task_id}", response_model=Task)
def encontrar_tarefa(task_id: int):
  found_tasks = [t for t in tarefas if t["id"] == task_id]

  if not found_tasks:
    raise HTTPException(status_code=404, detail=f"Tarefa {task_id} não encontrada")

  return found_tasks[0]

@task_router.post("/", response_model=Task)
def criar_tarefa(task: PostInput):
  next_id = get_next_id()

  new_task = Task(id=next_id, title=task.title)
  tarefas.append(new_task.model_dump())

  return new_task

@task_router.patch("/{task_id}")
def atualizar_tarefa(task_id: int, task: PatchInput):

  found_index = -1
  
  for i, tarefa in enumerate(tarefas):
    if tarefa["id"] == task_id:
      found_index = i
      break

  if found_index == -1:
    raise HTTPException(status_code=404, detail=f"Tarefa {task_id} não encontrada")    

  task_dict = task.model_dump(exclude_unset=True)

  if not task_dict:
    raise HTTPException(status_code=422, detail=f"Escolha um campo válido para atualizar")    
  
  tarefas[found_index] = { **tarefas[found_index], **task_dict }

  return { "detail": f"Tarefa {task_id} atualizada com sucesso" }

@task_router.delete("/{task_id}")
def deletar_tarefa(task_id: int):
  global tarefas

  found_index = -1

  for i, task in enumerate(tarefas):
    if task["id"] == task_id:
      found_index = i
      break

  if found_index == -1:
    raise HTTPException(status_code=404, detail=f"Tarefa {task_id} não encontrada")    

  del tarefas[found_index]

  return { "detail": f"Tarefa {task_id} excluída com sucesso" }
