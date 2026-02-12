import asyncio
import sys
import os
from datetime import datetime

# Asegurar que el directorio raíz está en el path
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from dotenv import load_dotenv
# Cargar variables de entorno apuntando específicamente a database/.env
load_dotenv("database/.env")

from controllers.controller_permiso import PermisoController
from controllers.controller_rol import RolController
from controllers.controller_rol_permiso import RolPermisoController
from controllers.controller_usuario import UserController

from schemas.schema_permiso import PermisoCreate
from schemas.schema_rol import RolCreate
from schemas.schema_rol_permiso import RolPermisoCreate
from schemas.schema_usuario import UsuarioCreate

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
    print("Iniciando población de la base de datos...")

    # Instanciar controladores
    permiso_ctrl = PermisoController()
    rol_ctrl = RolController()
    rol_permiso_ctrl = RolPermisoController()
    user_ctrl = UserController()

    # 1. Crear Permisos (6 permisos)
    permisos_data = [
        "gestionar_usuarios",
        "ver_pacientes",
        "editar_historia_clinica",
        "gestionar_citas",
        "ver_reportes_financieros",
        "gestionar_inventario"
    ]
    
    permisos_objs = []
    print("Creando Permisos...")
    for p_name in permisos_data:
        p_create = PermisoCreate(nombre_permiso=p_name)
        p_obj = await permiso_ctrl.create_permiso(p_create)
        permisos_objs.append(p_obj)
        print(f" - Permiso creado: {p_obj.nombre_permiso} (ID: {p_obj.id})")

    # Mapeo de permisos para fácil acceso
    perms = {p.nombre_permiso: p for p in permisos_objs}

    # 2. Crear Roles (3 roles)
    roles_data = ["Administrador", "Doctor", "Asistente"]
    roles_objs = []
    
    print("\nCreando Roles...")
    for r_name in roles_data:
        r_create = RolCreate(nombre_rol=r_name)
        r_obj = await rol_ctrl.create_rol(r_create)
        roles_objs.append(r_obj)
        print(f" - Rol creado: {r_obj.nombre_rol} (ID: {r_obj.id})")

    roles = {r.nombre_rol: r for r in roles_objs}

    # 3. Asignar Permisos a Roles
    # Admin: Todos
    # Doctor: ver_pacientes, editar_historia_clinica, gestionar_citas
    # Asistente: ver_pacientes, gestionar_citas, gestionar_inventario
    
    allocations = [
        ("Administrador", permisos_data),
        ("Doctor", ["ver_pacientes", "editar_historia_clinica", "gestionar_citas"]),
        ("Asistente", ["ver_pacientes", "gestionar_citas", "gestionar_inventario"])
    ]

    print("\nAsignando Permisos a Roles...")
    for rol_name, perm_list in allocations:
        rol = roles[rol_name]
        for perm_name in perm_list:
            perm = perms[perm_name]
            rp_create = RolPermisoCreate(rol_id=rol.id, permiso_id=perm.id)
            await rol_permiso_ctrl.create_rol_permiso(rp_create)
            print(f" - Asignado {perm_name} a {rol_name}")

    # 4. Crear Usuarios (2 usuarios)
    print("\nCreando Usuarios...")
    
    # Usuario 1: Admin
    admin_create = UsuarioCreate(
        codigo="ADM001",
        nombre="Admin",
        apellido="SuperUser",
        rol_id=roles["Administrador"].id,
        ultima_edicion=datetime.now(),
        porcentaje=0
    )
    user_admin = await user_ctrl.create_user(admin_create)
    print(f" - Usuario creado: {user_admin.nombre} {user_admin.apellido} con Rol Administrador")

    # Usuario 2: Doctor
    doctor_create = UsuarioCreate(
        codigo="DOC001",
        nombre="Gregory",
        apellido="House",
        rol_id=roles["Doctor"].id,
        ultima_edicion=datetime.now(),
        porcentaje=50
    )
    user_doctor = await user_ctrl.create_user(doctor_create)
    print(f" - Usuario creado: {user_doctor.nombre} {user_doctor.apellido} con Rol Doctor")

    print("\n¡Población completada con éxito!")

if __name__ == "__main__":
    if sys.platform == 'win32':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())
