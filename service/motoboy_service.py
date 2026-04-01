from sqlalchemy.orm import Session
from schemas.motoboy import MotoboyCreate
from repository.base_repository import salvar_objeto
from repository.motoboy_repository import *
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
        lista = lista_motoboys_repository(db)
        return lista
    except Exception as e:
        return f'erro interno {e}'


def response_motoboy(db:Session,id:int):

    motoboy = busca_motoboy_repository(db,id)

    if not motoboy:
        raise HTTPException(
            status_code=404,
            detail='Motoboy não encontrado'
        )

    return motoboy


def alterar_status_ativo_motoboy(db:Session,id:int):

    motoboy = alterar_motoboy_status_ativo_repository(db,id)

    if not motoboy:
        raise HTTPException(
            status_code=404,
            detail='Motoboy não encontrado'
        )

    return motoboy


def alterar_status_livre_motoboy(db:Session,id:int):

    motoboy = alterar_motoboy_status_livre_repository(db,id)

    if not motoboy:
        raise HTTPException(
            status_code=404,
            detail='Motoboy não encontrado'
        )

    return motoboy


def delete_motoboy(db:Session,id:int):
    motoboy = deletar_motoboy_repository(db,id)

    if not motoboy:
        raise HTTPException(
            status_code=404,
            detail='Motoboy não encontrado'
        )

    return motoboy
