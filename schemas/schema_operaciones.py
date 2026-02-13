from pydantic import BaseModel
import datetime

class compra_insumo(BaseModel):
    ID_inventario : int
    ID_usuario : int
    cantidad : int
    precio_compra : float
    ID_cierre_caja : int
    
    class Config:
        from_attributes = True

