import pytest

def test_api_integration(web_driver, api_client):
    web_driver.get("https://reqres.in/")
    response = api_client.get("/api/users?page=2")
    assert response.status_code == 200
    assert response.json()["success"] == True