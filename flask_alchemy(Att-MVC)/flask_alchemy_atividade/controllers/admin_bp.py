from flask import Blueprint, render_template

from models.user_model import User
from models.book_model import Book

admin_bp = Blueprint('admin', __name__)

@admin_bp.route('/')
def index():
    return render_template('index.html')

@admin_bp.route('/listar')
def listar():
    users = User.query.all()  
    books = Book.query.all()  
    return render_template('listar.html', users=users, books=books)