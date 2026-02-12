from typing import List
from fastapi import APIRouter
from controllers.controller_compras import ComprasController
from schemas.schema_compras import ComprasCreate, ComprasUpdate, ComprasResponse

router = APIRouter()
controller = ComprasController()

@router.get("/getallcompras/", response_model=List[ComprasResponse], operation_id="get_all_compras")
async def get_all_compras():
    return await controller.get_all_compras()

@router.get("/getcomprabyid/{compra_id}", response_model=ComprasResponse, operation_id="get_compra_by_id")
async def get_compra_by_id(compra_id: int):
    return await controller.get_compra_by_id(compra_id)

@router.post("/createcompra/", response_model=ComprasResponse, operation_id="create_compra")
async def create_compra(compra: ComprasCreate):
    return await controller.create_compra(compra)

@router.put("/updatecompra/{compra_id}", response_model=ComprasResponse, operation_id="update_compra")
async def update_compra(compra_id: int, compra: ComprasUpdate):
    return await controller.update_compra(compra_id, compra)

@router.delete("/deletecompra/{compra_id}", response_model=ComprasResponse, operation_id="delete_compra")
async def delete_compra(compra_id: int):
    return await controller.delete_compra(compra_id)
