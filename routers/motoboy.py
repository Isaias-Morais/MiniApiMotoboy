from fastapi import APIRouter, Depends
from schemas.motoboy import MotoboyCreate, MotoboyResponse, MotoboyList, MotoboyDelete, MotoboyStatus
from database.db import get_db
from sqlalchemy.orm import Session
from service.motoboy_service import registra_motoboy, lista_motoboy, response_motoboy, motoboy_altera_status

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
    pass


@router.patch('/{id}',response_model=MotoboyStatus)
async def motoboy_status(id:int,db : Session = Depends(get_db)):
    return motoboy_altera_status(db,id)