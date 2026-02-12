from typing import List
from fastapi import APIRouter
from controllers.controller_comisiones import ComisionesController
from schemas.schema_comisiones import ComisionesCreate, ComisionesUpdate, ComisionesResponse

router = APIRouter()
controller = ComisionesController()

@router.get("/getallcomisiones/", response_model=List[ComisionesResponse], operation_id="get_all_comisiones")
async def get_all_comisiones():
    return await controller.get_all_comisiones()

@router.get("/getcomisionbyid/{comision_id}", response_model=ComisionesResponse, operation_id="get_comision_by_id")
async def get_comision_by_id(comision_id: int):
    return await controller.get_comision_by_id(comision_id)

@router.post("/createcomision/", response_model=ComisionesResponse, operation_id="create_comision")
async def create_comision(comision: ComisionesCreate):
    return await controller.create_comision(comision)

@router.put("/updatecomision/{comision_id}", response_model=ComisionesResponse, operation_id="update_comision")
async def update_comision(comision_id: int, comision: ComisionesUpdate):
    return await controller.update_comision(comision_id, comision)

@router.delete("/deletecomision/{comision_id}", response_model=ComisionesResponse, operation_id="delete_comision")
async def delete_comision(comision_id: int):
    return await controller.delete_comision(comision_id)
