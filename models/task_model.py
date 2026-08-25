from pydantic import BaseModel, StringConstraints
from typing import Annotated

Title = Annotated[str, StringConstraints(min_length=5, max_length=40)]

class Task(BaseModel):
  id: int
  title: str
  done: bool = False
  user_id: int

class GetOutput(BaseModel):
  tasks: list[Task]

class PostInput(BaseModel):
  title: Title

class PatchInput(BaseModel):
  title: Title | None = None
  done: bool | None = None
