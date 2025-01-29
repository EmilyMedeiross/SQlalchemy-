from sqlalchemy import create_engine
from sqlalchemy.orm import Session 
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped, mapped_column

from sqlalchemy import Table, Column, ForeignKey

from sqlalchemy.orm import relationship 

from typing import List

engine = create_engine('sqlite:///exemplo1.db')
session = Session(bind=engine)

class Base(DeclarativeBase):
    pass


estudante_curso= Table(
    "estudantes_cursos",
    Base.metadata,
    Column('estudante_id', ForeignKey('estudantes.id'), primary_key=True),
    Column('curso_id', ForeignKey('cursos.id'), primary_key=True)
)

# Relacionamento  NxN 

class Curso(Base):
    __tablename__= 'cursos'
    id:Mapped[int] = mapped_column(primary_key=True)
    nome:Mapped[str]
    estudantes: Mapped[List['Estudante']] = relationship(
        'Estudante',
        secondary=estudante_curso,
        back_populates='cursos'
    ) 

class Estudante(Base):
    __tablename__= 'estudantes'
    id:Mapped[int] = mapped_column(primary_key=True)
    nome:Mapped[str]
    cursos: Mapped[List['Curso']] = relationship(
        'Curso',
        secondary=estudante_curso,
        back_populates='estudantes'
    ) 
  
Base.metadata.create_all(bind=engine)

info = Curso(nome='Informática')
session.add(info)
session.commit()

x = Estudante(nome='Estudante1', curso_id=1)
y = Estudante(nome='Estudante2', curso_id=1 )
z = Estudante(nome='Estudante3')

session.add_all([x, y, z])
session.commit()

info.estudantes.append(x)
info.estudantes.append(y)
session.commit()

info.estudantes.remove(x)
session.commit()


