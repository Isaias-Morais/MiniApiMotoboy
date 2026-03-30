from fastapi import APIRouter,Depends
from schemas.pedidos import PedidoCreate,PedidoResponse,PedidoList
from database.db import get_db
from sqlalchemy.orm import Session


router = APIRouter(prefix='/pedidos')


@router.post('/')
async def criar_pedidos(pedidos:PedidoCreate,db: Session = Depends(get_db)):
    return pedidos


@router.get('/{id}')
async def pedido_reponse(id:int,db: Session = Depends(get_db)):
    pass

@router.get('/')
async def pedidos_list(db: Session = Depends(get_db)):
    pass


