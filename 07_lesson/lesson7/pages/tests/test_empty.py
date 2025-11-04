from selenium import webdriver
from pages.empty_result_page import EmptyResultPage

def test_empty_result():
    driver = webdriver.Chrome()
    page = EmptyResultPage(driver)

    driver.get("https://www.saucedemo.com/")
    page.search("")
    assert "Username is required" in page.get_error()

    driver.quit()