from flask_sqlalchemy import SQLAlchemy 
from sqlalchemy.orm import DeclarativeBase 

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)

def init_db(app):
    app.config['SECRET_KEY'] = "Senha"
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banco.db'
    db.init_app(app)

    with app.app_context():
        db.create_all()


