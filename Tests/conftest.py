import pytest
from selenium import webdriver
import time
driver = None

@pytest.fixture(scope="class")

def setup(request):
    global driver
    driver = webdriver.Chrome()
    driver.get("https://www.naukri.com/")
    driver.maximize_window()

    request.cls.driver = driver
    yield
    driver.close()

