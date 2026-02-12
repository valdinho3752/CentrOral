from typing import List
from fastapi import APIRouter
from controllers.controller_transaccion import TransaccionController
from schemas.schema_transaccion import TransaccionCreate, TransaccionUpdate, TransaccionResponse

router = APIRouter()
controller = TransaccionController()

@router.get("/getalltransacciones/", response_model=List[TransaccionResponse], operation_id="get_all_transacciones")
async def get_all_transacciones():
    return await controller.get_all_transacciones()

@router.get("/gettransaccionbyid/{transaccion_id}", response_model=TransaccionResponse, operation_id="get_transaccion_by_id")
async def get_transaccion_by_id(transaccion_id: int):
    return await controller.get_transaccion_by_id(transaccion_id)

@router.post("/createtransaccion/", response_model=TransaccionResponse, operation_id="create_transaccion")
async def create_transaccion(transaccion: TransaccionCreate):
    return await controller.create_transaccion(transaccion)

@router.put("/updatetransaccion/{transaccion_id}", response_model=TransaccionResponse, operation_id="update_transaccion")
async def update_transaccion(transaccion_id: int, transaccion: TransaccionUpdate):
    return await controller.update_transaccion(transaccion_id, transaccion)

@router.delete("/deletetransaccion/{transaccion_id}", response_model=TransaccionResponse, operation_id="delete_transaccion")
async def delete_transaccion(transaccion_id: int):
    return await controller.delete_transaccion(transaccion_id)
