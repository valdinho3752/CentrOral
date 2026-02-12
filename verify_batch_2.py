import asyncio
import sys
import os
from datetime import date, datetime

sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from dotenv import load_dotenv
load_dotenv("database/.env")

# Controllers
from controllers.controller_seguimiento_paciente import SeguimientoPacienteController
from controllers.controller_diagnostico import DiagnosticoController
from controllers.controller_inventario import InventarioController
from controllers.controller_cierre_caja import CierreCajaController
from controllers.controller_transaccion import TransaccionController

# Controllers for dependencies (from Batch 1 or User)
from controllers.controller_usuario import UserController
from controllers.controller_plan_tratamiento import PlanTratamientoController
from controllers.controller_tratamiento import TratamientoController
from controllers.controller_pieza import PiezaController

# Schemas
from schemas.schema_seguimiento_paciente import SeguimientoPacienteCreate, SeguimientoPacienteUpdate
from schemas.schema_diagnostico import DiagnosticoCreate
from schemas.schema_inventario import InventarioCreate, InventarioUpdate
from schemas.schema_cierre_caja import CierreCajaCreate
from schemas.schema_transaccion import TransaccionCreate

# Import ALL models to ensure relationships resolve
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
    print("Iniciando verificación Batch 2...")
    
    # Instanciar controladores
    seguimiento_ctrl = SeguimientoPacienteController()
    diagnostico_ctrl = DiagnosticoController()
    inventario_ctrl = InventarioController()
    cierre_ctrl = CierreCajaController()
    transaccion_ctrl = TransaccionController()

    user_ctrl = UserController()
    plan_ctrl = PlanTratamientoController()
    trat_ctrl = TratamientoController()
    pieza_ctrl = PiezaController()

    # Obtener dependencias (Asumiendo que Batch 1 y Populate DB se ejecutaron)
    users = await user_ctrl.get_all_users()
    planes = await plan_ctrl.get_all_planes()
    tramientos = await trat_ctrl.get_all_tratamientos()
    piezas = await pieza_ctrl.get_all_piezas()

    if not all([users, planes, tramientos, piezas]):
        print("Error: Faltan dependencias. Ejecuta populate_db.py y verify_batch_1.py primero.")
        return

    user = users[0]
    plan = planes[0]
    tratamiento = tramientos[0]
    pieza = piezas[0]

    print(f"Dependencias OK: User {user.id}, Plan {plan.id}, Tratamiento {tratamiento.id}, Pieza {pieza.id}")

    # 1. Inventario (Sin deps)
    print("\n[Inventario] Creando...")
    inv_create = InventarioCreate(
        nombre_insumo="Guantes Latex",
        cantidad=100,
        descripcion="Caja de 100 unidades"
    )
    inv = await inventario_ctrl.create_inventario(inv_create)
    print(f"Inventario creado: {inv.nombre_insumo} ({inv.cantidad}) ID: {inv.id}")
    
    # Update Inventario (Partial)
    print("[Inventario] Actualizando (retirando 10)...")
    inv_update = InventarioUpdate(cantidad=90)
    inv = await inventario_ctrl.update_inventario(inv.id, inv_update)
    print(f"Inventario actualizado: {inv.cantidad} (Descripción mantiene: {inv.descripcion is not None})")

    # 2. Seguimiento Paciente
    print("\n[SeguimientoPaciente] Creando...")
    seg_create = SeguimientoPacienteCreate(
        fecha=date.today(),
        descripcion="Paciente reporta molestia leve",
        plan_tratamiento_id=plan.id,
        usuario_id=user.id,
        pieza_id=pieza.id
    )
    seg = await seguimiento_ctrl.create_seguimiento(seg_create)
    print(f"Seguimiento creado ID: {seg.id}, Fecha: {seg.fecha}")

    # 3. Diagnostico
    print("\n[Diagnostico] Creando...")
    diag_create = DiagnosticoCreate(
        cara_dental="Vestibular",
        estado="Pendiente",
        precio_aplicado=150.00,
        plan_tratamiento_id=plan.id,
        tratamiento_id=tratamiento.id,
        pieza_id=pieza.id,
        doctor_id=user.id,
        usuario_id=user.id
    )
    diag = await diagnostico_ctrl.create_diagnostico(diag_create)
    print(f"Diagnostico creado ID: {diag.id}, Cara: {diag.cara_dental}")

    # 4. Cierre Caja
    print("\n[CierreCaja] Creando...")
    cierre_create = CierreCajaCreate(
        fecha_inicio=datetime.now(),
        fecha_cierre=datetime.now(),
        total_ingresos=1000.00,
        total_egresos=200.00,
        total_diario=800.00,
        total_acumulado=5000.00,
        usuario_id=user.id
    )
    cierre = await cierre_ctrl.create_cierre(cierre_create)
    print(f"CierreCaja creado ID: {cierre.id}, Total Diario: {cierre.total_diario}")

    # 5. Transaccion
    print("\n[Transaccion] Creando...")
    trans_create = TransaccionCreate(
        tipo="Ingreso",
        origen_deposito="Pago Consulta",
        fecha_hora=datetime.now(),
        usuario_id=user.id,
        cierre_caja_id=cierre.id
    )
    trans = await transaccion_ctrl.create_transaccion(trans_create)
    print(f"Transaccion creada ID: {trans.id}, Tipo: {trans.tipo}")

    print("\n¡Verificación Batch 2 completada con éxito!")

if __name__ == "__main__":
    if sys.platform == 'win32':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())
