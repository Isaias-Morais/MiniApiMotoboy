from typing import Optional
from pydantic import BaseModel
from datetime import datetime


class MotoboyBase(BaseModel):
    nome : str
    veiculo : str
    telefone : str


class MotoboyResponse(MotoboyBase):
    id : int
    status_ativo : bool
    status_livre :bool
    data_de_criacao : datetime
    ultimo_pedido : Optional[datetime] = None
    class Config:
        from_attributes = True

class MotoboyCreate(MotoboyBase):
    pass


class MotoboyList(BaseModel):
    id : int
    nome : str
    data_de_criacao : datetime


class MotoboyDelete(MotoboyBase):
    id : int
    data_de_criacao : datetime


class MotoboyStatus(BaseModel):
    id : int
    nome : str
    status_ativo : bool
    status_livre : bool



