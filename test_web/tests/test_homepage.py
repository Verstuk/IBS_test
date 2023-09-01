import pytest

def test_homepage_title(web_driver):
    web_driver.get("https://reqres.in/")
    assert web_driver.title == " Reqres - A hosted REST-API ready to respond to your AJAX requests "

