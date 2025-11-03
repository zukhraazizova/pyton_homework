import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_form():
    driver = webdriver.Safari()
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    # Заполняем поля
    driver.find_element(By.NAME, "first-name").send_keys("Иван")
    driver.find_element(By.NAME, "last-name").send_keys("Петров")
    driver.find_element(By.NAME, "address").send_keys("Ленина, 55-3")
    driver.find_element(By.NAME, "e-mail").send_keys("test@skypro.com")
    driver.find_element(By.NAME, "phone").send_keys("+798589999878")
    # zip-code — оставляем пустым
    driver.find_element(By.NAME, "city").send_keys("Москва")
    driver.find_element(By.NAME, "country").send_keys("Россия")
    driver.find_element(By.NAME, "job-position").send_keys("QA")
    driver.find_element(By.NAME, "company").send_keys("SkyPro")

    # Submit
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    # Проверка красного поля zip-code
    zip_code = driver.find_element(By.ID, "zip-code")
    assert "alert-danger" in zip_code.get_attribute("class"), "zip-code не подсвечен красным"

    # Проверка зеленых полей
    success_fields = [
        "first-name", "last-name", "address", "e-mail", "phone",
        "city", "country", "job-position", "company"
    ]

    for locator in success_fields:
        field = driver.find_element(By.ID, locator)
        assert "alert-success" in field.get_attribute("class")

    driver.quit()