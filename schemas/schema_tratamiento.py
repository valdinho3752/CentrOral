from pydantic import BaseModel
from typing import Optional

class TratamientoBase(BaseModel):
    nombre_tratamiento: str
    precio_economico: float
    precio_medio: Optional[float] = None
    precio_alto: Optional[float] = None

class TratamientoCreate(TratamientoBase):
    pass

class TratamientoUpdate(TratamientoBase):
    nombre_tratamiento: Optional[str] = None
    precio_economico: Optional[float] = None
    precio_medio: Optional[float] = None
    precio_alto: Optional[float] = None

class TratamientoResponse(TratamientoBase):
    id: int

    class Config:
        from_attributes = True
