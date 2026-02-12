from models.model_rol import Rol
from database.conection import Session
from schemas.schema_rol import *
from sqlalchemy import select, update

class RolController:
    def __init__(self, session_factory: Session = Session()):
        self.session_factory = session_factory

    async def get_all_rols(self):
        async with self.session_factory as session:
            result = await session.execute(select(Rol))
            return result.scalars().all()

    async def get_rol_by_id(self, rol_id: int):
        async with self.session_factory as session:
            result = await session.execute(select(Rol).where(Rol.id == rol_id))
            return result.scalar_one_or_none()

    async def create_rol(self, rol: RolCreate):
        async with self.session_factory as session:
            new_rol = Rol(
                nombre_rol=rol.nombre_rol
            )
            session.add(new_rol)
            await session.commit()
            return new_rol
    
    async def update_rol(self, rol_id: int, rol: RolUpdate):
        async with self.session_factory as session:
            rol_to_update = await session.execute(update(Rol).where(Rol.id == rol_id).values(
                nombre_rol=rol.nombre_rol
            ).returning(Rol)
            )
            await session.commit()
            updated = rol_to_update.scalar_one_or_none()
            return updated

    async def delete_rol(self, rol_id: int):
        async with self.session_factory as session:
            rol_to_delete = await session.execute(select(Rol).where(Rol.id == rol_id))
            rol_to_delete = rol_to_delete.scalar_one_or_none()
            if rol_to_delete is None:
                return None
            await session.delete(rol_to_delete)
            await session.commit()
            return rol_to_delete
