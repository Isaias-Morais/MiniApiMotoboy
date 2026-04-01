from sqlalchemy.orm import Session
from repository.base_repository import salvar_objeto
from models.pedido import Pedidos
from models.enum import StatusPedidos
from repository.pedidos_repository import *
from fastapi import HTTPException
from schemas.pedidos import *


def registra_pedidos(db:Session,pedidos:PedidoCreate):

    try:
        novo = Pedidos(**pedidos.dict())
        salvar_objeto(db,novo)
        return 'objeto salvo'
    except Exception as e:
        return f'erro interno {e}'

def lista_pedidos(db:Session):

    try:
        lista = listar_pedidos_repository(db)
        return lista
    except Exception as e:
        return f'erro interno {e}'

def response_pedido(db:Session,id:int):

    pedido = busca_pedido_repository(db,id)

    if not pedido:
        raise HTTPException(
            status_code=404,
            detail='Pedido não encontrado'
        )

    return pedido


def alterar_status_pedido(db:Session,id:int,status:StatusPedidos):

    pedido = alterar_pedidos_status_repository(db,id,status)

    if not pedido:
        raise HTTPException(
            status_code=404,
            detail='pedido não encontrado'
        )

    return pedido


def deletar_pedido(db:Session,id:int):
    pedido = deletar_pedido_repository(db,id)

    if not pedido:
        raise HTTPException(
            status_code=404,
            detail='pedido não encontrado'
        )

    return pedido