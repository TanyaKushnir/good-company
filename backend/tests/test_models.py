import pytest
from sqlalchemy.orm import Session
from app import models
from app.database import SessionLocal, engine

# Setup and teardown fixtures

@pytest.fixture(scope="module")
def setup_database():
    models.Base.metadata.create_all(bind=engine)
    yield
    models.Base.metadata.drop_all(bind=engine)

@pytest.fixture
def db_session(setup_database):
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Tests for models

def test_create_user(db_session: Session):
    user_data = {
        "username": "testuser",
        "password": "testpassword",
        "role": "user"
    }
    user = models.User(**user_data)
    db_session.add(user)
    db_session.commit()
    assert user.id is not None
    assert user.username == "testuser"
    assert user.role == "user"

def test_create_store(db_session: Session):
    store_data = {
        "store_name": "Test Store",
        "store_description": "This is a test store"
        # Add other required fields as per your Store model
    }
    store = models.Store(**store_data)
    db_session.add(store)
    db_session.commit()
    assert store.id is not None
    assert store.store_name == "Test Store"
    # Add more assertions based on your Store model fields
