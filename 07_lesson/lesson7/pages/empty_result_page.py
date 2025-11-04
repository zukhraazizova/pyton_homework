from selenium.webdriver.common.by import By

class EmptyResultPage:
    def __init__(self, driver):
        self.driver = driver

    def search(self, text):
        self.driver.find_element(By.ID, "user-name").send_keys(text)
        self.driver.find_element(By.ID, "login-button").click()

    def get_error(self):
        return self.driver.find_element(By.CSS_SELECTOR, "h3").text