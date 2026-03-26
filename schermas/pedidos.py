from typing import Optional
from pydantic import BaseModel
from decimal import Decimal
from datetime import datetime

class PedidoBase(BaseModel):
    descricao:str
    observacao: Optional[str]
    valor:Decimal


class PedidoResponse(PedidoBase):
    id: int
    status:str
    data_de_criacao: datetime
    class Config:
        from_attributes = True


class PedidoCreate(PedidoBase):
    pass