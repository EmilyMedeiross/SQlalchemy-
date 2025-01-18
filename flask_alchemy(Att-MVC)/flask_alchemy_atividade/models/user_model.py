from database import db
from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import Text 


class User(db.Model):
    __tablename__ = 'users'
    id:Mapped[int] = mapped_column(primary_key=True)
    nome:Mapped[str] = mapped_column("nome", Text, nullable=False )
    email:Mapped[str] = mapped_column("email", Text, nullable=False, unique=True)
     
    def __init__ (self, nome, email):
        self.nome = nome
        self.email = email

    def create_user(nome, email):
        new_user = User(nome=nome,email=email)
        db.session.add(new_user)
        db.session.commit()