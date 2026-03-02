import pytest 
from pages.LoginPage import *
from utils.utils import *

# # Runs once per test class
# @pytest.fixture(scope="class")

# def setup_driver(request):
#     driver = webdriver.Chrome()
#     driver.maximize_window()

#     # driver.get("https://www.saucedemo.com/")

#     request.cls.driver = driver
#     #The yield statement pauses the fixture and provides the browser instance 
#     # to the test function. Once the test function finishes, execution returns to the 
#     # fixture to run the cleanup code after yield
#     yield driver

#     # teardown 
#     driver.quit()



# the setup_driver method will be called just once even if there are more than one 
# test methods as below

# commented since the setup_driver fixture is in conftest.py
@pytest.mark.usefixtures("setup_driver")

class TestLogin:
    url1="https://www.saucedemo.com/"
    url2="https://www.google.com/maps"
    
    def test_valid_login(self):
        get_url(self.driver, self.url1)

        login_page = LoginPage(self.driver)
        login_page.input_username("standard_user")
        login_page.input_password("secret_sauce")
        login_page.click_login()

        # Assertion is in the test class
        assert "Swag Labs" in self.driver.title 

    def test_google_browse(self):
        get_url(self.driver, self.url2)
        assert "Google" in self.driver.title



