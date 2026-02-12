from typing import List
from fastapi import APIRouter
from controllers.controller_deposito_diagnostico import DepositoDiagnosticoController
from schemas.schema_deposito_diagnostico import DepositoDiagnosticoCreate, DepositoDiagnosticoUpdate, DepositoDiagnosticoResponse

router = APIRouter()
controller = DepositoDiagnosticoController()

@router.get("/getalldepositodiagnosticos/", response_model=List[DepositoDiagnosticoResponse], operation_id="get_all_deposito_diagnosticos")
async def get_all_deposito_diagnosticos():
    return await controller.get_all_deposito_diagnosticos()

@router.get("/getdepositodiagnosticobyid/{dd_id}", response_model=DepositoDiagnosticoResponse, operation_id="get_deposito_diagnostico_by_id")
async def get_deposito_diagnostico_by_id(dd_id: int):
    return await controller.get_deposito_diagnostico_by_id(dd_id)

@router.post("/createdepositodiagnostico/", response_model=DepositoDiagnosticoResponse, operation_id="create_deposito_diagnostico")
async def create_deposito_diagnostico(dd: DepositoDiagnosticoCreate):
    return await controller.create_deposito_diagnostico(dd)

@router.put("/updatedepositodiagnostico/{dd_id}", response_model=DepositoDiagnosticoResponse, operation_id="update_deposito_diagnostico")
async def update_deposito_diagnostico(dd_id: int, dd: DepositoDiagnosticoUpdate):
    return await controller.update_deposito_diagnostico(dd_id, dd)

@router.delete("/deletedepositodiagnostico/{dd_id}", response_model=DepositoDiagnosticoResponse, operation_id="delete_deposito_diagnostico")
async def delete_deposito_diagnostico(dd_id: int):
    return await controller.delete_deposito_diagnostico(dd_id)
