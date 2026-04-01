from fastapi import APIRouter, Depends
from schemas.motoboy import *
from database.db import get_db
from sqlalchemy.orm import Session
from service.motoboy_service import *
router = APIRouter(prefix='/motoboy')


@router.post('/')
async def motoboy_create(motoboy:MotoboyCreate,db: Session = Depends(get_db)):
    return registra_motoboy(db,motoboy)


@router.get('/{id}',response_model=MotoboyResponse)
async def motoboy_reponse(id:int,db: Session = Depends(get_db)):
    return response_motoboy(db,id)

@router.get('/',response_model=list[MotoboyList])
async def motoboy_list(db: Session = Depends(get_db)):
    return lista_motoboy(db)

@router.delete('/{id}',response_model=MotoboyDelete)
async def motoboy_delete(id:int,db : Session = Depends(get_db)):
    return delete_motoboy(db,id)


@router.patch('/{id}/ativo',response_model=MotoboyStatus)
async def motoboy_status_ativo(id:int,db : Session = Depends(get_db)):
    return alterar_status_ativo_motoboy(db,id)


@router.patch('/{id}/livre',response_model=MotoboyStatus)
async def motoboy_status_livre(id:int,db : Session = Depends(get_db)):
    return alterar_status_livre_motoboy(db,id)