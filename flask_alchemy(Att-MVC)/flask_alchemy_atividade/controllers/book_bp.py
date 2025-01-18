from flask import Blueprint, render_template, url_for, redirect, request, flash, session, make_response

from models.book_model import Book

from database import db

book_bp = Blueprint('book', __name__)


@book_bp.route('/')
def index():
    return render_template('index.html')

@book_bp.route('/create_book', methods=['POST', 'GET'])
def create_book():
    if request.method == 'POST':

        titulo = request.form['titulo']
        autor = request.form['autor']

        Book.create_book(titulo, autor)

        flash("Livro registrado com sucesso!", 'success')
        return redirect(url_for('admin.listar'))

    return render_template('create_book.html')