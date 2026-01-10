from pydantic import BaseModel
from typing import Optional
from datetime import date

class SeguimientoPacienteBase(BaseModel):
    fecha: date
    descripcion: Optional[str] = None
    plan_tratamiento_id: int
    usuario_id: int
    pieza_id: int

class SeguimientoPacienteCreate(SeguimientoPacienteBase):
    pass

class SeguimientoPacienteUpdate(SeguimientoPacienteBase):
    fecha: Optional[date] = None
    descripcion: Optional[str] = None
    plan_tratamiento_id: Optional[int] = None
    usuario_id: Optional[int] = None
    pieza_id: Optional[int] = None

class SeguimientoPacienteResponse(SeguimientoPacienteBase):
    id: int

    class Config:
        from_attributes = True
