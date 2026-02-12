from typing import List
from fastapi import APIRouter
from controllers.controller_permiso import PermisoController
from schemas.schema_permiso import PermisoCreate, PermisoUpdate, PermisoResponse

router = APIRouter()
controller = PermisoController()

@router.get("/getallpermisos/", response_model=List[PermisoResponse], operation_id="get_all_permisos")
async def get_all_permisos():
    return await controller.get_all_permisos()

@router.get("/getpermisobyid/{permiso_id}", response_model=PermisoResponse, operation_id="get_permiso_by_id")
async def get_permiso_by_id(permiso_id: int):
    return await controller.get_permiso_by_id(permiso_id)

@router.post("/createpermiso/", response_model=PermisoResponse, operation_id="create_permiso")
async def create_permiso(permiso: PermisoCreate):
    return await controller.create_permiso(permiso)

@router.put("/updatepermiso/{permiso_id}", response_model=PermisoResponse, operation_id="update_permiso")
async def update_permiso(permiso_id: int, permiso: PermisoUpdate):
    return await controller.update_permiso(permiso_id, permiso)

@router.delete("/deletepermiso/{permiso_id}", response_model=PermisoResponse, operation_id="delete_permiso")
async def delete_permiso(permiso_id: int):
    return await controller.delete_permiso(permiso_id)
