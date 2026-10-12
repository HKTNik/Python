from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from page_shop_login import LoginPage
from page_shop_cart import CartPage
from page_shop_main import AddPage
from page_shop_checkout import CheckoutPage


def test_shop():
    options = Options()
    service = Service()
    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")

    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")

    inventory_page = AddPage(driver)
    inventory_page.add_backpack().add_bolt_tshirt().add_onesie().go_to_cart()

    cart_page = CartPage(driver)
    cart_page.click_checkout()

    checkout_page = CheckoutPage(driver)
    checkout_page.fill_shipping_info(
        "Nikita", "Triasunov", "423490"
    ).click_continue()

    total_text = checkout_page.get_total_text()
    expected_total = "Total: $58.29"

    assert total_text == expected_total

    driver.quit()
