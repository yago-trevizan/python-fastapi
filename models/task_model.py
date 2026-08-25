from pydantic import BaseModel, Field

class Task(BaseModel):
  id: int
  title: str
  done: bool = False
  user_id: int

class GetOutput(BaseModel):
  tasks: list[Task]

class PostInput(BaseModel):
  title: str = Field(min_length=5, max_length=40)

class PatchInput(BaseModel):
  title: str | None = None
  done: bool | None = None
