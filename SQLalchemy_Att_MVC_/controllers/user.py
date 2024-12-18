from flask import Blueprint, render_template, url_for, redirect, request, flash, session, make_response

from flask_login import login_user, login_required, logout_user, current_user

from werkzeug.security import generate_password_hash, check_password_hash

from models.user_model import Usuario

from database import db 

user_bp = Blueprint('user', __name__)

@user_bp.route('/')
def index():
    users = Usuario.query.all()
    return render_template('index.html', users=users)

@user_bp.route('/create', methods=['POST', 'GET'])
def create():
    if request.method == 'POST':

        email = request.form['email']
        senha = request.form['password']

        senha_hashed = generate_password_hash(senha)

        Usuario.create(email, senha_hashed)

        flash("Usuário registrado com sucesso!", 'success')
        user = Usuario.get_email(email)
        login_user(user)
        return redirect(url_for('user.index'))

    return render_template('create.html')

@user_bp.route('/<int:id>/edit', methods=['POST', 'GET'])
def edit(id):
    user = db.session.query(Usuario).filter(Usuario.id == id).first()
    
    if user is None:
        return redirect(url_for('error', message='Usuário Inexistente'))
    
    if request.method == 'POST':
        new_email = request.form['email']
        
        # Chama o método modify (controllers) para atualizar o email
        Usuario.modify(new_email, id)
        
        return redirect(url_for('user.index'))
    
    return render_template('edit.html', user=user)

@user_bp.route('/<int:id>/delete', methods=['POST', 'GET'])
def delete(id):
    user = db.session.query(Usuario).filter(Usuario.id == id).first()
    
    if user is None:
        return redirect(url_for('error', message='Usuário Inexistente'))
    
    if request.method == 'POST':
        try:
            Usuario.delete_user(id)
            return redirect(url_for('user.index'))
        except Exception as e:
            return redirect(url_for('error', message='Erro ao deletar usuário.'))
    
    return render_template('delete.html', user=user)
