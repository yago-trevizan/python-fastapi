from pydantic import BaseModel, Field

class Credentials(BaseModel):
  username: str = Field(max_length=12)
  password: str = Field(min_length=6)
