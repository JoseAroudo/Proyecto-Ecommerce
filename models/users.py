from sqlite3 import Date

from config.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class Users(Base):
    __tablename__ = 'Users'

    id_people = Column(String,primary_key=True)
    name = Column(Integer, nullable=False)
    last_name = Column(String,nullable=False)
    cellphone = Column(String,nullable=False)
    birthdate= Column(Date,nullable=False)
    #todo podría ir fecha de nacimiento? para comprobar si es mayor de edad
    email = Column(String,nullable=False)

    item = relationship("Item", back_populates="Users")
    car = relationship("Carrito", back_populates="Users")