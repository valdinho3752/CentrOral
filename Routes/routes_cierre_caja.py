from typing import List
from fastapi import APIRouter
from controllers.controller_cierre_caja import CierreCajaController
from schemas.schema_cierre_caja import CierreCajaCreate, CierreCajaUpdate, CierreCajaResponse

router = APIRouter()
controller = CierreCajaController()

@router.get("/getallcierres/", response_model=List[CierreCajaResponse], operation_id="get_all_cierres")
async def get_all_cierres():
    return await controller.get_all_cierres()

@router.get("/getcierrebyid/{cierre_id}", response_model=CierreCajaResponse, operation_id="get_cierre_by_id")
async def get_cierre_by_id(cierre_id: int):
    return await controller.get_cierre_by_id(cierre_id)

@router.post("/createcierre/", response_model=CierreCajaResponse, operation_id="create_cierre")
async def create_cierre(cierre: CierreCajaCreate):
    return await controller.create_cierre(cierre)

@router.put("/updatecierre/{cierre_id}", response_model=CierreCajaResponse, operation_id="update_cierre")
async def update_cierre(cierre_id: int, cierre: CierreCajaUpdate):
    return await controller.update_cierre(cierre_id, cierre)

@router.delete("/deletecierre/{cierre_id}", response_model=CierreCajaResponse, operation_id="delete_cierre")
async def delete_cierre(cierre_id: int):
    return await controller.delete_cierre(cierre_id)
