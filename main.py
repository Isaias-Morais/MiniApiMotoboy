from fastapi import FastAPI
from routers.pedidos import router as pedido_router

app = FastAPI()

app.include_router(pedido_router)