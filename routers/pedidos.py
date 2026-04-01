from fastapi import APIRouter,Depends
from schemas.pedidos import *
from database.db import get_db
from sqlalchemy.orm import Session
from service.pedidos_service import *
from models.enum import StatusPedidos

router = APIRouter(prefix='/pedidos')


@router.post('/')
async def pedido_create(pedidos:PedidoCreate,db: Session = Depends(get_db)):
    return registra_pedidos(db,pedidos)


@router.get('/{id}',response_model=PedidoResponse)
async def pedido_reponse(id:int,db: Session = Depends(get_db)):
    return response_pedido(db,id)


@router.get('/',response_model=list[PedidoList])
async def pedidos_list(db: Session = Depends(get_db)):
    return lista_pedidos(db)


@router.delete('/{id}',response_model=PedidoDelete)
async def delete_pedido(id:int,db:Session = Depends(get_db)):
    return deletar_pedido(db,id)


@router.patch('/{id}/status/{status}',response_model=PedidoStatus)
async def pedido_status(id:int,status:StatusPedidos,db : Session = Depends(get_db)):
    return alterar_status_pedido(db,id,status)