from database.base import Base
from database.engine import engine
from models.motoboy import Motoboy
from models.pedido import Pedidos

Base.metadata.create_all(bind=engine)