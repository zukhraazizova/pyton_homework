from selenium.webdriver.common.by import By

class OverviewPage:
    def __init__(self, driver):
        self.driver = driver

    def read_total(self):
        total = self.driver.find_element(By.CSS_SELECTOR, ".summary_total_label").text
        return total.replace("Total: $", "")