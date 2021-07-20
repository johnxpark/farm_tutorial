from pydantic import BaseModel

class Player(BaseModel):
    name: str
    number: int
    position: str