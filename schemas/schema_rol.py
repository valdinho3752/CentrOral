from pydantic import BaseModel
from typing import Optional

class RolBase(BaseModel):
    nombre_rol: str

class RolCreate(RolBase):
    pass

class RolUpdate(RolBase):
    nombre_rol: Optional[str] = None

class RolResponse(RolBase):
    id: int

    class Config:
        from_attributes = True
