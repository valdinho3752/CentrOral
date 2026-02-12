from models.model_diagnostico import Diagnostico
from database.conection import Session
from schemas.schema_diagnostico import *
from sqlalchemy import select, update

class DiagnosticoController:
    def __init__(self, session_factory: Session = Session()):
        self.session_factory = session_factory

    async def get_all_diagnosticos(self):
        async with self.session_factory as session:
            result = await session.execute(select(Diagnostico))
            return result.scalars().all()

    async def get_diagnostico_by_id(self, diagnostico_id: int):
        async with self.session_factory as session:
            result = await session.execute(select(Diagnostico).where(Diagnostico.id == diagnostico_id))
            return result.scalar_one_or_none()

    async def create_diagnostico(self, diagnostico: DiagnosticoCreate):
        async with self.session_factory as session:
            new_diagnostico = Diagnostico(
                cara_dental=diagnostico.cara_dental,
                precio_elegido=diagnostico.precio_elegido,
                estado=diagnostico.estado,
                fecha_conclusion=diagnostico.fecha_conclusion,
                precio_aplicado=diagnostico.precio_aplicado,
                plan_tratamiento_id=diagnostico.plan_tratamiento_id,
                tratamiento_id=diagnostico.tratamiento_id,
                pieza_id=diagnostico.pieza_id,
                doctor_id=diagnostico.doctor_id,
                usuario_id=diagnostico.usuario_id
            )
            session.add(new_diagnostico)
            await session.commit()
            return new_diagnostico
    
    async def update_diagnostico(self, diagnostico_id: int, diagnostico: DiagnosticoUpdate):
        async with self.session_factory as session:
            
            update_data = diagnostico.model_dump(exclude_unset=True)
            if not update_data:
                return None
                
            diagnostico_to_update = await session.execute(update(Diagnostico).where(Diagnostico.id == diagnostico_id).values(
                **update_data
            ).returning(Diagnostico)
            )
            await session.commit()
            updated = diagnostico_to_update.scalar_one_or_none()
            return updated

    async def delete_diagnostico(self, diagnostico_id: int):
        async with self.session_factory as session:
            diagnostico_to_delete = await session.execute(select(Diagnostico).where(Diagnostico.id == diagnostico_id))
            diagnostico_to_delete = diagnostico_to_delete.scalar_one_or_none()
            if diagnostico_to_delete is None:
                return None
            await session.delete(diagnostico_to_delete)
            await session.commit()
            return diagnostico_to_delete
