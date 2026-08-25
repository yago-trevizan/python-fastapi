from pydantic import BaseModel

class User(BaseModel):
  id: int
  name: str
  username: str
  password: str

class UserOutput(BaseModel):
  id: int
  name: str
  username: str

class GetUsersOutput(BaseModel):
  users: list[UserOutput]
