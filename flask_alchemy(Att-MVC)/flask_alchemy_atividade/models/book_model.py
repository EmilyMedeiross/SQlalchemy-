from database import db
from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import Text 

class Book(db.Model):
    __tablename__ = 'books'
    id:Mapped[int] = mapped_column(primary_key=True)
    titulo:Mapped[str] = mapped_column("titulo", Text, nullable=False )
    autor:Mapped[str]= mapped_column("autor", Text, nullable=False )

    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor 

    def create_book(titulo, autor):
        new_book = Book(titulo=titulo,autor=autor)
        db.session.add(new_book)
        db.session.commit()