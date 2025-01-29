from sqlalchemy import create_engine
from sqlalchemy.orm import Session 
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import relationship

from typing import List
from sqlalchemy import Table, Column, ForeignKey

engine = create_engine('sqlite:///exemplo2.db')
session = Session(bind=engine)

class Base(DeclarativeBase):
    pass

# Relacionamento  1xN 

class Curso(Base):

    __tablename__= 'cursos'
    id:Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nome:Mapped[str]
    estudantes:Mapped[List['Estudante']] = relationship(
        'Estudante', backref='curso')

class Estudante(Base):
    __tablename__= 'estudantes'
    id:Mapped[int] = mapped_column(primary_key=True)
    nome:Mapped[str]
    curso_id = mapped_column(
        ForeignKey('cursos.id'), nullable=True)
    
    def __repr__(self) -> str:
        return f"Nome=({self.nome})"


Base.metadata.create_all(bind=engine)

# info = Curso(nome='Informática')
# session.add(info)
# session.commit()

# x = Estudante(nome='A', curso_id=1)
# y = Estudante(nome='B', curso_id=1 )
# z = Estudante(nome='C')

# session.add_all([x, y, z])
# session.commit()

info = Session.query(Curso).get(1)
print(info.estudantes)

x = session.query(Estudante).get(1)
print(x.curso)







