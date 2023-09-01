import pytest
from test_api.utils.api_utils import APIClient

@pytest.fixture(scope="session")
def api_client():
    base_url = "https://reqres.in/"
    return APIClient(base_url)

