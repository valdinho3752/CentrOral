from typing import List
from fastapi import APIRouter
from controllers.controller_paciente import PacienteController
from schemas.schema_paciente import PacienteCreate, PacienteUpdate, PacienteResponse

router = APIRouter()
controller = PacienteController()

@router.get("/getallpacientes/", response_model=List[PacienteResponse], operation_id="get_all_pacientes")
async def get_all_pacientes():
    return await controller.get_all_pacientes()

@router.get("/getpacientebyid/{paciente_id}", response_model=PacienteResponse, operation_id="get_paciente_by_id")
async def get_paciente_by_id(paciente_id: int):
    return await controller.get_paciente_by_id(paciente_id)

@router.post("/createpaciente/", response_model=PacienteResponse, operation_id="create_paciente")
async def create_paciente(paciente: PacienteCreate):
    return await controller.create_paciente(paciente)

@router.put("/updatepaciente/{paciente_id}", response_model=PacienteResponse, operation_id="update_paciente")
async def update_paciente(paciente_id: int, paciente: PacienteUpdate):
    return await controller.update_paciente(paciente_id, paciente)

@router.delete("/deletepaciente/{paciente_id}", response_model=PacienteResponse, operation_id="delete_paciente")
async def delete_paciente(paciente_id: int):
    return await controller.delete_paciente(paciente_id)
