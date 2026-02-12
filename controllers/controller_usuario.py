from models.model_usuario import Usuario
from database.conection import Session
from schemas.schema_usuario import *
from sqlalchemy import select, update

class UserController:
    def __init__(self,   session_factory: Session = Session()):
        self.session_factory = session_factory

    async def get_all_users(self):
        async with self.session_factory as session:
            result = await session.execute(select(Usuario))
            return result.scalars().all()

    async def get_user_by_id(self, user_id: int):
        async with self.session_factory as session:
            result = await session.execute(select(Usuario).where(Usuario.id == user_id))
            return result.scalar_one_or_none()

    async def create_user(self, user: UsuarioCreate):
        async with self.session_factory as session:
            new_user = Usuario(
                codigo=user.codigo,
                nombre=user.nombre,
                apellido=user.apellido,
                rol_id=user.rol_id,
                ultima_edicion=user.ultima_edicion,
                porcentaje=user.porcentaje
            )
            session.add(new_user)
            await session.commit()
            return new_user
    
    async def update_user(self, user_id: int, user: UsuarioUpdate):
        async with self.session_factory as session:
            user_to_update = await session.execute(update(Usuario).where(Usuario.id == user_id).values(
                codigo=user.codigo,
                nombre=user.nombre,
                apellido=user.apellido,
                rol_id=user.rol_id,
                ultima_edicion=user.ultima_edicion,
                porcentaje=user.porcentaje
            ).returning(Usuario)
            )
            await session.commit()
            updated = user_to_update.scalar_one_or_none()
            return updated

    async def delete_user(self, user_id: int):
        async with self.session_factory as session:
            user_to_delete = await session.execute(select(Usuario).where(Usuario.id == user_id))
            user_to_delete = user_to_delete.scalar_one_or_none()
            if user_to_delete is None:
                return None
            await session.delete(user_to_delete)
            await session.commit()
            return user_to_delete