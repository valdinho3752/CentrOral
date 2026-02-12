from models.model_permiso import Permiso
from database.conection import Session
from schemas.schema_permiso import *
from sqlalchemy import select, update

class PermisoController:
    def __init__(self, session_factory: Session = Session()):
        self.session_factory = session_factory

    async def get_all_permisos(self):
        async with self.session_factory as session:
            result = await session.execute(select(Permiso))
            return result.scalars().all()

    async def get_permiso_by_id(self, permiso_id: int):
        async with self.session_factory as session:
            result = await session.execute(select(Permiso).where(Permiso.id == permiso_id))
            return result.scalar_one_or_none()

    async def create_permiso(self, permiso: PermisoCreate):
        async with self.session_factory as session:
            new_permiso = Permiso(
                nombre_permiso=permiso.nombre_permiso
            )
            session.add(new_permiso)
            await session.commit()
            return new_permiso
    
    async def update_permiso(self, permiso_id: int, permiso: PermisoUpdate):
        async with self.session_factory as session:
            permiso_to_update = await session.execute(update(Permiso).where(Permiso.id == permiso_id).values(
                nombre_permiso=permiso.nombre_permiso
            ).returning(Permiso)
            )
            await session.commit()
            updated = permiso_to_update.scalar_one_or_none()
            return updated

    async def delete_permiso(self, permiso_id: int):
        async with self.session_factory as session:
            permiso_to_delete = await session.execute(select(Permiso).where(Permiso.id == permiso_id))
            permiso_to_delete = permiso_to_delete.scalar_one_or_none()
            if permiso_to_delete is None:
                return None
            await session.delete(permiso_to_delete)
            await session.commit()
            return permiso_to_delete
