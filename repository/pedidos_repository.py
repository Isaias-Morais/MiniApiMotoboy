from models.motoboy import Motoboy
from models.pedido import Pedidos
from sqlalchemy.orm import Session
from models.enum import StatusPedidos

def listar_pedidos_repository(session:Session):
    return session.query(Pedidos).all()


def alterar_pedidos_status_repository(session:Session,pedido:Pedidos,status:StatusPedidos):
    pedido = pedido

    if not pedido:
        return None

    pedido.status = status
    session.flush()
    session.commit()
    session.refresh(pedido)
    return pedido

def busca_pedido_repository(session:Session,id:int):
    pedido = session.query(Pedidos).filter(Pedidos.id == id).first()

    if not pedido:
        return None

    return pedido

def deletar_pedido_repository(session:Session,id:int):
    pedido = busca_pedido_repository(session,id)

    if not pedido:
        return None

    session.delete(pedido)
    session.commit()
    return pedido


def defini_motoboy_id_pedido_repository(session:Session,pedido:Pedidos,motoboy:Motoboy):

    pedido.motoboy_id = motoboy.id
    session.flush()
    session.commit()
    session.refresh(pedido)
    return pedido

