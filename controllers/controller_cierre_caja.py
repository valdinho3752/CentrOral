from models.model_cierre_caja import CierreCaja
from database.conection import Session
from schemas.schema_cierre_caja import *
from sqlalchemy import select, update

class CierreCajaController:
    def __init__(self, session_factory: Session = Session()):
        self.session_factory = session_factory

    async def get_all_cierres(self):
        async with self.session_factory as session:
            result = await session.execute(select(CierreCaja))
            return result.scalars().all()

    async def get_cierre_by_id(self, cierre_id: int):
        async with self.session_factory as session:
            result = await session.execute(select(CierreCaja).where(CierreCaja.id == cierre_id))
            return result.scalar_one_or_none()

    async def create_cierre(self, cierre: CierreCajaCreate):
        async with self.session_factory as session:
            new_cierre = CierreCaja(
                fecha_inicio=cierre.fecha_inicio,
                fecha_cierre=cierre.fecha_cierre,
                total_ingresos=cierre.total_ingresos,
                total_egresos=cierre.total_egresos,
                total_diario=cierre.total_diario,
                total_acumulado=cierre.total_acumulado,
                usuario_id=cierre.usuario_id
            )
            session.add(new_cierre)
            await session.commit()
            return new_cierre
    
    async def update_cierre(self, cierre_id: int, cierre: CierreCajaUpdate):
        async with self.session_factory as session:
            
            update_data = cierre.model_dump(exclude_unset=True)
            if not update_data:
                return None
            
            cierre_to_update = await session.execute(update(CierreCaja).where(CierreCaja.id == cierre_id).values(
                **update_data
            ).returning(CierreCaja)
            )
            await session.commit()
            updated = cierre_to_update.scalar_one_or_none()
            return updated

    async def delete_cierre(self, cierre_id: int):
        async with self.session_factory as session:
            cierre_to_delete = await session.execute(select(CierreCaja).where(CierreCaja.id == cierre_id))
            cierre_to_delete = cierre_to_delete.scalar_one_or_none()
            if cierre_to_delete is None:
                return None
            await session.delete(cierre_to_delete)
            await session.commit()
            return cierre_to_delete
