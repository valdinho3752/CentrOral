from typing import List
from fastapi import APIRouter
from controllers.controller_tratamiento import TratamientoController
from schemas.schema_tratamiento import TratamientoCreate, TratamientoUpdate, TratamientoResponse

router = APIRouter()
controller = TratamientoController()

@router.get("/getalltratamientos/", response_model=List[TratamientoResponse], operation_id="get_all_tratamientos")
async def get_all_tratamientos():
    return await controller.get_all_tratamientos()

@router.get("/gettratamientobyid/{tratamiento_id}", response_model=TratamientoResponse, operation_id="get_tratamiento_by_id")
async def get_tratamiento_by_id(tratamiento_id: int):
    return await controller.get_tratamiento_by_id(tratamiento_id)

@router.post("/createtratamiento/", response_model=TratamientoResponse, operation_id="create_tratamiento")
async def create_tratamiento(tratamiento: TratamientoCreate):
    return await controller.create_tratamiento(tratamiento)

@router.put("/updatetratamiento/{tratamiento_id}", response_model=TratamientoResponse, operation_id="update_tratamiento")
async def update_tratamiento(tratamiento_id: int, tratamiento: TratamientoUpdate):
    return await controller.update_tratamiento(tratamiento_id, tratamiento)

@router.delete("/deletetratamiento/{tratamiento_id}", response_model=TratamientoResponse, operation_id="delete_tratamiento")
async def delete_tratamiento(tratamiento_id: int):
    return await controller.delete_tratamiento(tratamiento_id)
