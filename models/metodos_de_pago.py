from config.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class Pay_metod(Base):
    __tablename__ = 'pay_metod'
    #todo revisar, creo que debe ser optional todo, creo
    card_number = Column(String,primary_key=True, nullable=False)
    card_type = Column(Integer, nullable= False)
    card_holder_name = Column(String, nullable=False)#Nombre del titular de la tarjeta
    bank= Column(String, nullable=False)
    cvc=Column(Integer, nullable=False)

    cc=Column(Integer,ForeignKey('Users.id_people'))

    #todo en estas relaciones las variables tienen el mismo nombre?
    pay = relationship("Users", back_populates="Pay_metod")