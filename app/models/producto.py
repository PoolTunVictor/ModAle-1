from sqlalchemy import Column, Integer, String, Text, DECIMAL, Boolean
from sqlalchemy.orm import relationship
from ..database.database import Base

class Producto(Base):
    __tablename__ = "productos"
    id_producto = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100))
    descripcion = Column(Text)
    caracteristicas = Column(Text)
    precio = Column(DECIMAL(10, 2))
    stock = Column(Integer)
    activo = Column(Boolean, default=True)

    detalles = relationship("DetallePedido", back_populates="producto")
    movimientos = relationship("MovimientoStock", back_populates="producto")
