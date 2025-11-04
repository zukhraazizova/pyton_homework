from selenium.webdriver.common.by import By

class ProductsPage:
    def __init__(self, driver):
        self.driver = driver

    def add_item(self, name):
        self.driver.find_element(
            By.XPATH, f"//div[text()='{name}']/ancestor::div[@class='inventory_item']//button"
        ).click()

    def go_to_cart(self):
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()