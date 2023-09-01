import pytest

@pytest.mark.parametrize("endpoint", ["/api/users?page=2"])
def test_get_list_users(api_client):
    response = api_client.get("endpoint")
    assert response.status_code == 200
    assert response.json()["text"] == "To keep ReqRes free, contributions towards server costs are appreciated!"

@pytest.mark.parametrize("endpoint", ["/api/users"])
def test_post_create(api_client):
    data = {
            "name": "morpheus",
            "job": "leader"
    }
    response = api_client.post("endpoint", data)
    assert response.status_code == 201

@pytest.mark.parametrize("endpoint", ["/api/login"])
def test_post_login(api_client):
    data = {
            "email": "eve.holt@reqres.in",
            "password": "cityslicka"
    }

    response = api_client.post("endpoint", data)
    assert response.status_code == 200

@pytest.mark.parametrize("endpoint", ["/api/register"])
def test_post_register(api_client):
    data = {
            "email": "eve.holt@reqres.in",
            "password": "pistol"
    }

    response = api_client.post("endpoint", data)
    assert response.status_code == 200

