from selenium import webdriver
from selenium.webdriver.common.by import By


# Initialize the WebDriver (replace with your WebDriver's path if not in PATH)
# Example for Chrome:
driver = webdriver.Chrome() 

# Example for Firefox (if GeckoDriver is in PATH):
# driver = webdriver.Firefox()

# Navigate to a website
driver.get("https://the-internet.herokuapp.com/tables")

# get rows in table- Method 1

# rows=driver.find_elements(By.XPATH , "//*[@id='table1']/tbody/tr")
# print(len(rows))
# # get cols
# cols=driver.find_elements(By.XPATH, "//*[@id='table1']/tbody/tr[1]/td")
# print(cols)


# another way to do it - Method 2
# find table handle
table=driver.find_element(By.ID , "table1")
rows=table.find_elements(By.TAG_NAME, "tr")
# print(len(rows)) # here row 1 with be heading


# sum Due colum - col index 3
sum=0
for i in range (1, len(rows)): # index 0 is the heading
    # get cols
    cell=rows[i].find_elements(By.TAG_NAME, "td")
    # print(len(cell))
    temp_amount=cell[3].text
    due_amount=temp_amount.replace('$','')
    # print(f"due_amount {due_amount}")
    sum=sum+float(due_amount)

assert sum==251.00

# Close the browser
driver.quit()