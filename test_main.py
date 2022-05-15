from fastapi.testclient import TestClient

from src.app import app

client = TestClient(app)


def test_read_demons():
    response = client.get("/demons")
    assert response.status_code == 200
    #assert response.json() == {"msg": "Hello World"}


def test_create_demon():
    test_params = {
        "name": "Test Demon",
        "description": "Test Demon Description",
        "url_image": "False_url_image"
    }
    response = client.post(
        "/demons/", json=test_params)
    assert response.status_code == 200
    #assert response.json() == test_params


if __name__ == "__main__":
    test_read_demons()
    test_create_demon()
