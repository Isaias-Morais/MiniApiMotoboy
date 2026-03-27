from sqlalchemy.orm import Session
from schermas.motoboy import MotoboyCreate
from repository.base_repository import salvar_objeto
from models.motoboy import Motoboy

def registra_motoboy(db:Session,motoboy:MotoboyCreate):

    try:
        novo = Motoboy(**motoboy.dict())
        salvar_objeto(db,novo)
        return 'objeto salvo'
    except Exception as e:
        return f'erro interno {e}'
