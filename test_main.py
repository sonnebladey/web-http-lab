from fastapi.testclient import TestClient
from main import app
client = TestClient(app)

def test_health():
    responce = client.get("/health")
    assert responce.status_code == 200
    assert responce.json() == {"status":"ok"}
def test_hello():
    responce = client.get("/hello")
    assert responce.status_code == 200
    assert responce.json() == {"message":"Hello from Notes API"}
def test_missing():
    responce = client.get("/missing")
    assert responce.status_code == 404