from pydantic import BaseModel, Field

class Credentials(BaseModel):
  username: str
  password: str = Field(min_length=6)
