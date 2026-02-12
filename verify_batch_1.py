import asyncio
import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from dotenv import load_dotenv
load_dotenv("database/.env")

# Controllers
from controllers.controller_paciente import PacienteController
from controllers.controller_historia_medica import HistoriaMedicaController
from controllers.controller_plan_tratamiento import PlanTratamientoController
from controllers.controller_tratamiento import TratamientoController
from controllers.controller_pieza import PiezaController
from controllers.controller_usuario import UserController

# Schemas
from schemas.schema_paciente import PacienteCreate, PacienteUpdate
from schemas.schema_historia_medica import HistoriaMedicaCreate
from schemas.schema_plan_tratamiento import PlanTratamientoCreate
from schemas.schema_tratamiento import TratamientoCreate
from schemas.schema_pieza import PiezaCreate

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

import random

async def main():
    print("Iniciando verificación Batch 1...")
    
    # 1. Instanciar controladores
    paciente_ctrl = PacienteController()
    historia_ctrl = HistoriaMedicaController()
    plan_ctrl = PlanTratamientoController()
    tratamiento_ctrl = TratamientoController()
    pieza_ctrl = PiezaController()
    user_ctrl = UserController()

    # Obtener un usuario existente para relaciones
    users = await user_ctrl.get_all_users()
    if not users:
        print("Error: No se encontraron usuarios. Ejecuta populate_db.py primero.")
        return
    user = users[0]
    print(f"Usando usuario: {user.nombre} {user.apellido} (ID: {user.id})")

    # 2. Paciente
    print("\n[Paciente] Creando...")
    p_create = PacienteCreate(
        nombres="Juan",
        apellidos="Perez",
        telefono="12345678",
        direccion="Calle Falsa 123",
        email="juan.perez@example.com",
        motivo_consulta="Dolor de muela"
    )
    paciente = await paciente_ctrl.create_paciente(p_create)
    print(f"Paciente creado: {paciente.nombres} {paciente.apellidos} (ID: {paciente.id})")

    print("[Paciente] Actaulizando...")
    p_update = PacienteUpdate(telefono="87654321")
    paciente_updated = await paciente_ctrl.update_paciente(paciente.id, p_update)
    print(f"Paciente actualizado tel: {paciente_updated.telefono}")

    # 3. Historia Medica
    print("\n[HistoriaMedica] Creando...")
    hm_create = HistoriaMedicaCreate(
        paciente_id=paciente.id,
        diabetes=True,
        alergia_penicilina=True,
        medicamento_detalle="Paracetamol ocasional"
    )
    hm = await historia_ctrl.create_historia(hm_create)
    print(f"Historia Medica creada para Paciente ID {hm.paciente_id} (ID: {hm.id})")
    print(f" - Diabetes: {hm.diabetes}")

    # 4. Tratamiento
    print("\n[Tratamiento] Creando...")
    t_create = TratamientoCreate(
        nombre_tratamiento="Limpieza Dental",
        precio_economico=150.00,
        precio_medio=200.00,
        precio_alto=250.00
    )
    tratamiento = await tratamiento_ctrl.create_tratamiento(t_create)
    print(f"Tratamiento creado: {tratamiento.nombre_tratamiento} (ID: {tratamiento.id})")

    # 5. Pieza
    print("\n[Pieza] Creando...")
    pieza_create = PiezaCreate(n_pieza=18)
    pieza = await pieza_ctrl.create_pieza(pieza_create)
    print(f"Pieza creada: {pieza.n_pieza} (ID: {pieza.id})")

    # 6. Plan Tratamiento
    print("\n[PlanTratamiento] Creando...")
    plan_create = PlanTratamientoCreate(
        precio_total=500.00,
        paciente_id=paciente.id,
        usuario_id=user.id,
        estado="Pendiente"
    )
    plan = await plan_ctrl.create_plan(plan_create)
    print(f"Plan Tratamiento creado: Estado {plan.estado}, Total {plan.precio_total} (ID: {plan.id})")

    print("\n¡Verificación Batch 1 completada con éxito!")

if __name__ == "__main__":
    if sys.platform == 'win32':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())
