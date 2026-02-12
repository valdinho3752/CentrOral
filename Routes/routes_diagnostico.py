from typing import List
from fastapi import APIRouter
from controllers.controller_diagnostico import DiagnosticoController
from schemas.schema_diagnostico import DiagnosticoCreate, DiagnosticoUpdate, DiagnosticoResponse

router = APIRouter()
controller = DiagnosticoController()

@router.get("/getalldiagnosticos/", response_model=List[DiagnosticoResponse], operation_id="get_all_diagnosticos")
async def get_all_diagnosticos():
    return await controller.get_all_diagnosticos()

@router.get("/getdiagnosticobyid/{diagnostico_id}", response_model=DiagnosticoResponse, operation_id="get_diagnostico_by_id")
async def get_diagnostico_by_id(diagnostico_id: int):
    return await controller.get_diagnostico_by_id(diagnostico_id)

@router.post("/creatediagnostico/", response_model=DiagnosticoResponse, operation_id="create_diagnostico")
async def create_diagnostico(diagnostico: DiagnosticoCreate):
    return await controller.create_diagnostico(diagnostico)

@router.put("/updatediagnostico/{diagnostico_id}", response_model=DiagnosticoResponse, operation_id="update_diagnostico")
async def update_diagnostico(diagnostico_id: int, diagnostico: DiagnosticoUpdate):
    return await controller.update_diagnostico(diagnostico_id, diagnostico)

@router.delete("/deletediagnostico/{diagnostico_id}", response_model=DiagnosticoResponse, operation_id="delete_diagnostico")
async def delete_diagnostico(diagnostico_id: int):
    return await controller.delete_diagnostico(diagnostico_id)
