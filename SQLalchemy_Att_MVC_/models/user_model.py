from database import db
from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import Integer, Text, Boolean
from flask_login import UserMixin

class Usuario(db.Model, UserMixin):
    __tablename__  = "usuarios"

    id: Mapped[int] = mapped_column("id", Integer, primary_key = True, autoincrement=True)

    email: Mapped[str] = mapped_column("email", Text, nullable=False, unique=True)

    senha: Mapped[str] = mapped_column("senha", Text, nullable=False)

    def __init__(self, email, senha):
        self.email = email        
        self.senha = senha         

    @staticmethod
    def get_email(email):
        print(f"Buscando usuário com email:{email}")
        return db.session.query(Usuario).filter_by(email=email).first()
    
    @staticmethod 
    def create(email, senha):
        new_user = Usuario(email=email,senha=senha)
        db.session.add(new_user)
        db.session.commit()

    @staticmethod 
    def modify(email,id):
        user = db.session.query(Usuario).filter(Usuario.id == id).first()  
        user.email = email
        db.session.add(user)
        db.session.commit()
     
    @staticmethod
    def delete_user(id):
        user = db.session.query(Usuario).filter(Usuario.id == id).first()
        if user is None:
          raise ValueError("Usuário não encontrado.")
        db.session.delete(user)
        db.session.commit()