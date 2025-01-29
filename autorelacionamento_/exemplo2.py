from sqlalchemy import create_engine, ForeignKey, select
from sqlalchemy.orm import Session
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.orm import relationship
from typing import List 

engine = create_engine('sqlite:///exemplo1.db')
session = Session(bind=engine)

class Base(DeclarativeBase):
    pass 


class Medico(Base):
    __tablename__= 'medicos'
    id:Mapped[int] = mapped_column(primary_key=True)
    pass

class Paciente(Base):
    __tablename__ = 'pacientes'
    d:Mapped[int] = mapped_column(primary_key=True)
    pass





