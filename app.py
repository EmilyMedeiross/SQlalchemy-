from flask import Flask, url_for, request, render_template,  flash, redirect 
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from models import Base, User

engine = create_engine('sqlite:///database.db')

Base.metadata.create_all(bind=engine)

app = Flask(__name__)
app.config['SECRET_KEY'] =  "SENHA"

session = Session(bind=engine)


@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template('index.html')

@app.route('/cadastrar', methods=['POST', 'GET'])
def cadastrar():
    if request.method == 'POST':
        user = User(
            nome = request.form['nome']
        )
        
        session.add(user)
        session.commit()
        return redirect(url_for('index'))
        
    return render_template('cadastro.html')
