import pytest
from fastapi.testclient import TestClient
from app.main import app
from datetime import datetime


def test_create_reservation(client: TestClient):
    reservation_data = {
        "customer_name": "Миша",
        "table_id": 1,
        "reservation_time": "2025-04-15T19:00:00",
        "duration_minutes": 120
    }

    response = client.post("/reservations/", json=reservation_data)
    assert response.status_code == 200
    data = response.json()

    assert "id" in data
    assert data["customer_name"] == "Миша"
    assert data["table_id"] == 1
    assert data["reservation_time"] == "2025-04-15T19:00:00"
    assert data["duration_minutes"] == 120


def test_get_reservations(client: TestClient):
    reservation_data = {
        "customer_name": "Саша",
        "table_id": 2,
        "reservation_time": "2025-04-16T20:00:00",
        "duration_minutes": 90
    }

    client.post("/reservations/", json=reservation_data)

    response = client.get("/reservations/")
    assert response.status_code == 200
    data = response.json()

    assert isinstance(data, list)
    assert len(data) > 0
    assert any(reservation["customer_name"] == "Саша" for reservation in data)


def test_delete_reservation(client: TestClient):
    reservation_data = {
        "customer_name": "Посетитель",
        "table_id": 1,
        "reservation_time": "2025-05-15T20:00:00",
        "duration_minutes": 60
    }

    post_resp = client.post("/reservations/", json=reservation_data)
    assert post_resp.status_code == 200
    reservation_id = post_resp.json()["id"]
    assert reservation_id is not None

    delete_resp = client.delete(f"/reservations/{reservation_id}")
    assert delete_resp.status_code == 200

    data = delete_resp.json()
    assert data["message"] == f"Бронь с id-{reservation_id} успешно удалена"


def test_invalid_date_format(client: TestClient):
    invalid_reservation_data = {
        "customer_name": "Упс что то не так",
        "table_id": 3,
        "reservation_time": "15-04-2025T19:00:00",
        "duration_minutes": 60
    }

    response = client.post("/reservations/", json=invalid_reservation_data)
    assert response.status_code == 422
    response_data = response.json()
    assert "detail" in response_data
    assert "Неверный формат даты" in response_data["detail"][0]["msg"]
