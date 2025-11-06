class LoginPage:
    """
    Класс для страницы логина
    """

    def __init__(self, driver):
        """
        Инициализация страницы

        :param driver: WebDriver экземпляр
        """
        self.driver = driver

    def enter_username(self, username: str) -> None:
        """
        Ввод имени пользователя

        :param username: str - имя пользователя
        :return: None
        """
        # Код для ввода имени пользователя
        pass

    def enter_password(self, password: str) -> None:
        """
        Ввод пароля

        :param password: str - пароль пользователя
        :return: None
        """
        pass

    def click_login(self) -> bool:
        """
        Нажатие кнопки входа

        :return: bool - True если вход успешен, иначе False
        """
        pass