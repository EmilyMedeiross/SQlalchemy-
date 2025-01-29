
from sqlalchemy import create_engine, ForeignKey, select
from sqlalchemy.orm import Session
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.orm import relationship
from typing import List 

engine = create_engine('sqlite:///exemplo1.db')
session = Session(bind=engine)

class Base(DeclarativeBase):
    pass 

class User(Base):
    __tablename__= 'users'
    id:Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str]

    gerente_id = mapped_column(
        ForeignKey('users.id'),
        nullable=True)  # Auto-Referencia -> chave  estrangeira que refencia outro usuário na mesma tabela
    
    gerenciados: Mapped[List['User']] = relationship(
        'User',
         back_populates='gerente') # Lista de usuários que este usuário gerencia 

    gerente = relationship(
        'User',
        back_populates='gerenciados',
        remote_side=[id]) # Retorna o usuário que gerencia este usuário.
      
      # remote_side[id] -> Ele garante que, quando buscamos user.gerente, o SQLAlchemy sabe que deve buscar o usuário cujos id correspondem ao gerente_id do usuário atual.

    def __repr__(self) -> str:
        return self.nome

# back_populates: Garante a relação bidirecional: Se A é gerente de B, então B.gerente aponta para A, e A.gerenciados contém B.

    
    
Base.metadata.create_all(bind=engine)

# user1 = User(nome='Hugo')
# session.add(user1)
# session.commit()

# user2 = User(nome='Lucas', gerente_id=1)
# user3 = User(nome='Thiago', gerente_id=1)
# user4 = User(nome='Fabricio')
# user5 = User(nome='Hermenegildo')


# session.add_all([user2, user3, user4, user5])
# session.commit()

# Selecionando Usuário pelo ID 
sttm = select(User).where(User.id == 1)
print(sttm)

chefe = session.execute(sttm).scalars().first()
print(chefe.nome)

# Verifica quem o usuário chefe gerencia 
print(chefe.gerenciados)

# Verificando o gerente de um usuário

sttm = select(User).where(User.id == 4)
pessoa = session.execute(sttm).scalars().first()
print("Eu sou:" + str(pessoa))
print("Meu chefe é:" + str(pessoa.gerente))