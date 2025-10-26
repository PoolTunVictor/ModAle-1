from fastapi import FastAPI
from .database.database import Base, engine

from .controllers import (
    ClienteController,
    DetallePedidoController,
    ProductoController,
    DireccionController,
    MovimientoStockController,
    PedidoController
)
from .models import *


Base.metadata.create_all(bind=engine)

app = FastAPI(title="ModAle API", version="1.0")

app.include_router(ClienteController().router)
app.include_router(DireccionController().router)
app.include_router(ProductoController().router)

app.include_router(PedidoController().router)

app.include_router(DetallePedidoController().router)
app.include_router(MovimientoStockController().router)
