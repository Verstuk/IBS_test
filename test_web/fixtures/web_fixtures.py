import pytest
from selenium import webdriver

@pytest.fixture(scope="session")
def web_driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()