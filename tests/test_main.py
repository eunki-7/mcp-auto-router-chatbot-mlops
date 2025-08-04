"""Basic unit tests for inference API."""
from fastapi.testclient import TestClient
from src.inference.main import app

client = TestClient(app)

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"

def test_chat_endpoint():
    response = client.post("/chat", json={"text": "Hello"})
    assert response.status_code == 200
    assert "response" in response.json()
