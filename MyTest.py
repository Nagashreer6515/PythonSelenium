from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()
driver.implicitly_wait(5)
driver.find_element(By.NAME, "username").send_keys("Admin")
driver.find_element(By.NAME, "password").send_keys("admin123")
driver.find_element(By.XPATH,"//button[@type='submit']").click()

act_title= driver.title
print(driver.title)
exp_title = "OrangeHRM"

if act_title == exp_title:
    print("Pass")
else:
    print("Fail")

