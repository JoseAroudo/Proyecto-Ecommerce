from config.database import Base
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship

class Producto(Base):
    __tablename__ = 'producto'

    id_product = Column(Integer, primary_key=True)
    name = Column(String,nullable=False,unique=True)
    marca = Column(String,nullable=False)
    price = Column(Float,nullable=False)
    stock = Column(Integer,nullable=False)
    stock_quantity = Column(Integer,nullable=False)
    #created_at = Column(DateTime,nullable=False) Esto se puede hacer para tener en base de datos y no mostrarlo?
    description = Column(String,nullable=False)

    id_item=Column(Integer, ForeignKey('Items.id_item'))


    item = relationship("Item", back_populates="Producto")