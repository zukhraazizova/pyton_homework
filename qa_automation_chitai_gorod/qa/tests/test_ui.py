import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import constants  # Убедись, что в constants.py есть SEARCH_BOOK и BASE_URL

# ------------------------ Фикстура для драйвера ------------------------
@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()  # Selenium сам скачает драйвер
    driver.maximize_window()
    driver.get(constants.BASE_URL)
    yield driver
    driver.quit()

# ------------------------ Тесты ------------------------

@pytest.mark.ui
@allure.suite("UI тесты Лабиринта")
@allure.title("Открытие главной страницы")
@allure.description("Проверка, что главная страница открывается")
def test_open_main_page(driver):
    with allure.step("Открываем главную страницу"):
        driver.get(constants.BASE_URL)
    with allure.step("Проверяем заголовок страницы"):
        assert "Лабиринт" in driver.title

@pytest.mark.ui
@allure.suite("UI тесты Лабиринта")
@allure.title("Добавление товара в корзину")
def test_add_product_to_cart(driver):
    driver.find_element(By.ID, "search-field").send_keys(constants.SEARCH_BOOK)
    driver.find_element(By.CSS_SELECTOR, "span.b-header-b-search-e-btntxt").click()

    add_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "a.buy-link"))
    )
    add_button.click()

    with allure.step("Проверяем счетчик корзины"):
        cart_count = WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element(
                (By.CSS_SELECTOR, "span.basket-in-cart-a"), "1"
            )
        )
    count = driver.find_element(By.CSS_SELECTOR, "span.basket-in-cart-a").text
    assert count == "1"

@pytest.mark.ui
@allure.suite("UI тесты Лабиринта")
@allure.title("Удаление товара из корзины")
def test_deleted_product(driver):
    driver.find_element(By.ID, "search-field").send_keys(constants.SEARCH_BOOK)
    driver.find_element(By.CSS_SELECTOR, "span.b-header-b-search-e-btntxt").click()
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "a.buy-link"))
    ).click()
    driver.find_element(By.CSS_SELECTOR, "a.cart-icon-js").click()

    clear_cart = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Очистить корзину')]"))
    )
    clear_cart.click()

    WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, "span.basket-in-cart-a"), "0"
        )
    )
    count = driver.find_element(By.CSS_SELECTOR, "span.basket-in-cart-a").text
    assert count == "0"

@pytest.mark.ui
@allure.suite("UI тесты Лабиринта")
@allure.title("Восстановление удаленного товара")
def test_return_product_in_cart(driver):
    driver.find_element(By.ID, "search-field").send_keys(constants.SEARCH_BOOK)
    driver.find_element(By.CSS_SELECTOR, "span.b-header-b-search-e-btntxt").click()
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "a.buy-link"))
    ).click()
    driver.find_element(By.CSS_SELECTOR, "a.cart-icon-js").click()

    # Очистка корзины
    clear_cart = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Очистить корзину')]"))
    )
    clear_cart.click()

    # Восстановление
    restore = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Восстановить')]"))
    )
    restore.click()

    WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, "span.basket-in-cart-a"), "1"
        )
    )
    count = driver.find_element(By.CSS_SELECTOR, "span.basket-in-cart-a").text
    assert count == "1"

@pytest.mark.ui
@allure.suite("UI тесты Лабиринта")
@allure.title("Изменение количества товара в корзине")
def test_change_quantity(driver):
    driver.find_element(By.ID, "search-field").send_keys(constants.SEARCH_BOOK)
    driver.find_element(By.CSS_SELECTOR, "span.b-header-b-search-e-btntxt").click()
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "a.buy-link"))
    ).click()
    driver.find_element(By.CSS_SELECTOR, "a.cart-icon-js").click()

    quantity_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "input.cart-quantity"))
    )
    plus_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "img.img-plus"))
    )
    driver.execute_script("arguments[0].click();", plus_button)

    WebDriverWait(driver, 10).until(lambda d: quantity_input.get_attribute("value") == "2")
    assert quantity_input.get_attribute("value") == "2"