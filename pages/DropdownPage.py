
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DropdownPage:
    def __init__(self, driver):
        self.driver=driver

    dropdown="dropdownMenuButton"
    dropdown_menu="//div[@class='dropdown-menu show']"
    dropdown_menu_items="//div[@class='dropdown-menu show']/a"


    # Interact with elements - dropdown
    def click_dropdown(self):
        self.driver.find_element(By.ID, self.dropdown).click()

        # wait for dropdown to be viisble
        WebDriverWait(self.driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, self.dropdown_menu)))

    # get all elemnets from dropdown
    def get_all_items(self):
        items=[]
        dropdown_items=self.driver.find_elements(By.XPATH, self.dropdown_menu_items)
        for item in dropdown_items:
            items.append(item.text) # or use item.get_attribute('data_value')
        return items

    

