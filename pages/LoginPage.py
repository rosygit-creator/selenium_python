from selenium.webdriver.common.by import By
# import pytest

# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC



# Navigate to a website
class LoginPage:
    def __init__(self, driver):
        self.driver=driver
    
    usernm="user-name"
    passw="password"
    login="login-button"

    def get_url(self, url):
        self.driver.get(url)

    def input_username(self,username):
        # print("self user ####", self.usernm)
        # self.driver.get("https://www.saucedemo.com/")
        self.driver.find_element(By.ID, self.usernm).send_keys(username)
      
    def input_password(self,password):
        self.driver.find_element(By.ID, self.passw).send_keys(password)
        

    def click_login(self):  
        self.driver.find_element(By.ID, self.login).click
       
# @pytest.fixture(scope="session")
# def login_page(driver):
#     # Instantiate LoginPage once for the session
#     print("inside login_page")
#     obj=LoginPage(driver)
#     return obj
