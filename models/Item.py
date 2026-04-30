from config.database import Base
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

class Item(Base):
    __tablename__ = 'Item'

    id_item = Column(Integer, primary_key=True)
    quantity = Column(Integer, nullable=False)

    id_orden= Column(Integer, ForeignKey('Carrito.id_orden'))


    item = relationship("Producto", back_populates="Item")
    car = relationship("Carrito", back_populates="Item")