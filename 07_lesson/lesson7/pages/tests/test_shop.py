from selenium import webdriver
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.overview_page import OverviewPage


def test_shop():
    driver = webdriver.Chrome()
    login = LoginPage(driver)
    products = ProductsPage(driver)
    cart = CartPage(driver)
    checkout = CheckoutPage(driver)
    overview = OverviewPage(driver)

    login.open()
    login.login("standard_user", "secret_sauce")

    products.add_item("Sauce Labs Backpack")
    products.add_item("Sauce Labs Bolt T-Shirt")
    products.add_item("Sauce Labs Onesie")

    products.go_to_cart()
    cart.checkout()
    checkout.fill_form("Zuhra", "Azizova", "101000")

    total = overview.read_total()
    assert total == "58.29"

    driver.quit()