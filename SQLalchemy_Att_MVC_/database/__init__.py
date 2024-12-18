from flask_sqlalchemy import SQLAlchemy # type: ignore

db = SQLAlchemy()

def init_db(app):
    app.config['SECRET_KEY'] = "superdificil2"
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banco.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    with app.app_context():
        db.create_all()