from models.model_inventario import Inventario
from database.conection import Session
from schemas.schema_inventario import *
from sqlalchemy import select, update

class InventarioController:
    def __init__(self, session_factory: Session = Session()):
        self.session_factory = session_factory

    async def get_all_inventarios(self):
        async with self.session_factory as session:
            result = await session.execute(select(Inventario))
            return result.scalars().all()

    async def get_inventario_by_id(self, inventario_id: int):
        async with self.session_factory as session:
            result = await session.execute(select(Inventario).where(Inventario.id == inventario_id))
            return result.scalar_one_or_none()

    async def create_inventario(self, inventario: InventarioCreate):
        async with self.session_factory as session:
            new_inventario = Inventario(
                nombre_insumo=inventario.nombre_insumo,
                cantidad=inventario.cantidad,
                descripcion=inventario.descripcion,
                marca=inventario.marca
            )
            session.add(new_inventario)
            await session.commit()
            return new_inventario
    
    async def update_inventario(self, inventario_id: int, inventario: InventarioUpdate):
        async with self.session_factory as session:
            
            update_data = inventario.model_dump(exclude_unset=True)
            if not update_data:
                return None
                
            inventario_to_update = await session.execute(update(Inventario).where(Inventario.id == inventario_id).values(
                **update_data
            ).returning(Inventario)
            )
            await session.commit()
            updated = inventario_to_update.scalar_one_or_none()
            return updated

    async def delete_inventario(self, inventario_id: int):
        async with self.session_factory as session:
            inventario_to_delete = await session.execute(select(Inventario).where(Inventario.id == inventario_id))
            inventario_to_delete = inventario_to_delete.scalar_one_or_none()
            if inventario_to_delete is None:
                return None
            await session.delete(inventario_to_delete)
            await session.commit()
            return inventario_to_delete
