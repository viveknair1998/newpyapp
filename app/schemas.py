from pydantic import BaseModel

class RegistroCreate(BaseModel):
    name: str