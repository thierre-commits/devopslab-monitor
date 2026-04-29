from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

def test_create_and_list_services(client):
    response = client.post(
        "/services",
        json={"name": "API Test", "url": "http://test.com"},
    )

    assert response.status_code == 200

    data = response.json()
    assert data["name"] == "API Test"

    response = client.get("/services")
    assert response.status_code == 200

    data = response.json()
    assert len(data) == 1