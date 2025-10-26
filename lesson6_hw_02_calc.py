from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

# 1. Устанавливаем время ожидания
delay_input = driver.find_element(By.ID, "delay")
delay_input.clear()
delay_input.send_keys("45")

# 2. Нажимаем кнопки
driver.find_element(By.XPATH, "//span[text()='7']").click()
driver.find_element(By.XPATH, "//span[text()='+']").click()
driver.find_element(By.XPATH, "//span[text()='8']").click()
driver.find_element(By.XPATH, "//span[text()='=']").click()

# 3. Ждем, пока появится результат
WebDriverWait(driver, 50).until(
    EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15")
)

result = driver.find_element(By.CLASS_NAME, "screen").text
print("Результат:", result)

driver.quit()