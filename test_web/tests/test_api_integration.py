import pytest
from test_web.fixtures.web_fixtures import web_driver
from test_api.fixtures.api_fixtures import api_client

def test_api_integration(web_driver, api_client):
    web_driver.get("https://reqres.in/")
    response = api_client.get("/api/users?page=2")
    assert response.status_code == 200
    assert response.json()["success"] == True