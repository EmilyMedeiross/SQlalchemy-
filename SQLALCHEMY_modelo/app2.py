from sqlalchemy import create_engine, Column, String, Integer, Boolean, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base 


db = create_engine("sqlite:///banco.db")
Session = sessionmaker(bind=db)
session = Session()

Base = declarative_base()

class Usuario(Base):
    __tablename__  = "usuarios"
    id = Column("id", Integer, primary_key = True, autoincrement=True)
    nome = Column ("nome", String)
    email = Column("email", String)
    senha = Column("senha", String)
    ativo = Column("ativo", Boolean)

    def __init__(self, nome, email, senha, ativo=True):
        self.nome = nome
        self.email = email
        self.senha = senha 
        self.ativo = ativo 

class Livro(Base):
    __tablename__ = "livros"
    id = Column("id", Integer, primary_key = True, autoincrement=True)
    titulo = Column('titulo', String)
    quant_paginas = Column("quant_paginas", Integer )
    autor = Column("autor", ForeignKey("usuarios.id" ))
    
    def __init__(self, titulo, quant_paginas, autor):
        self.titulo = titulo
        self.quant_paginas = quant_paginas
        self.autor = autor

Base.metadata.create_all(bind=db)
                
# CRUD (CRIAR, LER, ATUALIZAR, DELETAR)

# CRIAR 

# usuario = Usuario(nome='Archie', email='archieblass@gmail.com', senha='123456') 

# session.add(usuario)
# session.commit()


# usuario2 = Usuario(nome='Noah', email='noah@gmail.com', senha='123') 

# session.add(usuario2)
# session.commit()

#READ

#list_usuarios = session.query(Usuario).all()
# print(list_usuarios)

 #usuario_archie =session.query(Usuario).filter_by(email="archieblass@gmail.com").first()
# print(usuario_archie.nome)
# print(usuario_archie.email)

usuario_noah =session.query(Usuario).filter_by(email="noah@gmail.com").first()
print(usuario_noah.nome)
print(usuario_noah.email)


# livro =Livro(titulo="As aventuras de Ben", quant_paginas="350", autor = usuario_archie.id)

#  session.add(livro)
#  session.commit()

#UPDATE
# usuario_archie.nome = "Archie Bless"
# session.add(usuario_archie)
# session.commit()

#DELETE 

session.delete(usuario_noah)
session.commit()