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

driver.find_element(By.ID, "new-tab-button").click
# print("new window")

# get all window handles
all_windows=driver.window_handles

for h in all_windows:
    if h!=original_handle:
        driver.switch_to.window(h)
  
assert driver.title=="Formy"        
    
# text_form=driver.find_element(By.CLASS_NAME, "//*[@class='display-3']")
# print(text_form.text)

# Close the browser
driver.quit()