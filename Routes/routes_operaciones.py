from typing import List
from fastapi import APIRouter
from controllers.controller_operaciones import OperacionesController
from schemas.schema_operaciones import compra_insumo


router = APIRouter()
controller = OperacionesController()

@router.post("/comprar_insumo/", response_model=compra_insumo, operation_id="comprar_insumo")
async def comprar_insumo(operacion: compra_insumo):
    return await controller.comprar_insumo(operacion)