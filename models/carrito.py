from config.database import Base
from sqlalchemy import Integer, Column, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from models import producto


class Carrito(Base):
    __tablename__ = 'carrito'


    id_orden = Column(Integer, primary_key=True, index=True, autoincrement=True, nullable=False)
    cc = Column(Integer, ForeignKey("Users.idpeople"))

    is_active= Column(Boolean, primary_key=True)


    person = relationship("Users", back_populates="Carrito")
    item = relationship("Item", back_populates="Carrito")