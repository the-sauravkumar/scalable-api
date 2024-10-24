import pytest
from app import create_app, db
from app.models import User

@pytest.fixture
def app():
    app = create_app('testing')
    return app

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def db_init(app):
    with app.app_context():
        db.create_all()
        yield db
        db.session.remove()
        db.drop_all()