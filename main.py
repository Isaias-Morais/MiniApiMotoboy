from fastapi import FastAPI
from database.engine import engine
from routers.pedidos import router as pedido_router
from routers.motoboy import router as motoboy_router
from database.base import Base

import models.motoboy
import models.pedido
app = FastAPI()

@app.get('/')
async def home():
    return {"message":"acesse '/docs' "}

@app.on_event('startup')
def startup():
    Base.metadata.create_all(engine)
app.include_router(pedido_router)

app.include_router(motoboy_router)