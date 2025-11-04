import os

from selenium import webdriver
from selenium.webdriver.common.by import By



# Initialize the WebDriver (replace with your WebDriver's path if not in PATH)
# Example for Chrome:
driver = webdriver.Chrome() 

# Example for Firefox (if GeckoDriver is in PATH):
# driver = webdriver.Firefox()

# Navigate to a website
driver.get("https://formy-project.herokuapp.com/fileupload")

file_upload_input=driver.find_element(By.ID, "file-upload-field")

choose_button=driver.find_element(By.CLASS_NAME, "//*[@class='input-group input-file']/span/button")
choose_button.click

file_to_upload = os.path.abspath("f1.txt") 
file_upload_input.send_keys(file_to_upload)



# Close the browser
driver.quit()