from database.base import Base
from database.engine import engine
from models.motoboy import Motoboy
from models.pedido import Pedidos

def criar_tabelas():
    return Base.metadata.create_all(bind=engine)