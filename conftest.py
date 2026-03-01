import pytest
from selenium import webdriver
# Runs once per test class
@pytest.fixture(scope="class")

def setup_driver(request):
    driver = webdriver.Chrome()
    driver.maximize_window()

    # driver.get("https://www.saucedemo.com/")

    request.cls.driver = driver
    #The yield statement pauses the fixture and provides the browser instance 
    # to the test function. Once the test function finishes, execution returns to the 
    # fixture to run the cleanup code after yield
    yield driver

    # teardown 
    driver.quit()
