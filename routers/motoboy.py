from fastapi import APIRouter, Depends
from schemas.motoboy import *
from database.db import get_db
from sqlalchemy.orm import Session
from service.motoboy_service import *
from service.pedidos_service import *
router = APIRouter(prefix='/motoboy')


@router.post('/')
async def create_motoboy(motoboy:MotoboyCreate,db: Session = Depends(get_db)):
    return registra_motoboy(db,motoboy)


@router.get('/{id}',response_model=MotoboyResponse)
async def response_motoboy(id:int,db: Session = Depends(get_db)):
    return resposta_motoboy(db,id)

@router.get('/',response_model=list[MotoboyList])
async def list_motoboy(db: Session = Depends(get_db)):
    return lista_motoboy(db)

@router.delete('/{id}',response_model=MotoboyDelete)
async def delete_motoboy(id:int,db : Session = Depends(get_db)):
    return delete_motoboy(db,id)


@router.patch('/{id}/ativo',response_model=MotoboyStatus)
async def status_ativo_motoboy(id:int,db : Session = Depends(get_db)):
    return alterar_status_ativo_motoboy(db,id)


@router.patch('/{id}/livre',response_model=MotoboyStatus)
async def status_livre_motoboy(id:int,db : Session = Depends(get_db)):
    return alterar_status_livre_motoboy(db,id)


@router.patch('/{id}/inicia_rota',response_model=PedidoStatus)
async def iniciar_rota_motoboy(id:int,db:Session = Depends(get_db)):
    return iniciar_rota(db,id)


@router.patch('/{id}/finalizar_rota',response_model=PedidoStatus)
async def finalizar_rota_motoboy(id:int,db:Session = Depends(get_db)):
    return pedido_entregue(db,id)


@router.patch('/{id}/falha',response_model=PedidoStatus)
async def falha_na_rota_motoboy(id:int,db:Session = Depends(get_db)):
    return pedido_falhou(db,id)

