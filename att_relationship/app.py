from flask import Flask, render_template, request, redirect, url_for
from sqlalchemy import create_engine, Column, String, Integer, DateTime, ForeignKey, Table
from sqlalchemy.orm import sessionmaker, declarative_base, relationship
from datetime import datetime



app = Flask(__name__)
engine = create_engine('sqlite:///banco.db', echo=True)
Session = sessionmaker(bind=engine)
Base = declarative_base()


locacao_veiculos = Table(
    'locacao_veiculos',
    Base.metadata,
    Column('cliente_id', Integer, ForeignKey('clientes.id'), primary_key=True),
    Column('veiculo_id', Integer, ForeignKey('veiculos.id'), primary_key=True),
    Column('data_locacao', DateTime, default=datetime)
)

class Cliente(Base):
    __tablename__ = 'clientes'
    id = Column(Integer, primary_key=True)
    nome = Column(String(100), nullable=False)
    cpf = Column(String(14), unique=True, nullable=False)
    telefone = Column(String(15), nullable=False)
    veiculos = relationship('Veiculo', secondary=locacao_veiculos, back_populates='clientes')


class Veiculo(Base):
    __tablename__ = 'veiculos'
    id = Column(Integer, primary_key=True)
    modelo = Column(String(100), nullable=False)
    marca = Column(String(100), nullable=False)
    ano = Column(String(4), nullable=False)
    clientes = relationship('Cliente', secondary=locacao_veiculos, back_populates='veiculos')


Base.metadata.create_all(engine)

# Rotas  --------------------------------------------------------------------------------------------
@app.route('/')
def index():
    return render_template('index.html')

# Cadastrar Cliente
@app.route('/cadastrar_clientes', methods=['GET', 'POST'])
def cadastrar_clientes():
    if request.method == 'POST':
        nome = request.form['nome']
        cpf = request.form['cpf']
        telefone = request.form['telefone']

        session = Session()
        novo_cliente = Cliente(nome=nome, cpf=cpf, telefone=telefone)
        session.add(novo_cliente)
        session.commit()
        session.close()

        return redirect(url_for('listar'))

    return render_template('cadastrar_clientes.html')


@app.route('/cadastrar_veiculos', methods=['GET', 'POST'])
def cadastrar_veiculos():
    if request.method == 'POST':
        modelo = request.form['modelo']
        marca = request.form['marca']
        ano = request.form['ano']

        session = Session()
        novo_veiculo = Veiculo(modelo=modelo, marca=marca, ano=ano)
        session.add(novo_veiculo)
        session.commit()
        session.close()

        return redirect(url_for('listar'))

    return render_template('cadastrar_veiculos.html')

@app.route('/cadastrar_locacao', methods=['GET', 'POST'])
def cadastrar_locacao():
    session = Session()
    clientes = session.query(Cliente).all()
    veiculos = session.query(Veiculo).all()

    if request.method == 'POST':
        cliente_id = request.form['cliente_id']
        veiculo_id = request.form['veiculo_id']

        session.execute(
            locacao_veiculos.insert().values(cliente_id=cliente_id, veiculo_id=veiculo_id)
        )
        session.commit()
        session.close()

        return redirect(url_for('listar'))

    session.close()
    return render_template('cadastrar_locacao.html', clientes=clientes, veiculos=veiculos)


@app.route('/listar')
def listar():
    session = Session()
    clientes = session.query(Cliente).all()
    veiculos = session.query(Veiculo).all()
    locacoes = session.query(locacao_veiculos).all()

    # Recupera detalhes das locações
    locacoes_detalhadas = []
    for locacao in locacoes:
        cliente = session.query(Cliente).get(locacao.cliente_id)
        veiculo = session.query(Veiculo).get(locacao.veiculo_id)
        locacoes_detalhadas.append({
            'cliente': cliente.nome,
            'veiculo': f"{veiculo.marca} {veiculo.modelo}",
            'data_locacao': locacao.data_locacao
        })

    session.close()
    return render_template('listar.html', clientes=clientes, veiculos=veiculos, locacoes=locacoes_detalhadas)


if __name__ == '__main__':
    app.run(debug=True)