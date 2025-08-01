import pytest
from app import create_app
from app.extensions import db
from app.models.user import User, UserRole
from flask_jwt_extended import create_access_token

@pytest.fixture
def app():
    app = create_app()
    app.config.update({
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:",
        "JWT_SECRET_KEY": "test-secret"
    })

    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def admin_token(app):
    admin = User(name="Admin", email="admin@test.com", role=UserRole.ADMIN)
    admin.set_password("admin123")
    db.session.add(admin)
    db.session.commit()
    return create_access_token(identity=admin.id)
