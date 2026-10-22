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

def test_get_note_id():
    responce = client.post("/notes", json={
        "title":"Test", 
        "content":"My first note"
    })
    note_id = responce.json()["id"]
    get_responce = client.get(f"/notes/{note_id}")

    assert get_responce.status_code == 200
    assert get_responce.json()["id"] == note_id


def test_head_health():
    response = client.head("/health")
    assert response.status_code == 200
    assert response.content == b""  # b"" no responce body
