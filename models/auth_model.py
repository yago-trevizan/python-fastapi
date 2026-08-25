from pydantic import BaseModel, Field

class SigninInput(BaseModel):
  name: str = Field(pattern="^[a-zA-Z ]{3,40}$")
  username: str = Field(pattern="^[a-z0-9_]{5,12}$")
  password: str = Field(min_length=6)
