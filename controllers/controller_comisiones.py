from models.model_comisiones import Comisiones
from database.conection import Session
from schemas.schema_comisiones import *
from sqlalchemy import select, update

class ComisionesController:
    def __init__(self, session_factory: Session = Session()):
        self.session_factory = session_factory

    async def get_all_comisiones(self):
        async with self.session_factory as session:
            result = await session.execute(select(Comisiones))
            return result.scalars().all()

    async def get_comision_by_id(self, comision_id: int):
        async with self.session_factory as session:
            result = await session.execute(select(Comisiones).where(Comisiones.id == comision_id))
            return result.scalar_one_or_none()

    async def create_comision(self, comision: ComisionesCreate):
        async with self.session_factory as session:
            new_comision = Comisiones(
                comision_total=comision.comision_total,
                usuario_id=comision.usuario_id,
                cierre_caja_id=comision.cierre_caja_id
            )
            session.add(new_comision)
            await session.commit()
            return new_comision
    
    async def update_comision(self, comision_id: int, comision: ComisionesUpdate):
        async with self.session_factory as session:
            
            update_data = comision.model_dump(exclude_unset=True)
            if not update_data:
                return None
                
            comision_to_update = await session.execute(update(Comisiones).where(Comisiones.id == comision_id).values(
                **update_data
            ).returning(Comisiones)
            )
            await session.commit()
            updated = comision_to_update.scalar_one_or_none()
            return updated

    async def delete_comision(self, comision_id: int):
        async with self.session_factory as session:
            comision_to_delete = await session.execute(select(Comisiones).where(Comisiones.id == comision_id))
            comision_to_delete = comision_to_delete.scalar_one_or_none()
            if comision_to_delete is None:
                return None
            await session.delete(comision_to_delete)
            await session.commit()
            return comision_to_delete
