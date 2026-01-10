from pydantic import BaseModel
from typing import Optional
from datetime import date

class ComprasBase(BaseModel):
    fecha: date
    precio_compra: float
    cantidad: int
    usuario_id: int
    inventario_id: int
    transaccion_id: int

class ComprasCreate(ComprasBase):
    pass

class ComprasUpdate(ComprasBase):
    fecha: Optional[date] = None
    precio_compra: Optional[float] = None
    cantidad: Optional[int] = None
    usuario_id: Optional[int] = None
    inventario_id: Optional[int] = None
    transaccion_id: Optional[int] = None

class ComprasResponse(ComprasBase):
    id: int

    class Config:
        from_attributes = True
