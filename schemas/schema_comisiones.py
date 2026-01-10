from pydantic import BaseModel
from typing import Optional

class ComisionesBase(BaseModel):
    comision_total: float
    usuario_id: int
    cierre_caja_id: int

class ComisionesCreate(ComisionesBase):
    pass

class ComisionesUpdate(ComisionesBase):
    comision_total: Optional[float] = None
    usuario_id: Optional[int] = None
    cierre_caja_id: Optional[int] = None

class ComisionesResponse(ComisionesBase):
    id: int

    class Config:
        from_attributes = True
