from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class TransaccionBase(BaseModel):
    tipo: str
    origen_deposito: str
    fecha_hora: datetime
    usuario_id: int
    cierre_caja_id: int

class TransaccionCreate(TransaccionBase):
    pass

class TransaccionUpdate(TransaccionBase):
    tipo: Optional[str] = None
    origen_deposito: Optional[str] = None
    fecha_hora: Optional[datetime] = None
    usuario_id: Optional[int] = None
    cierre_caja_id: Optional[int] = None

class TransaccionResponse(TransaccionBase):
    id: int

    class Config:
        from_attributes = True
