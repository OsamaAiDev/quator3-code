from fastapi.testclient import TestClient
from class02_q5.main import app

# test 1 
# code req send kre ga server pr or response check kre ga
def test_root_path():
    client = TestClient(app = app)
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}

# test 2
def test_piaic_description():
    client = TestClient(app = app)
    response = client.get("/piaic")
    assert response.status_code == 200
    assert response.json() == {"organization": "Piaic"}

    # test 3 fail test
def test_third_check():
    client = TestClient(app = app)
    response = client.get("/piaic")
    assert response.status_code == 200
    assert response.json() == {"organization": "Osama"}