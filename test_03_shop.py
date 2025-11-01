from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")

# Авторизация
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

# Добавляем товары
driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()

# Корзина и оформление
driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
driver.find_element(By.ID, "checkout").click()

# Заполняем форму
driver.find_element(By.ID, "first-name").send_keys("Иван")
driver.find_element(By.ID, "last-name").send_keys("Петров")
driver.find_element(By.ID, "postal-code").send_keys("1856")
driver.find_element(By.ID, "continue").click()

# Проверяем сумму
total = driver.find_element(By.CLASS_NAME, "summary_total_label").text
assert total == "Total: $58.29", "Итоговая сумма неверная!"

driver.quit()