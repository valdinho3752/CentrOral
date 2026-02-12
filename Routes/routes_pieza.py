from typing import List
from fastapi import APIRouter
from controllers.controller_pieza import PiezaController
from schemas.schema_pieza import PiezaCreate, PiezaUpdate, PiezaResponse

router = APIRouter()
controller = PiezaController()

@router.get("/getallpiezas/", response_model=List[PiezaResponse], operation_id="get_all_piezas")
async def get_all_piezas():
    return await controller.get_all_piezas()

@router.get("/getpiezabyid/{pieza_id}", response_model=PiezaResponse, operation_id="get_pieza_by_id")
async def get_pieza_by_id(pieza_id: int):
    return await controller.get_pieza_by_id(pieza_id)

@router.post("/createpieza/", response_model=PiezaResponse, operation_id="create_pieza")
async def create_pieza(pieza: PiezaCreate):
    return await controller.create_pieza(pieza)

@router.put("/updatepieza/{pieza_id}", response_model=PiezaResponse, operation_id="update_pieza")
async def update_pieza(pieza_id: int, pieza: PiezaUpdate):
    return await controller.update_pieza(pieza_id, pieza)

@router.delete("/deletepieza/{pieza_id}", response_model=PiezaResponse, operation_id="delete_pieza")
async def delete_pieza(pieza_id: int):
    return await controller.delete_pieza(pieza_id)
