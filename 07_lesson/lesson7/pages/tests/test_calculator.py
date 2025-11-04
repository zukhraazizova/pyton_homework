from pages.calculator_page import CalculatorPage
from selenium import webdriver
import time

def test_calculator():
    driver = webdriver.Chrome()
    page = CalculatorPage(driver)

    page.open()
    page.set_delay(45)
    page.click_button("7")
    page.click_button("+")
    page.click_button("8")
    page.click_button("=")

    time.sleep(45)
    assert page.get_result() == "15"

    driver.quit()