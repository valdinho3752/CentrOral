from typing import List
from fastapi import APIRouter
from controllers.controller_rol import RolController
from schemas.schema_rol import RolCreate, RolUpdate, RolResponse

router = APIRouter()
controller = RolController()

@router.get("/getallroles/", response_model=List[RolResponse], operation_id="get_all_roles")
async def get_all_roles():
    return await controller.get_all_rols()

@router.get("/getrolbyid/{rol_id}", response_model=RolResponse, operation_id="get_rol_by_id")
async def get_rol_by_id(rol_id: int):
    return await controller.get_rol_by_id(rol_id)

@router.post("/createrol/", response_model=RolResponse, operation_id="create_rol")
async def create_rol(rol: RolCreate):
    return await controller.create_rol(rol)

@router.put("/updaterol/{rol_id}", response_model=RolResponse, operation_id="update_rol")
async def update_rol(rol_id: int, rol: RolUpdate):
    return await controller.update_rol(rol_id, rol)

@router.delete("/deleterol/{rol_id}", response_model=RolResponse, operation_id="delete_rol")
async def delete_rol(rol_id: int):
    return await controller.delete_rol(rol_id)
