from pydantic import BaseModel
from typing import Optional
from datetime import date

class DepositosBase(BaseModel):
    fecha: date
    deposito: float
    saldo: float
    usuario_id: int
    plan_tratamiento_id: int
    transaccion_id: int

class DepositosCreate(DepositosBase):
    pass

class DepositosUpdate(DepositosBase):
    fecha: Optional[date] = None
    deposito: Optional[float] = None
    saldo: Optional[float] = None
    usuario_id: Optional[int] = None
    plan_tratamiento_id: Optional[int] = None
    transaccion_id: Optional[int] = None

class DepositosResponse(DepositosBase):
    id: int

    class Config:
        from_attributes = True
