from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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
submit_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")

# Скроллим вниз, чтобы кнопка была видна
driver.execute_script("window.scrollBy(0, 300);")

# Ждём пока станет кликабельной
WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))
)

# Кликаем через JS (иначе может не сработать)
driver.execute_script("arguments[0].click();", submit_button)

# 4. Проверяем поля с ошибками (подсвечены красным)
error_fields = driver.find_elements(By.CLASS_NAME, "alert-danger")
for field in error_fields:
    print("Поле с ошибкой:", field.get_attribute("name"))

driver.quit()