from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class UsuarioBase(BaseModel):
    codigo: str
    nombre: str
    apellido: str
    rol_id: int
    ultima_edicion: datetime
    porcentaje: Optional[int] = None

class UsuarioCreate(UsuarioBase):
    pass

class UsuarioUpdate(UsuarioBase):
    codigo: Optional[str] = None
    nombre: Optional[str] = None
    apellido: Optional[str] = None
    rol_id: Optional[int] = None
    ultima_edicion: Optional[datetime] = None
    porcentaje: Optional[int] = None

class UsuarioResponse(UsuarioBase):
    id: int

    class Config:
        from_attributes = True
