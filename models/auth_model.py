from pydantic import BaseModel, Field

class SigninInput(BaseModel):
  name: str = Field(min_length=3)
  username: str = Field(max_length=12)
  password: str = Field(min_length=6)
