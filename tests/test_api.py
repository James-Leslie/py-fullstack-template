"""Tests for the FastAPI backend."""

from fastapi.testclient import TestClient

from api.main import app

client = TestClient(app)


def test_health() -> None:
    """Health endpoint returns healthy status."""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}


def test_increment_default() -> None:
    """Increment with default amount."""
    response = client.post("/counter/increment", json={"value": 5})
    assert response.status_code == 200
    assert response.json() == {"result": 6}


def test_increment_custom_amount() -> None:
    """Increment with custom amount."""
    response = client.post("/counter/increment", json={"value": 10, "amount": 5})
    assert response.status_code == 200
    assert response.json() == {"result": 15}


def test_decrement_default() -> None:
    """Decrement with default amount."""
    response = client.post("/counter/decrement", json={"value": 10})
    assert response.status_code == 200
    assert response.json() == {"result": 9}


def test_decrement_custom_amount() -> None:
    """Decrement with custom amount."""
    response = client.post("/counter/decrement", json={"value": 20, "amount": 7})
    assert response.status_code == 200
    assert response.json() == {"result": 13}
