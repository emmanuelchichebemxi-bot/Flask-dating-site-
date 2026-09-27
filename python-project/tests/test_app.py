from app import app


def test_index_returns_welcome_message() -> None:
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200
    assert response.get_json() == {"message": "Hello from Flask!"}


def test_health_returns_ok() -> None:
    client = app.test_client()

    response = client.get("/health")

    assert response.status_code == 200
    assert response.get_json() == {"status": "ok"}