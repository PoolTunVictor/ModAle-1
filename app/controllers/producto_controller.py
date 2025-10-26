from fastapi import Depends
from sqlalchemy.orm import Session
from ..models.producto import Producto
from .base_controller import BaseController

class ProductoController(BaseController):
    def __init__(self):
        super().__init__(Producto, "productos")