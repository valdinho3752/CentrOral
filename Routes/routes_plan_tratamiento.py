from typing import List
from fastapi import APIRouter
from controllers.controller_plan_tratamiento import PlanTratamientoController
from schemas.schema_plan_tratamiento import PlanTratamientoCreate, PlanTratamientoUpdate, PlanTratamientoResponse

router = APIRouter()
controller = PlanTratamientoController()

@router.get("/getallplanes/", response_model=List[PlanTratamientoResponse], operation_id="get_all_planes")
async def get_all_planes():
    return await controller.get_all_planes()

@router.get("/getplanbyid/{plan_id}", response_model=PlanTratamientoResponse, operation_id="get_plan_by_id")
async def get_plan_by_id(plan_id: int):
    return await controller.get_plan_by_id(plan_id)

@router.post("/createplan/", response_model=PlanTratamientoResponse, operation_id="create_plan")
async def create_plan(plan: PlanTratamientoCreate):
    return await controller.create_plan(plan)

@router.put("/updateplan/{plan_id}", response_model=PlanTratamientoResponse, operation_id="update_plan")
async def update_plan(plan_id: int, plan: PlanTratamientoUpdate):
    return await controller.update_plan(plan_id, plan)

@router.delete("/deleteplan/{plan_id}", response_model=PlanTratamientoResponse, operation_id="delete_plan")
async def delete_plan(plan_id: int):
    return await controller.delete_plan(plan_id)
