from pydantic import BaseModel
from typing import Optional

class PermisoBase(BaseModel):
    nombre_permiso: str

class PermisoCreate(PermisoBase):
    pass

class PermisoUpdate(PermisoBase):
    nombre_permiso: Optional[str] = None

class PermisoResponse(PermisoBase):
    id: int

    class Config:
        from_attributes = True
