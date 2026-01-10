from pydantic import BaseModel
from typing import Optional

class InventarioBase(BaseModel):
    nombre_insumo: str
    cantidad: int
    descripcion: Optional[str] = None

class InventarioCreate(InventarioBase):
    pass

class InventarioUpdate(InventarioBase):
    nombre_insumo: Optional[str] = None
    cantidad: Optional[int] = None
    descripcion: Optional[str] = None

class InventarioResponse(InventarioBase):
    id: int

    class Config:
        from_attributes = True
