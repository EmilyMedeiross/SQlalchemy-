from flask import Flask 
from database import init_db 
from controllers.user_bp import user_bp 
from controllers.book_bp import book_bp 
from controllers.admin_bp import admin_bp


app = Flask(__name__)
app.config['SECRET_KEY'] =  "SENHA"


init_db(app)

app.register_blueprint(user_bp)
app.register_blueprint(book_bp)
app.register_blueprint(admin_bp)

if __name__ == "__main__":
    app.run(debug=True)
            