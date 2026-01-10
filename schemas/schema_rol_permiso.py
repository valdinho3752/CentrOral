from pydantic import BaseModel
from typing import Optional

class RolPermisoBase(BaseModel):
    rol_id: int
    permiso_id: int

class RolPermisoCreate(RolPermisoBase):
    pass

class RolPermisoUpdate(RolPermisoBase):
    rol_id: Optional[int] = None
    permiso_id: Optional[int] = None

class RolPermisoResponse(RolPermisoBase):
    id: int

    class Config:
        from_attributes = True
