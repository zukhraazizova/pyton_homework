from selenium.webdriver.common.by import By

class CalculatorPage:
    URL = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.URL)

    def set_delay(self, value):
        field = self.driver.find_element(By.ID, "delay")
        field.clear()
        field.send_keys(value)

    def click_button(self, text):
        self.driver.find_element(By.XPATH, f"//span[text()='{text}']").click()

    def get_result(self):
        return self.driver.find_element(By.CSS_SELECTOR, "div.screen").text