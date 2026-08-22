from pydantic import BaseModel

class Task(BaseModel):
  id: int
  title: str
  done: bool = False
  user_id: int

class GetOutput(BaseModel):
  tarefas: list[Task]

class PostInput(BaseModel):
  title: str

class PatchInput(BaseModel):
  title: str | None = None
  done: bool | None = None
