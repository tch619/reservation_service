import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.schemas import Table


def test_create_table(client: TestClient):
    response = client.post("/tables/", json={
        "name": "VIP Table",
        "seats": 4,
        "location": "Second floor"
    })
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "VIP Table"
    assert data["seats"] == 4
    assert data["location"] == "Second floor"


def test_get_tables(client: TestClient):
    response = client.get("/tables/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert any(t["name"] == "VIP Table" for t in data)


def test_delete_table(client: TestClient):
    post_resp = client.post("/tables/", json={
        "name": "Temp Table",
        "seats": 2,
        "location": "Outside"
    })
    assert post_resp.status_code == 200
    table_id = post_resp.json()["id"]
    assert table_id is not None

    delete_resp = client.delete(f"/tables/{table_id}")
    assert delete_resp.status_code == 200
    assert delete_resp.json()["message"] == "Стол с id-2 успешно удален"
