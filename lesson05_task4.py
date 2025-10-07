from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import warnings

warnings.filterwarnings("ignore")


driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/login")
time.sleep(2) 

driver.find_element(By.ID, "username").send_keys("tomsmith")
time.sleep(1) 

driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
time.sleep(1)

driver.find_element(By.CSS_SELECTOR, "button.radius").click()
time.sleep(2)  

message = driver.find_element(By.ID, "flash").text
print("Результат авторизации:", message)

time.sleep(3)
driver.quit()