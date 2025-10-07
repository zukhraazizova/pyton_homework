from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()

driver.get("https://the-internet.herokuapp.com/inputs")

input_field = driver.find_element(By.TAG_NAME, "input")

input_field.send_keys("Тестовое значение")
time.sleep(1)

input_field.clear()
time.sleep(1)

input_field.send_keys("12345")
time.sleep(2)


driver.quit()