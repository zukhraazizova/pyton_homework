from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# 1. Открываем браузер
driver = webdriver.Chrome()
driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

# 2. Заполняем поля
driver.find_element(By.NAME, "first-name").send_keys("Иван")
driver.find_element(By.NAME, "last-name").send_keys("Петров")
driver.find_element(By.NAME, "address").send_keys("Ленинградский 53-3")
driver.find_element(By.NAME, "e-mail").send_keys("test@test.ru")
driver.find_element(By.NAME, "phone").send_keys("89215635522")
driver.find_element(By.NAME, "zip-code").send_keys("1856")
driver.find_element(By.NAME, "city").send_keys("Москва")
driver.find_element(By.NAME, "country").send_keys("Россия")
driver.find_element(By.NAME, "job-position").send_keys("QA")
driver.find_element(By.NAME, "company").send_keys("SkyPro")

# 3. Нажимаем кнопку
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

# 4. Проверяем поля с ошибками
error_fields = driver.find_elements(By.CLASS_NAME, "alert-danger")
for field in error_fields:
    print("Поле с ошибкой:", field.get_attribute("name"))

driver.quit()