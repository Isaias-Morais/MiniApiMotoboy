from models.motoboy import Motoboy
from sqlalchemy.orm import Session
from fastapi import HTTPException


def listar_motoboys(session:Session):
    return session.query(Motoboy).all()


def alterar_motoboy_status(session:Session,id:int):
    motoboy = busca_motoboy(session,id)

    if not motoboy:
        raise HTTPException(
            status_code=404,
            detail='Motoboy não encontrado'
        )

    else:
        motoboy.status_ativo = not motoboy.status_ativo
        session.flush()
        session.commit()
        return motoboy



def busca_motoboy(session:Session,id:int):
    return session.query(Motoboy).filter(Motoboy.id == id).first()