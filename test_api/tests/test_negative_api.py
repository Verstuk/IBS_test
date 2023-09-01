import pytest

@pytest.mark.parametrize("endpoint", ["/api/login"])
def test_post_login(api_client):
    data = {
        "email": "peter@klaven"
    }

    response = api_client.post("endpoint", data)
    assert response.status_code == 400

@pytest.mark.parametrize("endpoint", ["/api/register"])
def test_post_register(api_client):
    data = {
    "email": "sydney@fife"
    }

    response = api_client.post("endpoint", data)
    assert response.status_code == 400