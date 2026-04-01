from typing import Optional
from pydantic import BaseModel
from decimal import Decimal
from datetime import datetime
from models.enum import StatusPedidos


class PedidoBase(BaseModel):
    descricao:str
    observacao: Optional[str]
    endereco: str
    valor:Decimal


class PedidoResponse(PedidoBase):
    id:int
    status:StatusPedidos
    data_de_criacao: datetime
    class Config:
        from_attributes = True


class PedidoCreate(PedidoBase):
    pass

class PedidoList(BaseModel):
    id:int
    descricao:str
    data_de_criacao:datetime

class PedidoDelete(BaseModel):
    id : int
    data_de_criacao : datetime


class PedidoStatus(BaseModel):
    id : int
    descricao : str
    status : str
