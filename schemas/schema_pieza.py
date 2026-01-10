from pydantic import BaseModel
from typing import Optional

class PiezaBase(BaseModel):
    n_pieza: int

class PiezaCreate(PiezaBase):
    pass

class PiezaUpdate(PiezaBase):
    n_pieza: Optional[int] = None

class PiezaResponse(PiezaBase):
    id: int

    class Config:
        from_attributes = True
