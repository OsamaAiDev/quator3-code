from fastapi.testclient import TestClient
from fastapi import FastAPI
from todo_api import settings
from sqlmodel import SQLModel, Session, create_engine
from todo_api.main import app, get_session
import pytest

connection_string: str = str(settings.TEST_DATABASE_URL).replace("postgresql", "postgresql+psycopg")
engine = create_engine(connection_string, connect_args={"sslmode": "require"}, pool_recycle=300)

"""
Refactor with pytest fixture

"""
@pytest.fixture(scope="module", autouse=True)
def get_db_session():
    SQLModel.metadata.create_all(engine)
    yield Session(engine)

@pytest.fixture(scope="function")
def test_app(get_db_session):
    def test_session():
        yield get_db_session()
    app.dependency_overrides["get_session"] = test_session
    with TestClient(app = app) as client:
        yield client

# Test 1: Root Test
def test_root():
    client = TestClient(app = app)
    response = client.get("/")
    data = response.json()

    assert response.status_code == 200
    assert data == {"message": "Wecome to my todo API!"}

# Test 2: Post Todo Test
def test_create_todo(test_app):

    test_todo_record = {"content": "Test task 1", "is_completed": True}
    response = test_app.post("/todos/", json = test_todo_record)
    data = response.json()

    assert response.status_code == 200
    assert data["content"] == test_todo_record["content"]

# Test 3: Get All Todos
def test_get_all_todos(test_app):

    test_todo_record = {"content": "Test task all todos", "is_completed": True}
    response = test_app.post("/todos/", json = test_todo_record)
    data = response.json()

    todos_list_response = test_app.get("/todos/")
    newly_created_todo_response = todos_list_response.json()[-1]

    assert todos_list_response.status_code == 200
    assert newly_created_todo_response["content"] == test_todo_record["content"]

    # Test 4: Single Todo Test
def test_get_single_todo(test_app):

    test_todo_record = {"content": "Get single todo test", "is_completed": True}
    response = test_app.post("/todos/", json = test_todo_record)
    todo_id = response.json()["id"]

    single_todo_res = test_app.get(f"/todos/{todo_id}/")
    single_todo_data = single_todo_res.json()

    assert single_todo_res.status_code == 200
    assert single_todo_data["content"] == test_todo_record["content"]

# Test 5 - Update Todo
def test_update_todo(test_app):

    test_todo_record = {"content": "Update single todo test", "is_completed": True}
    response = test_app.post("/todos/", json = test_todo_record)
    todo_id = response.json()["id"]

    updated_todo_record = {"content": "Updated single todo test", "is_completed": True}
    updated_todo_response = test_app.put(f"/todos/{todo_id}/", json = updated_todo_record)
    updated_todo_data = updated_todo_response.json()

    assert updated_todo_response.status_code == 200
    assert updated_todo_data["content"] == updated_todo_record["content"]

# Test 6: Delete Todo

def test_delete_todo(test_app):

    test_todo_record = {"content": "Delete single todo test", "is_completed": True}
    response = test_app.post("/todos/", json = test_todo_record)
    todo_id = response.json()["id"]
    deleted_todo_response = test_app.delete(f"/todos/{todo_id}/")
    deleted_todo_data = deleted_todo_response.json()

    assert deleted_todo_response.status_code == 200
    assert deleted_todo_data["message"] == "Task successfully deleted"