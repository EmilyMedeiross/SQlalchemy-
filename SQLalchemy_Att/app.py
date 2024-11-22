from flask import Flask, render_template, flash, request, redirect, url_for
from sqlalchemy import create_engine, Column, String, Integer, Boolean
from sqlalchemy.orm import sessionmaker, declarative_base 

db = create_engine("sqlite:///banco.db")

Session = sessionmaker(bind=db)
session = Session()

Base = declarative_base()

app = Flask(__name__)
app.config['SECRET_KEY'] =  "SENHA"


class Usuario(Base):
    __tablename__  = "usuarios"
    id = Column("id", Integer, primary_key = True, autoincrement=True)
    email = Column("email", String)
    senha = Column("senha", String)
    ativo = Column("ativo", Boolean)

    def __init__(self, email, senha, ativo=True):
        self.email = email
        self.senha = senha 
        self.ativo = ativo 

Base.metadata.create_all(bind=db)
            
@app.route('/')
def index():
    users = session.query(Usuario).all()
    return render_template('pages/index.html', users= users)

@app.route('/create', methods=['POST', 'GET'])
def create():
    if request.method == 'POST':
        user = Usuario(
            email = request.form['email'],
            senha= request.form['password']
        )
        if not user.email:
            flash('Email é obrigatório')
        else:
          session.add(user)
          session.commit()
          return redirect(url_for('index'))
    
    return render_template('pages/create.html')

@app.route('/<int:id>/edit', methods=['POST', 'GET'])
def edit(id):

    user = session.query(Usuario).filter(Usuario.id == id).first()

    if user == None:
        return redirect(url_for('error', message='Usuário Inexistente'))

    if request.method == 'POST':

        user.email = request.form['email']
        session.commit()
        return redirect(url_for('index'))
    
    return render_template('pages/edit.html', user=user)

@app.route('/<int:id>/delete', methods=['POST', 'GET'])
def delete(id):

    user = session.query(Usuario).filter(Usuario.id == id).first()
    
    if user == None:
        return redirect(url_for('error', message='Usuário Inexistente'))
    
    if request.method == 'POST':
        session.delete(user)
        session.commit()
        return redirect(url_for('index'))
    
    return render_template('pages/delete.html', user=user)
    
    
@app.route('/error')
def error():
    error = request.args.get('message')
    return render_template('errors/error.html', message=error)