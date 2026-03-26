from pydantic import BaseModel
from datetime import datetime


class MotoboyBase(BaseModel):
    nome : str
    veiculo : str
    telefone : str


class MotoboyResponse(MotoboyBase):
    id : int
    status : bool
    data_de_cricao : datetime


class MotoboyCreate(MotoboyBase):
    pass