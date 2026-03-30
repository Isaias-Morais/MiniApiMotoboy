from pydantic import BaseModel
from datetime import datetime


class MotoboyBase(BaseModel):
    nome : str
    veiculo : str
    telefone : str


class MotoboyResponse(MotoboyBase):
    id : int
    status_ativo : bool
    data_de_criacao : datetime
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

