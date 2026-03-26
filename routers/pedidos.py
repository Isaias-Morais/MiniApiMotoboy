from fastapi import APIRouter,Depends
from schermas.pedidos import PedidoCreate,PedidoResponse
from database.database import get_db

router = APIRouter(prefix='/pedidos')

@router.post('/')
async def criar_pedidos(pedidos:PedidoCreate):
    return pedidos


@router.get('/{id}')
async def pedido_reponse(id:int,db = Depends(get_db)):
    pass


