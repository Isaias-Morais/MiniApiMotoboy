from sqlalchemy import nulls_first

from models.motoboy import Motoboy
from sqlalchemy.orm import Session
from datetime import datetime


def lista_motoboys_repository(session:Session):
    return session.query(Motoboy).all()


def alterar_motoboy_status_ativo_repository(session:Session,id:int):
    motoboy = busca_motoboy_repository(session,id)

    if not motoboy:
        return None

    motoboy.status_ativo = not motoboy.status_ativo
    session.flush()
    session.commit()
    session.refresh(motoboy)
    return motoboy


def alterar_motoboy_status_livre_repository(session:Session,motoboy:Motoboy):
    motoboy = motoboy

    if not motoboy:
        return None

    motoboy.status_livre = not motoboy.status_livre
    session.flush()
    session.commit()
    session.refresh(motoboy)
    return motoboy


def busca_motoboy_repository(session:Session,id:int):
    motoboy = session.query(Motoboy).filter(Motoboy.id == id).first()

    if not motoboy:
        return None

    return  motoboy



def deletar_motoboy_repository(session:Session,id:int):
    motoboy = busca_motoboy_repository(session,id)

    if not motoboy:
        return None

    session.delete(motoboy)
    session.commit()
    return motoboy

def atualiza_ultimo_pedido_motoboy_repository(session:Session,motoboy_id:int):

    motoboy : Motoboy = busca_motoboy_repository(session,motoboy_id)

    if not motoboy:
        return None

    motoboy.ultimo_pedido = datetime.utcnow()
    session.flush()
    session.commit()
    session.refresh(motoboy)
    return motoboy


def procurar_motoboy_disponivel_repository(session:Session):
    motoboy = session.query(
        Motoboy
    ).filter(
        Motoboy.status_ativo == True,
        Motoboy.status_livre == True
    ).order_by(
        nulls_first(Motoboy.ultimo_pedido.asc())
    ).first()

    if not motoboy:
        return None

    return motoboy



