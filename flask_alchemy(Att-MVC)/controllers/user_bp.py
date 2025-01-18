from flask import Blueprint, render_template, url_for, redirect, request, flash, session, make_response

from models.user_model import User

from database import db

user_bp = Blueprint('user', __name__)

@user_bp.route('/')
def index():
    return render_template('index.html')

@user_bp.route('/create_user', methods=['POST', 'GET'])
def create_user():
    if request.method == 'POST':

        nome = request.form['nome']
        email = request.form['email']

        User.create_user(nome, email)

        flash("Usuário registrado com sucesso!", 'success')
        return redirect(url_for('admin.listar'))

    return render_template('create_user.html')