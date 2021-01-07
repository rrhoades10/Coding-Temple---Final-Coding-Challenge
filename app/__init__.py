from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate 
from flask_login import LoginManager
from flask_moment import Moment 
from config import Config

db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()
moment = Moment()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)
    moment.init_app(app)

    from .blueprints.main import bp as main_bp
    app.register_blueprint(main_bp)
    
    from .blueprints.auth import bp as auth_bp
    app.register_blueprint(auth_bp)

    return app
