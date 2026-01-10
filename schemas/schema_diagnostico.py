from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class DiagnosticoBase(BaseModel):
    cara_dental: str
    precio_elegido: Optional[str] = None
    estado: str
    fecha_conclusion: Optional[datetime] = None
    precio_aplicado: float
    plan_tratamiento_id: int
    tratamiento_id: int
    pieza_id: int
    doctor_id: int
    usuario_id: int

class DiagnosticoCreate(DiagnosticoBase):
    pass

class DiagnosticoUpdate(DiagnosticoBase):
    cara_dental: Optional[str] = None
    precio_elegido: Optional[str] = None
    estado: Optional[str] = None
    fecha_conclusion: Optional[datetime] = None
    precio_aplicado: Optional[float] = None
    plan_tratamiento_id: Optional[int] = None
    tratamiento_id: Optional[int] = None
    pieza_id: Optional[int] = None
    doctor_id: Optional[int] = None
    usuario_id: Optional[int] = None

class DiagnosticoResponse(DiagnosticoBase):
    id: int

    class Config:
        from_attributes = True
