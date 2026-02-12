from models.model_tratamiento import Tratamiento
from database.conection import Session
from schemas.schema_tratamiento import *
from sqlalchemy import select, update

class TratamientoController:
    def __init__(self, session_factory: Session = Session()):
        self.session_factory = session_factory

    async def get_all_tratamientos(self):
        async with self.session_factory as session:
            result = await session.execute(select(Tratamiento))
            return result.scalars().all()

    async def get_tratamiento_by_id(self, tratamiento_id: int):
        async with self.session_factory as session:
            result = await session.execute(select(Tratamiento).where(Tratamiento.id == tratamiento_id))
            return result.scalar_one_or_none()

    async def create_tratamiento(self, tratamiento: TratamientoCreate):
        async with self.session_factory as session:
            new_tratamiento = Tratamiento(
                nombre_tratamiento=tratamiento.nombre_tratamiento,
                precio_economico=tratamiento.precio_economico,
                precio_medio=tratamiento.precio_medio,
                precio_alto=tratamiento.precio_alto
            )
            session.add(new_tratamiento)
            await session.commit()
            return new_tratamiento
    
    async def update_tratamiento(self, tratamiento_id: int, tratamiento: TratamientoUpdate):
        async with self.session_factory as session:
            update_data = tratamiento.model_dump(exclude_unset=True)
            if not update_data:
                return None
                
            tratamiento_to_update = await session.execute(update(Tratamiento).where(Tratamiento.id == tratamiento_id).values(
                **update_data
            ).returning(Tratamiento)
            )
            await session.commit()
            updated = tratamiento_to_update.scalar_one_or_none()
            return updated

    async def delete_tratamiento(self, tratamiento_id: int):
        async with self.session_factory as session:
            tratamiento_to_delete = await session.execute(select(Tratamiento).where(Tratamiento.id == tratamiento_id))
            tratamiento_to_delete = tratamiento_to_delete.scalar_one_or_none()
            if tratamiento_to_delete is None:
                return None
            await session.delete(tratamiento_to_delete)
            await session.commit()
            return tratamiento_to_delete
