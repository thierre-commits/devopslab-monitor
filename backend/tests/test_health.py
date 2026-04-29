from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health_endpoint(client):
    response = client.get("/health")

    assert response.status_code == 200

    data = response.json()

    assert data["status"] in ["ok", "error"]
    assert "database" in data
    assert "timestamp" in data
