from models.model_rol_permiso import RolPermiso
from database.conection import Session
from schemas.schema_rol_permiso import *
from sqlalchemy import select, update

class RolPermisoController:
    def __init__(self, session_factory: Session = Session()):
        self.session_factory = session_factory

    async def get_all_rol_permisos(self):
        async with self.session_factory as session:
            result = await session.execute(select(RolPermiso))
            return result.scalars().all()

    async def get_rol_permiso_by_id(self, rol_permiso_id: int):
        async with self.session_factory as session:
            result = await session.execute(select(RolPermiso).where(RolPermiso.id == rol_permiso_id))
            return result.scalar_one_or_none()

    async def create_rol_permiso(self, rol_permiso: RolPermisoCreate):
        async with self.session_factory as session:
            new_rol_permiso = RolPermiso(
                rol_id=rol_permiso.rol_id,
                permiso_id=rol_permiso.permiso_id
            )
            session.add(new_rol_permiso)
            await session.commit()
            return new_rol_permiso
    
    async def update_rol_permiso(self, rol_permiso_id: int, rol_permiso: RolPermisoUpdate):
        async with self.session_factory as session:
            rol_permiso_to_update = await session.execute(update(RolPermiso).where(RolPermiso.id == rol_permiso_id).values(
                rol_id=rol_permiso.rol_id,
                permiso_id=rol_permiso.permiso_id
            ).returning(RolPermiso)
            )
            await session.commit()
            updated = rol_permiso_to_update.scalar_one_or_none()
            return updated

    async def delete_rol_permiso(self, rol_permiso_id: int):
        async with self.session_factory as session:
            rol_permiso_to_delete = await session.execute(select(RolPermiso).where(RolPermiso.id == rol_permiso_id))
            rol_permiso_to_delete = rol_permiso_to_delete.scalar_one_or_none()
            if rol_permiso_to_delete is None:
                return None
            await session.delete(rol_permiso_to_delete)
            await session.commit()
            return rol_permiso_to_delete
