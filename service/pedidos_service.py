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

def resposta_pedido(db:Session,id:int):

    pedido = busca_pedido_repository(db,id)

    if not pedido:
        raise HTTPException(
            status_code=404,
            detail='Pedido não encontrado'
        )

    return pedido


def aceitar_pedido(db:Session,id:int):

    status = StatusPedidos

    pedido : Pedidos = busca_pedido_repository(db,id)

    if not pedido:
        raise HTTPException(
            status_code=404,
            detail='pedido não encontrado'
        )

    if pedido.status != status.PENDENTE:
        raise HTTPException(
            status_code=400,
            detail="Pedido não está pedente"
        )
    novo_status_pedido = alterar_pedidos_status_repository(db,pedido,status.PREPARO)
    return novo_status_pedido


def cancelar_pedido(db:Session,id:int):

    status = StatusPedidos

    pedido : Pedidos = busca_pedido_repository(db,id)

    if not pedido:
        raise HTTPException(
            status_code=404,
            detail='pedido não encontrado'
        )

    if pedido.status != status.PENDENTE:
        raise HTTPException(
            status_code=400,
            detail="Pedido não está pedente"
        )
    novo_status_pedido = alterar_pedidos_status_repository(db,pedido,status.CANCELADO)
    return novo_status_pedido


def pedido_pronto(db:Session,id:int):

    status = StatusPedidos

    pedido : Pedidos = busca_pedido_repository(db,id)

    if not pedido:
        raise HTTPException(
            status_code=404,
            detail='pedido não encontrado'
        )

    if pedido.status != status.PREPARO:
        raise HTTPException(
            status_code=400,
            detail="Pedido não está em preparo"
        )
    novo_status_pedido = alterar_pedidos_status_repository(db,pedido,status.PRONTO)
    return novo_status_pedido


def iniciar_rota(db:Session,id:int):

    status = StatusPedidos

    pedido : Pedidos = busca_pedido_repository(db,id)

    if not pedido:
        raise HTTPException(
            status_code=404,
            detail='pedido não encontrado'
        )

    if pedido.status != status.PRONTO:
        raise HTTPException(
            status_code=400,
            detail="Pedido não está pronto"
        )
    novo_status_pedido = alterar_pedidos_status_repository(db,pedido,status.EM_ROTA)
    return novo_status_pedido


def pedido_entregue(db:Session,id:int):

    status = StatusPedidos

    pedido : Pedidos = busca_pedido_repository(db,id)

    if not pedido:
        raise HTTPException(
            status_code=404,
            detail='pedido não encontrado'
        )

    if pedido.status != status.EM_ROTA:
        raise HTTPException(
            status_code=400,
            detail="Pedido não está em rota"
        )
    novo_status_pedido = alterar_pedidos_status_repository(db,pedido,status.ENTREGUE)
    return novo_status_pedido


def pedido_falhou(db:Session,id:int):

    status = StatusPedidos

    pedido : Pedidos = busca_pedido_repository(db,id)

    if not pedido:
        raise HTTPException(
            status_code=404,
            detail='pedido não encontrado'
        )

    if pedido.status != status.EM_ROTA:
        raise HTTPException(
            status_code=400,
            detail="Pedido não está em rota"
        )
    novo_status_pedido = alterar_pedidos_status_repository(db,pedido,status.FALHA_NA_ENTREGA)
    return novo_status_pedido


def deletar_pedido(db:Session,id:int):
    pedido = deletar_pedido_repository(db,id)

    if not pedido:
        raise HTTPException(
            status_code=404,
            detail='pedido não encontrado'
        )

    return pedido