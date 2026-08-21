from pydantic import BaseModel, Field

class User(BaseModel):
  name: str = Field(min_length=3)
  username: str = Field(max_length=12)
  password: str = Field(min_length=6)

class UserOutput(BaseModel):
  name: str
  username: str

class GetUsersOutput(BaseModel):
  users: list[UserOutput]
