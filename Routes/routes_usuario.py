from typing import List
from fastapi import APIRouter
from controllers.controller_usuario import UserController
from schemas.schema_usuario import UsuarioCreate, UsuarioUpdate, UsuarioResponse

router = APIRouter()
controller = UserController()

@router.get("/getallusers/", response_model=List[UsuarioResponse], operation_id="get_all_users")
async def get_all_users():
    return await controller.get_all_users()

@router.get("/getuserbyid/{user_id}", response_model=UsuarioResponse, operation_id="get_user_by_id")
async def get_user_by_id(user_id: int):
    return await controller.get_user_by_id(user_id)

@router.post("/createuser/", response_model=UsuarioResponse, operation_id="create_user")
async def create_user(user: UsuarioCreate):
    return await controller.create_user(user)

@router.put("/updateuser/{user_id}", response_model=UsuarioResponse, operation_id="update_user")
async def update_user(user_id: int, user: UsuarioUpdate):
    return await controller.update_user(user_id, user)

@router.delete("/deleteuser/{user_id}", response_model=UsuarioResponse, operation_id="delete_user")
async def delete_user(user_id: int):
    return await controller.delete_user(user_id)
