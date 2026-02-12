from models.model_transaccion import Transaccion
from database.conection import Session
from schemas.schema_transaccion import *
from sqlalchemy import select, update

class TransaccionController:
    def __init__(self, session_factory: Session = Session()):
        self.session_factory = session_factory

    async def get_all_transacciones(self):
        async with self.session_factory as session:
            result = await session.execute(select(Transaccion))
            return result.scalars().all()

    async def get_transaccion_by_id(self, transaccion_id: int):
        async with self.session_factory as session:
            result = await session.execute(select(Transaccion).where(Transaccion.id == transaccion_id))
            return result.scalar_one_or_none()

    async def create_transaccion(self, transaccion: TransaccionCreate):
        async with self.session_factory as session:
            new_transaccion = Transaccion(
                tipo=transaccion.tipo,
                origen_deposito=transaccion.origen_deposito,
                fecha_hora=transaccion.fecha_hora,
                usuario_id=transaccion.usuario_id,
                cierre_caja_id=transaccion.cierre_caja_id
            )
            session.add(new_transaccion)
            await session.commit()
            return new_transaccion
    
    async def update_transaccion(self, transaccion_id: int, transaccion: TransaccionUpdate):
        async with self.session_factory as session:
            
            update_data = transaccion.model_dump(exclude_unset=True)
            if not update_data:
                return None
                
            transaccion_to_update = await session.execute(update(Transaccion).where(Transaccion.id == transaccion_id).values(
                **update_data
            ).returning(Transaccion)
            )
            await session.commit()
            updated = transaccion_to_update.scalar_one_or_none()
            return updated

    async def delete_transaccion(self, transaccion_id: int):
        async with self.session_factory as session:
            transaccion_to_delete = await session.execute(select(Transaccion).where(Transaccion.id == transaccion_id))
            transaccion_to_delete = transaccion_to_delete.scalar_one_or_none()
            if transaccion_to_delete is None:
                return None
            await session.delete(transaccion_to_delete)
            await session.commit()
            return transaccion_to_delete
