from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class CierreCajaBase(BaseModel):
    fecha_inicio: datetime
    fecha_cierre: Optional[datetime] = None
    total_ingresos: Optional[float] = None
    total_egresos: Optional[float] = None
    total_diario: Optional[float] = None
    total_acumulado: Optional[float] = None
    usuario_id: int

class CierreCajaCreate(CierreCajaBase):
    pass

class CierreCajaUpdate(CierreCajaBase):
    fecha_inicio: Optional[datetime] = None
    fecha_cierre: Optional[datetime] = None
    total_ingresos: Optional[float] = None
    total_egresos: Optional[float] = None
    total_diario: Optional[float] = None
    total_acumulado: Optional[float] = None
    usuario_id: Optional[int] = None

class CierreCajaResponse(CierreCajaBase):
    id: int

    class Config:
        from_attributes = True
