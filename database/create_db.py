import sys
import os

# Agregamos el directorio raiz al path para poder importar models y database correctamente
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from database.conection import Base, engine
import asyncio
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

async def create_db():

    async with engine.begin() as conn:

        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

if sys.platform == 'win32':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

asyncio.run(create_db())