from models.model_pieza import Pieza
from database.conection import Session
from schemas.schema_pieza import *
from sqlalchemy import select, update

class PiezaController:
    def __init__(self, session_factory: Session = Session()):
        self.session_factory = session_factory

    async def get_all_piezas(self):
        async with self.session_factory as session:
            result = await session.execute(select(Pieza))
            return result.scalars().all()

    async def get_pieza_by_id(self, pieza_id: int):
        async with self.session_factory as session:
            result = await session.execute(select(Pieza).where(Pieza.id == pieza_id))
            return result.scalar_one_or_none()

    async def create_pieza(self, pieza: PiezaCreate):
        async with self.session_factory as session:
            new_pieza = Pieza(
                n_pieza=pieza.n_pieza
            )
            session.add(new_pieza)
            await session.commit()
            return new_pieza
    
    async def update_pieza(self, pieza_id: int, pieza: PiezaUpdate):
        async with self.session_factory as session:
            update_data = pieza.model_dump(exclude_unset=True)
            if not update_data:
                return None
                
            pieza_to_update = await session.execute(update(Pieza).where(Pieza.id == pieza_id).values(
                **update_data
            ).returning(Pieza)
            )
            await session.commit()
            updated = pieza_to_update.scalar_one_or_none()
            return updated

    async def delete_pieza(self, pieza_id: int):
        async with self.session_factory as session:
            pieza_to_delete = await session.execute(select(Pieza).where(Pieza.id == pieza_id))
            pieza_to_delete = pieza_to_delete.scalar_one_or_none()
            if pieza_to_delete is None:
                return None
            await session.delete(pieza_to_delete)
            await session.commit()
            return pieza_to_delete
