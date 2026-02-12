from typing import List
from fastapi import APIRouter
from controllers.controller_seguimiento_paciente import SeguimientoPacienteController
from schemas.schema_seguimiento_paciente import SeguimientoPacienteCreate, SeguimientoPacienteUpdate, SeguimientoPacienteResponse

router = APIRouter()
controller = SeguimientoPacienteController()

@router.get("/getallseguimientos/", response_model=List[SeguimientoPacienteResponse], operation_id="get_all_seguimientos")
async def get_all_seguimientos():
    return await controller.get_all_seguimientos()

@router.get("/getseguimientobyid/{seguimiento_id}", response_model=SeguimientoPacienteResponse, operation_id="get_seguimiento_by_id")
async def get_seguimiento_by_id(seguimiento_id: int):
    return await controller.get_seguimiento_by_id(seguimiento_id)

@router.post("/createseguimiento/", response_model=SeguimientoPacienteResponse, operation_id="create_seguimiento")
async def create_seguimiento(seguimiento: SeguimientoPacienteCreate):
    return await controller.create_seguimiento(seguimiento)

@router.put("/updateseguimiento/{seguimiento_id}", response_model=SeguimientoPacienteResponse, operation_id="update_seguimiento")
async def update_seguimiento(seguimiento_id: int, seguimiento: SeguimientoPacienteUpdate):
    return await controller.update_seguimiento(seguimiento_id, seguimiento)

@router.delete("/deleteseguimiento/{seguimiento_id}", response_model=SeguimientoPacienteResponse, operation_id="delete_seguimiento")
async def delete_seguimiento(seguimiento_id: int):
    return await controller.delete_seguimiento(seguimiento_id)
