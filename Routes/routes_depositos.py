from typing import List
from fastapi import APIRouter
from controllers.controller_depositos import DepositosController
from schemas.schema_depositos import DepositosCreate, DepositosUpdate, DepositosResponse

router = APIRouter()
controller = DepositosController()

@router.get("/getalldepositos/", response_model=List[DepositosResponse], operation_id="get_all_depositos")
async def get_all_depositos():
    return await controller.get_all_depositos()

@router.get("/getdepositobyid/{deposito_id}", response_model=DepositosResponse, operation_id="get_deposito_by_id")
async def get_deposito_by_id(deposito_id: int):
    return await controller.get_deposito_by_id(deposito_id)

@router.post("/createdeposito/", response_model=DepositosResponse, operation_id="create_deposito")
async def create_deposito(deposito: DepositosCreate):
    return await controller.create_deposito(deposito)

@router.put("/updatedeposito/{deposito_id}", response_model=DepositosResponse, operation_id="update_deposito")
async def update_deposito(deposito_id: int, deposito: DepositosUpdate):
    return await controller.update_deposito(deposito_id, deposito)

@router.delete("/deletedeposito/{deposito_id}", response_model=DepositosResponse, operation_id="delete_deposito")
async def delete_deposito(deposito_id: int):
    return await controller.delete_deposito(deposito_id)
