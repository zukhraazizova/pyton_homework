from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/ajax")

blue_button = driver.find_element(By.ID, "ajaxButton")
blue_button.click()

WebDriverWait(driver, 20).until(
    EC.text_to_be_present_in_element(
        (By.CLASS_NAME, "bg-success"),
        "Data loaded with AJAX get request."
    )
)

success_text = driver.find_element(By.CLASS_NAME, "bg-success").text
print(success_text)

driver.quit()