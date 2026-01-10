from pydantic import BaseModel
from typing import Optional

class DepositoDiagnosticoBase(BaseModel):
    depositos_id: int
    diagnostico_id: int
    monto_aplicado: float

class DepositoDiagnosticoCreate(DepositoDiagnosticoBase):
    pass

class DepositoDiagnosticoUpdate(DepositoDiagnosticoBase):
    depositos_id: Optional[int] = None
    diagnostico_id: Optional[int] = None
    monto_aplicado: Optional[float] = None

class DepositoDiagnosticoResponse(DepositoDiagnosticoBase):
    id: int

    class Config:
        from_attributes = True
