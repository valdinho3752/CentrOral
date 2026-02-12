from typing import List
from fastapi import APIRouter
from controllers.controller_inventario import InventarioController
from schemas.schema_inventario import InventarioCreate, InventarioUpdate, InventarioResponse

router = APIRouter()
controller = InventarioController()

@router.get("/getallinventarios/", response_model=List[InventarioResponse], operation_id="get_all_inventarios")
async def get_all_inventarios():
    return await controller.get_all_inventarios()

@router.get("/getinventariobyid/{inventario_id}", response_model=InventarioResponse, operation_id="get_inventario_by_id")
async def get_inventario_by_id(inventario_id: int):
    return await controller.get_inventario_by_id(inventario_id)

@router.post("/createinventario/", response_model=InventarioResponse, operation_id="create_inventario")
async def create_inventario(inventario: InventarioCreate):
    return await controller.create_inventario(inventario)

@router.put("/updateinventario/{inventario_id}", response_model=InventarioResponse, operation_id="update_inventario")
async def update_inventario(inventario_id: int, inventario: InventarioUpdate):
    return await controller.update_inventario(inventario_id, inventario)

@router.delete("/deleteinventario/{inventario_id}", response_model=InventarioResponse, operation_id="delete_inventario")
async def delete_inventario(inventario_id: int):
    return await controller.delete_inventario(inventario_id)
