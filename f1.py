from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Initialize the WebDriver (replace with your WebDriver's path if not in PATH)
# Example for Chrome:
driver = webdriver.Chrome() 

# Example for Firefox (if GeckoDriver is in PATH):
# driver = webdriver.Firefox()

# Navigate to a website
driver.get("https://www.google.com")

# Interact with elements (example: search for a term)
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Selenium Python")
search_box.send_keys(Keys.RETURN)

# Perform other actions like clicking buttons, extracting text, etc.

# Close the browser
driver.quit()