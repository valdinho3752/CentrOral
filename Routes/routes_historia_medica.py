from typing import List
from fastapi import APIRouter
from controllers.controller_historia_medica import HistoriaMedicaController
from schemas.schema_historia_medica import HistoriaMedicaCreate, HistoriaMedicaUpdate, HistoriaMedicaResponse

router = APIRouter()
controller = HistoriaMedicaController()

@router.get("/getallhistorias/", response_model=List[HistoriaMedicaResponse], operation_id="get_all_historias")
async def get_all_historias():
    return await controller.get_all_historias()

@router.get("/gethistoriabyid/{historia_id}", response_model=HistoriaMedicaResponse, operation_id="get_historia_by_id")
async def get_historia_by_id(historia_id: int):
    return await controller.get_historia_by_id(historia_id)

@router.get("/gethistoriabypacienteid/{paciente_id}", response_model=HistoriaMedicaResponse, operation_id="get_historia_by_paciente_id")
async def get_historia_by_paciente_id(paciente_id: int):
    return await controller.get_historia_by_paciente_id(paciente_id)

@router.post("/createhistoria/", response_model=HistoriaMedicaResponse, operation_id="create_historia")
async def create_historia(historia: HistoriaMedicaCreate):
    return await controller.create_historia(historia)

@router.put("/updatehistoria/{historia_id}", response_model=HistoriaMedicaResponse, operation_id="update_historia")
async def update_historia(historia_id: int, historia: HistoriaMedicaUpdate):
    return await controller.update_historia(historia_id, historia)

@router.delete("/deletehistoria/{historia_id}", response_model=HistoriaMedicaResponse, operation_id="delete_historia")
async def delete_historia(historia_id: int):
    return await controller.delete_historia(historia_id)
