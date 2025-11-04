from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Initialize the WebDriver (replace with your WebDriver's path if not in PATH)
# Example for Chrome:
driver = webdriver.Chrome() 

# Example for Firefox (if GeckoDriver is in PATH):
# driver = webdriver.Firefox()

# Navigate to a website
driver.get("https://formy-project.herokuapp.com/")

# Interact with elements - get all links

l1=[]
links=driver.find_elements(By.XPATH, "//div[@class='jumbotron-fluid']/li/a")
# links=driver.find_elements(By.TAG_NAME, "a")

for link in links:
    l1.append(link.get_attribute("href"))
print(l1)
links_count=len(l1)
print(f"links count {len(l1)}")

# Close the browser
driver.quit()