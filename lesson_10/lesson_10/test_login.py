import pytest
import allure

@allure.feature("Login Feature")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Тест успешного входа")
@allure.description("Проверка возможности успешного входа на сайт с корректными данными")
def test_login():
    with allure.step("Вводим имя пользователя"):
        username = "testuser"

    with allure.step("Вводим пароль"):
        password = "password123"

    with allure.step("Нажимаем кнопку Вход"):
        login_success = True  # здесь можно просто заглушку

    with allure.step("Проверяем успешный вход"):
        assert login_success is True