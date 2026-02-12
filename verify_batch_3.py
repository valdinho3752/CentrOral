import asyncio
import sys
import os
from datetime import date, datetime

sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from dotenv import load_dotenv
load_dotenv("database/.env")

# Controllers
from controllers.controller_compras import ComprasController
from controllers.controller_comisiones import ComisionesController
from controllers.controller_depositos import DepositosController
from controllers.controller_deposito_diagnostico import DepositoDiagnosticoController

# Dependency Controllers
from controllers.controller_usuario import UserController
from controllers.controller_inventario import InventarioController
from controllers.controller_transaccion import TransaccionController
from controllers.controller_cierre_caja import CierreCajaController
from controllers.controller_plan_tratamiento import PlanTratamientoController
from controllers.controller_diagnostico import DiagnosticoController

# Schemas
from schemas.schema_compras import ComprasCreate
from schemas.schema_comisiones import ComisionesCreate
from schemas.schema_depositos import DepositosCreate
from schemas.schema_deposito_diagnostico import DepositoDiagnosticoCreate

# Import ALL models
from models.model_cierre_caja import CierreCaja
from models.model_comisiones import Comisiones
from models.model_compras import Compras
from models.model_depositos import Depositos
from models.model_deposito_diagnostico import DepositoDiagnostico
from models.model_historia_medica import HistoriaMedica
from models.model_inventario import Inventario
from models.model_paciente import Paciente
from models.model_plan_tratamiento import PlanTratamiento
from models.model_permiso import Permiso
from models.model_rol import Rol
from models.model_rol_permiso import RolPermiso
from models.model_transaccion import Transaccion
from models.model_usuario import Usuario
from models.model_diagnostico import Diagnostico
from models.model_pieza import Pieza
from models.model_tratamiento import Tratamiento
from models.model_seguimiento_paciente import SeguimientoPaciente


async def main():
    print("Iniciando verificación Batch 3...")
    
    # Controllers
    compras_ctrl = ComprasController()
    comisiones_ctrl = ComisionesController()
    depositos_ctrl = DepositosController()
    dd_ctrl = DepositoDiagnosticoController()

    user_ctrl = UserController()
    inv_ctrl = InventarioController()
    trans_ctrl = TransaccionController()
    cierre_ctrl = CierreCajaController()
    plan_ctrl = PlanTratamientoController()
    diag_ctrl = DiagnosticoController()

    # Get dependencies
    users = await user_ctrl.get_all_users()
    invs = await inv_ctrl.get_all_inventarios()
    transacciones = await trans_ctrl.get_all_transacciones()
    cierres = await cierre_ctrl.get_all_cierres()
    planes = await plan_ctrl.get_all_planes()
    diagnosticos = await diag_ctrl.get_all_diagnosticos()

    if not all([users, invs, transacciones, cierres, planes, diagnosticos]):
        print("Error: Faltan dependencias. Ejecuta batches 1 y 2 primero.")
        return

    user = users[0]
    inventario = invs[0]
    transaccion = transacciones[0]
    cierre = cierres[0]
    plan = planes[0]
    diagnostico = diagnosticos[0]

    print(f"Dependencias OK: Inv {inventario.id}, Trans {transaccion.id}, Cierre {cierre.id}")

    # 1. Compras
    print("\n[Compras] Creando...")
    compra_create = ComprasCreate(
        fecha=date.today(),
        precio_compra=50.00,
        cantidad=10,
        usuario_id=user.id,
        inventario_id=inventario.id,
        transaccion_id=transaccion.id
    )
    compra = await compras_ctrl.create_compra(compra_create)
    print(f"Compra creada ID: {compra.id}, Precio: {compra.precio_compra}")

    # 2. Comisiones
    print("\n[Comisiones] Creando...")
    comision_create = ComisionesCreate(
        comision_total=25.50,
        usuario_id=user.id,
        cierre_caja_id=cierre.id
    )
    comision = await comisiones_ctrl.create_comision(comision_create)
    print(f"Comision creada ID: {comision.id}, Total: {comision.comision_total}")

    # 3. Depositos
    print("\n[Depositos] Creando...")
    dep_create = DepositosCreate(
        fecha=date.today(),
        deposito=100.00,
        saldo=400.00,
        usuario_id=user.id,
        plan_tratamiento_id=plan.id,
        transaccion_id=transaccion.id
    )
    deposito = await depositos_ctrl.create_deposito(dep_create)
    print(f"Deposito creado ID: {deposito.id}, Monto: {deposito.deposito}")

    # 4. Deposito Diagnostico
    print("\n[DepositoDiagnostico] Creando...")
    dd_create = DepositoDiagnosticoCreate(
        depositos_id=deposito.id,
        diagnostico_id=diagnostico.id,
        monto_aplicado=50.00
    )
    dd = await dd_ctrl.create_deposito_diagnostico(dd_create)
    print(f"DepositoDiagnostico creado ID: {dd.id}, Aplicado: {dd.monto_aplicado}")

    print("\n¡Verificación Batch 3 completada con éxito!")

if __name__ == "__main__":
    if sys.platform == 'win32':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())
