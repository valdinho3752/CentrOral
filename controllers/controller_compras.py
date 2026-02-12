from models.model_compras import Compras
from database.conection import Session
from schemas.schema_compras import *
from sqlalchemy import select, update

class ComprasController:
    def __init__(self, session_factory: Session = Session()):
        self.session_factory = session_factory

    async def get_all_compras(self):
        async with self.session_factory as session:
            result = await session.execute(select(Compras))
            return result.scalars().all()

    async def get_compra_by_id(self, compra_id: int):
        async with self.session_factory as session:
            result = await session.execute(select(Compras).where(Compras.id == compra_id))
            return result.scalar_one_or_none()

    async def create_compra(self, compra: ComprasCreate):
        async with self.session_factory as session:
            new_compra = Compras(
                fecha=compra.fecha,
                precio_compra=compra.precio_compra,
                cantidad=compra.cantidad,
                usuario_id=compra.usuario_id,
                inventario_id=compra.inventario_id,
                transaccion_id=compra.transaccion_id
            )
            session.add(new_compra)
            await session.commit()
            return new_compra
    
    async def update_compra(self, compra_id: int, compra: ComprasUpdate):
        async with self.session_factory as session:
            
            update_data = compra.model_dump(exclude_unset=True)
            if not update_data:
                return None
                
            compra_to_update = await session.execute(update(Compras).where(Compras.id == compra_id).values(
                **update_data
            ).returning(Compras)
            )
            await session.commit()
            updated = compra_to_update.scalar_one_or_none()
            return updated

    async def delete_compra(self, compra_id: int):
        async with self.session_factory as session:
            compra_to_delete = await session.execute(select(Compras).where(Compras.id == compra_id))
            compra_to_delete = compra_to_delete.scalar_one_or_none()
            if compra_to_delete is None:
                return None
            await session.delete(compra_to_delete)
            await session.commit()
            return compra_to_delete
