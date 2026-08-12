from db import tarefas

def get_next_id() -> int:
  next_id = 1

  if tarefas:
    next_id = tarefas[-1]["id"] + 1

  return next_id
