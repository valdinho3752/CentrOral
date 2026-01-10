from pydantic import BaseModel
from typing import Optional

class PacienteBase(BaseModel):
    nombres: str
    apellidos: str
    telefono: Optional[str] = None
    direccion: Optional[str] = None
    email: Optional[str] = None
    motivo_consulta: Optional[str] = None

class PacienteCreate(PacienteBase):
    pass

class PacienteUpdate(PacienteBase):
    nombres: Optional[str] = None
    apellidos: Optional[str] = None
    telefono: Optional[str] = None
    direccion: Optional[str] = None
    email: Optional[str] = None
    motivo_consulta: Optional[str] = None

class PacienteResponse(PacienteBase):
    id: int

    class Config:
        from_attributes = True
