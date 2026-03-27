from fastapi import APIRouter, Depends
from schermas.motoboy import MotoboyCreate,MotoboyResponse , MotoboyList
from database.db import get_db
from sqlalchemy.orm import Session
from service.motoboy_service import registra_motoboy

router = APIRouter(prefix='/motoboy')


@router.post('/')
async def motoboy_create(motoboy:MotoboyCreate,db: Session = Depends(get_db)):
    return registra_motoboy(db,motoboy)


@router.get('/{id}')
async def motoboy_reponse(id:int,db: Session = Depends(get_db)):
    return

@router.get('/')
async def motoboy_list(db: Session = Depends(get_db)):
    pass