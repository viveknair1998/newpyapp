from sqlalchemy import Column, Integer, String
from .database import Base

class Registro(Base):
    __tablename__ = "registros"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)