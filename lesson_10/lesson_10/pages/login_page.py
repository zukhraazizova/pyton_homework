from selenium.webdriver.common.by import By
import allure
from selenium.common.exceptions import NoSuchElementException


class LoginPage:

    USERNAME_INPUT = (By.ID, "username")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BTN = (By.ID, "login-button")
    SUCCESS_LABEL = (By.ID, "success")

    def __init__(self, driver):
        """
        :param driver: WebDriver instance
        """
        self.driver = driver

    @allure.step("Ввод имени пользователя '{username}'")
    def enter_username(self, username):
        self.driver.find_element(*self.USERNAME_INPUT).send_keys(username)

    @allure.step("Ввод пароля '{password}'")
    def enter_password(self, password):
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)

    @allure.step("Нажатие кнопки логина")
    def click_login(self):
        self.driver.find_element(*self.LOGIN_BTN).click()

    @allure.step("Проверка успешного входа")
    def is_login_successful(self):
        try:
            self.driver.find_element(*self.SUCCESS_LABEL)
            return True
        except NoSuchElementException:
            return False