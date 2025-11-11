import allure
from pages.login_page import LoginPage


@allure.title("Проверка успешного логина")
@allure.feature("Авторизация")
@allure.severity(allure.severity_level.CRITICAL)
def test_login(driver):
    driver.get("https://example.com/login")
    page = LoginPage(driver)

    with allure.step("Заполняем поля логина"):
        page.enter_username("testuser")
        page.enter_password("password123")

    with allure.step("Жмём кнопку логина"):
        page.click_login()

    with allure.step("Проверяем успех"):
        assert page.is_login_successful() is True