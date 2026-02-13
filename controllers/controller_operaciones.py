from controllers.controller_inventario import InventarioController
from controllers.controller_compras import ComprasController
from controllers.controller_transaccion import TransaccionController
from schemas.schema_operaciones import *
from schemas.schema_inventario import *
from schemas.schema_compras import *
from schemas.schema_transaccion import *
import datetime

class OperacionesController:
    def __init__(self):
        self.inventario_controller = InventarioController()
        self.compras_controller = ComprasController()
        self.transaccion_controller = TransaccionController()
    
    async def comprar_insumo(self, operacion: compra_insumo):
        new_transaccion = TransaccionCreate(
            tipo= "Egreso",
            origen_deposito= "caja",
            fecha_hora=datetime.datetime.now(),
            usuario_id=operacion.ID_usuario,
            cierre_caja_id=operacion.ID_cierre_caja
        )
        transaccion = await self.transaccion_controller.create_transaccion(new_transaccion)

        new_compra = ComprasCreate(
            fecha=datetime.date.today(),
            precio_compra=operacion.precio_compra,
            cantidad=operacion.cantidad,
            usuario_id=operacion.ID_usuario,
            inventario_id=operacion.ID_inventario,
            transaccion_id=transaccion.id
        )
        await self.compras_controller.create_compra(new_compra)

        insumo = await self.inventario_controller.get_inventario_by_id(operacion.ID_inventario)
        new_cantidad = insumo.cantidad + operacion.cantidad
        
        inventario_update = InventarioUpdate(cantidad=new_cantidad)
        await self.inventario_controller.update_inventario(operacion.ID_inventario, inventario_update)
        return operacion





        