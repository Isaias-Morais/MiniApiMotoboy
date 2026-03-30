from sqlalchemy.orm import Session
from schemas.motoboy import MotoboyCreate
from repository.base_repository import salvar_objeto
from repository.motoboy_repository import listar_motoboys, busca_motoboy, alterar_motoboy_status
from models.motoboy import Motoboy
from fastapi import HTTPException


def registra_motoboy(db:Session,motoboy:MotoboyCreate):

    try:
        novo = Motoboy(**motoboy.dict())
        salvar_objeto(db,novo)
        return 'objeto salvo'
    except Exception as e:
        return f'erro interno {e}'


def lista_motoboy(db:Session):

    try:
        lista = listar_motoboys(db)
        return lista
    except Exception as e:
        return f'erro interno {e}'


def response_motoboy(db:Session,id:int):

    motoboy = busca_motoboy(db,id)

    if not motoboy:
        raise HTTPException(
            status_code=404,
            detail='Motoboy não encontrado'
        )

    return motoboy


def motoboy_altera_status(db:Session,id:int):
    try:
        return alterar_motoboy_status(db,id)
    except Exception as e:
        return f'erro interno {e}'
