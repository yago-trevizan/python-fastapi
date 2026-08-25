from pydantic import BaseModel, Field

class User(BaseModel):
  id: int = Field(gt=0)
  name: str = Field(min_length=3)
  username: str = Field(max_length=12)
  password: str = Field(min_length=6)

class UserOutput(BaseModel):
  id: int
  name: str
  username: str

class GetUsersOutput(BaseModel):
  users: list[UserOutput]
