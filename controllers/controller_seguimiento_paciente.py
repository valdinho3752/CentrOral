from models.model_seguimiento_paciente import SeguimientoPaciente
from database.conection import Session
from schemas.schema_seguimiento_paciente import *
from sqlalchemy import select, update

class SeguimientoPacienteController:
    def __init__(self, session_factory: Session = Session()):
        self.session_factory = session_factory

    async def get_all_seguimientos(self):
        async with self.session_factory as session:
            result = await session.execute(select(SeguimientoPaciente))
            return result.scalars().all()

    async def get_seguimiento_by_id(self, seguimiento_id: int):
        async with self.session_factory as session:
            result = await session.execute(select(SeguimientoPaciente).where(SeguimientoPaciente.id == seguimiento_id))
            return result.scalar_one_or_none()

    async def create_seguimiento(self, seguimiento: SeguimientoPacienteCreate):
        async with self.session_factory as session:
            new_seguimiento = SeguimientoPaciente(
                fecha=seguimiento.fecha,
                descripcion=seguimiento.descripcion,
                plan_tratamiento_id=seguimiento.plan_tratamiento_id,
                usuario_id=seguimiento.usuario_id,
                pieza_id=seguimiento.pieza_id
            )
            session.add(new_seguimiento)
            await session.commit()
            return new_seguimiento
    
    async def update_seguimiento(self, seguimiento_id: int, seguimiento: SeguimientoPacienteUpdate):
        async with self.session_factory as session:
            
            update_data = seguimiento.model_dump(exclude_unset=True)
            if not update_data:
                return None

            seguimiento_to_update = await session.execute(update(SeguimientoPaciente).where(SeguimientoPaciente.id == seguimiento_id).values(
                **update_data
            ).returning(SeguimientoPaciente)
            )
            await session.commit()
            updated = seguimiento_to_update.scalar_one_or_none()
            return updated

    async def delete_seguimiento(self, seguimiento_id: int):
        async with self.session_factory as session:
            seguimiento_to_delete = await session.execute(select(SeguimientoPaciente).where(SeguimientoPaciente.id == seguimiento_id))
            seguimiento_to_delete = seguimiento_to_delete.scalar_one_or_none()
            if seguimiento_to_delete is None:
                return None
            await session.delete(seguimiento_to_delete)
            await session.commit()
            return seguimiento_to_delete
