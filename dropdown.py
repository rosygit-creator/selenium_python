from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



# Initialize the WebDriver (replace with your WebDriver's path if not in PATH)
# Example for Chrome:
driver = webdriver.Chrome() 

# Example for Firefox (if GeckoDriver is in PATH):
# driver = webdriver.Firefox()

# Navigate to a website
driver.get("https://formy-project.herokuapp.com/dropdown")

# Interact with elements - dropdown

driver.find_element(By.ID, "dropdownMenuButton").click()

# wait for dropdown to be viisble

WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//div[@class='dropdown-menu show']"))
)

# get all elemnets from dropdown
items=[]
dropdown_items=driver.find_elements(By.XPATH, "//div[@class='dropdown-menu show']/a")
for item in dropdown_items:
    items.append(item.text) # or use item.get_attribute('data_value')
print(items)

if "Checkbox" in items:
    # print("true")
    assert "Checkbox" in items

# Close the browser
driver.quit()