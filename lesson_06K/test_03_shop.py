from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_shop():
    driver = webdriver.Firefox()
    driver.maximize_window()
    options = Options()
    service = Service()
    driver = webdriver.Firefox(service=service, options=options)

    wait = WebDriverWait(driver, 20)

    try:
        driver.get("http://www.saucedemo.com/")
        user_name = wait.until(EC.element_to_be_clickable((
            By.CSS_SELECTOR, "#user-name")))
        user_name.send_keys("standard_user")

        password = driver.find_element(By.CSS_SELECTOR, "#password")
        password.send_keys("secret_sauce")

        login_button = driver.find_element(By.CSS_SELECTOR, "#login-button")
        login_button.click()

        add_backpack = wait.until(EC.element_to_be_clickable((
            By.NAME, "add-to-cart-sauce-labs-backpack")))
        add_backpack.click()

        add_shirt = wait.until(EC.element_to_be_clickable((
            By.NAME, "add-to-cart-sauce-labs-bolt-t-shirt")))
        add_shirt.click()

        add_onesie = wait.until(EC.element_to_be_clickable((
            By.NAME, "add-to-cart-sauce-labs-onesie")))
        add_onesie.click()

        cart_container = wait.until(EC.element_to_be_clickable((
            By.ID, "shopping_cart_container")))
        cart_container.click()

        checkout_button = wait.until(EC.element_to_be_clickable((
            By.ID, "checkout")))
        checkout_button.click()

        first_name = wait.until(EC.element_to_be_clickable((
            By.ID, "first-name")))
        first_name.send_keys("Nikita")

        last_name = driver.find_element(By.ID, "last-name")
        last_name.send_keys("Triasunov")

        postal_code = driver.find_element(By.ID, "postal-code")
        postal_code.send_keys("423490")

        continue_button = wait.until(EC.element_to_be_clickable((
            By.ID, "continue")))
        continue_button.click()

        total_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((
                By.CLASS_NAME, "summary_total_label"))
        )
        total_text = total_element.text
        expected_total = "Total: $58.29"
        assert total_text == expected_total
        f"Ожидалось: {expected_total}, Получено: {total_text}"

    finally:
        driver.quit()
