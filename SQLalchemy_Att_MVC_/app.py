from flask import Flask 
from flask_login import LoginManager
from database import init_db 
from controllers.user import user_bp 
from models.user_model import Usuario


app = Flask(__name__)
app.config['SECRET_KEY'] =  "SENHA"

login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return Usuario.query.get(int(user_id))

init_db(app)

app.register_blueprint(user_bp)

if __name__ == "__main__":
    app.run(debug=True)
            
