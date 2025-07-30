from flask import Flask
from .extensions import db, jwt, cors, migrate
from .models import init_app_models

# ✅ IMPORT YOUR BLUEPRINT
from app.routes.auth import auth_bp

def create_app():
    app = Flask(__name__)
    
    # Load config
    app.config.from_object("config.Config")

    # Initialize extensions
    db.init_app(app)
    jwt.init_app(app)
    cors.init_app(app)
    migrate.init_app(app, db)

    # ✅ REGISTER BLUEPRINT
    app.register_blueprint(auth_bp, url_prefix="/auth")

    # Load models
    init_app_models()

    return app
