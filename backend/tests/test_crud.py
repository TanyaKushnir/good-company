import pytest
from sqlalchemy.orm import Session
from app import crud
from app.database import SessionLocal, engine
from app.models import User, Store, Product

# Setup and teardown fixtures

@pytest.fixture(scope="module")
def setup_database():
    # Create tables
    User.__table__.create(bind=engine)
    Store.__table__.create(bind=engine)
    Product.__table__.create(bind=engine)
    yield
    # Drop tables
    Product.__table__.drop(bind=engine)
    Store.__table__.drop(bind=engine)
    User.__table__.drop(bind=engine)

@pytest.fixture
def db_session(setup_database):
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Tests for CRUD operations

def test_create_user(db_session: Session):
    user_data = {
        "username": "testuser",
        "password": "testpassword",
        "role": "user"
    }
    created_user = crud.create_user(db_session, user_data)
    assert created_user.id is not None
    assert created_user.username == "testuser"
    assert created_user.role == "user"

def test_get_user(db_session: Session):
    user_data = {
        "username": "testuser",
        "password": "testpassword",
        "role": "user"
    }
    created_user = crud.create_user(db_session, user_data)
    retrieved_user = crud.get_user(db_session, created_user.id)
    assert retrieved_user is not None
    assert retrieved_user.id == created_user.id

def test_update_user(db_session: Session):
    user_data = {
        "username": "testuser",
        "password": "testpassword",
        "role": "user"
    }
    created_user = crud.create_user(db_session, user_data)
    update_data = {
        "role": "admin"
    }
    updated_user = crud.update_user(db_session, created_user.id, update_data)
    assert updated_user is not None
    assert updated_user.role == "admin"

def test_delete_user(db_session: Session):
    user_data = {
        "username": "testuser",
        "password": "testpassword",
        "role": "user"
    }
    created_user = crud.create_user(db_session, user_data)
    deleted_user = crud.delete_user(db_session, created_user.id)
    assert deleted_user is not None
    assert deleted_user.id == created_user.id
    assert crud.get_user(db_session, created_user.id) is None

# Add similar tests for other CRUD operations (create_store, get_store, update_store, delete_store, etc.)
