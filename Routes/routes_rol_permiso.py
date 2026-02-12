from typing import List
from fastapi import APIRouter
from controllers.controller_rol_permiso import RolPermisoController
from schemas.schema_rol_permiso import RolPermisoCreate, RolPermisoUpdate, RolPermisoResponse

router = APIRouter()
controller = RolPermisoController()

@router.get("/getallrolpermisos/", response_model=List[RolPermisoResponse], operation_id="get_all_rol_permisos")
async def get_all_rol_permisos():
    return await controller.get_all_rol_permisos()

@router.get("/getrolpermisobyid/{rol_permiso_id}", response_model=RolPermisoResponse, operation_id="get_rol_permiso_by_id")
async def get_rol_permiso_by_id(rol_permiso_id: int):
    return await controller.get_rol_permiso_by_id(rol_permiso_id)

@router.post("/createrolpermiso/", response_model=RolPermisoResponse, operation_id="create_rol_permiso")
async def create_rol_permiso(rol_permiso: RolPermisoCreate):
    return await controller.create_rol_permiso(rol_permiso)

@router.put("/updaterolpermiso/{rol_permiso_id}", response_model=RolPermisoResponse, operation_id="update_rol_permiso")
async def update_rol_permiso(rol_permiso_id: int, rol_permiso: RolPermisoUpdate):
    return await controller.update_rol_permiso(rol_permiso_id, rol_permiso)

@router.delete("/deleterolpermiso/{rol_permiso_id}", response_model=RolPermisoResponse, operation_id="delete_rol_permiso")
async def delete_rol_permiso(rol_permiso_id: int):
    return await controller.delete_rol_permiso(rol_permiso_id)
