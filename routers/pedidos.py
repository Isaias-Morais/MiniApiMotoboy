from fastapi import APIRouter,Depends
from schemas.pedidos import *
from database.db import get_db
from sqlalchemy.orm import Session
from service.pedidos_service import *
from models.enum import StatusPedidos

router = APIRouter(prefix='/pedidos')


@router.post('/')
async def create_pedido(pedidos:PedidoCreate,db: Session = Depends(get_db)):
    return registra_pedidos(db,pedidos)


@router.get('/{id}',response_model=PedidoResponse)
async def response_pedido(id:int,db: Session = Depends(get_db)):
    return resposta_pedido(db,id)


@router.get('/',response_model=list[PedidoList])
async def list_pedido(db: Session = Depends(get_db)):
    return lista_pedidos(db)


@router.delete('/{id}',response_model=PedidoDelete)
async def delete_pedido(id:int,db:Session = Depends(get_db)):
    return deletar_pedido(db,id)


@router.patch('/{id}/aceita_pedido',response_model=PedidoStatus)
async def accepted_pedido(id:int,db:Session = Depends(get_db)):
    return aceitar_pedido(db,id)

@router.patch('/{id}/cancela_pedido',response_model=PedidoStatus)
async def cancel_pedido(id:int,db:Session = Depends(get_db)):
    return cancelar_pedido(db,id)

@router.patch('/{id}/pronto_pedido',response_model=PedidoStatus)
async def ready_pedido(id:int,db:Session = Depends(get_db)):
    return pedido_pronto(db,id)