from selenium import webdriver
from selenium.webdriver.common.by import By


# Initialize the WebDriver (replace with your WebDriver's path if not in PATH)
# Example for Chrome:
driver = webdriver.Chrome() 

# Example for Firefox (if GeckoDriver is in PATH):
# driver = webdriver.Firefox()

# Navigate to a website
driver.get("https://formy-project.herokuapp.com/switch-window")

original_handle=driver.current_window_handle
# Interact with elements - open new window

driver.find_element(By.ID, "alert-button").click

# switch to alert
alert=driver.switch_to.alert
# print(alert.text)

assert alert.text=="This is a test alert!"        
alert.accept

# verify alert is accepted
text_form=driver.find_element(By.ID, "new-tab-button")
print(text_form.text)

# Close the browser
driver.quit()