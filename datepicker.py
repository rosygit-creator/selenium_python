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
driver.get("https://formy-project.herokuapp.com/datepicker")

# Interact with elements - datepicker

driver.find_element(By.ID, "datepicker").click()

# wait for datepicker to be viisble

WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//*[contains(@class, 'datepicker-dropdown')]"))
)


driver.find_element(By.XPATH,"//*[@class='datepicker-days']/table/tbody/tr/td[@class='today day']").click()
# selected date is not updated in DOM but in Ui so cannot validate it

# verify date

# get all rows 
# rows=driver.find_elements(By.XPATH,"//*[@class='datepicker-days']/table/tbody/tr")
# print(f"rows is {rows}")

# # get column count
# for row in rows:
#     cols=row.find_element(By.TAG_NAME, "td")
# print(f"cols is {cols}")






# Close the browser
driver.quit()