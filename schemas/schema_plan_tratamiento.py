from pydantic import BaseModel
from typing import Optional

class PlanTratamientoBase(BaseModel):
    precio_total: float
    paciente_id: int
    usuario_id: int
    estado: str

class PlanTratamientoCreate(PlanTratamientoBase):
    pass

class PlanTratamientoUpdate(PlanTratamientoBase):
    precio_total: Optional[float] = None
    paciente_id: Optional[int] = None
    usuario_id: Optional[int] = None
    estado: Optional[str] = None

class PlanTratamientoResponse(PlanTratamientoBase):
    id: int

    class Config:
        from_attributes = True
