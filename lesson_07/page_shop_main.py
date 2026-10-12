from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AddPage:
    ADD_BACKPACK = (By.NAME, "add-to-cart-sauce-labs-backpack")
    ADD_BOLT_TSHIRT = (By.NAME, "add-to-cart-sauce-labs-bolt-t-shirt")
    ADD_ONESIE = (By.NAME, "add-to-cart-sauce-labs-onesie")

    CART_CONTAINER = (By.ID, "shopping_cart_container")

    def __init__(self, driver, wait_timeout=30):
        self.driver = driver
        self.wait = WebDriverWait(driver, wait_timeout)

    def add_backpack(self):
        btn = self.wait.until(EC.element_to_be_clickable(self.ADD_BACKPACK))
        btn.click()
        return self

    def add_bolt_tshirt(self):
        btn = self.wait.until(EC.element_to_be_clickable(self.ADD_BOLT_TSHIRT))
        btn.click()
        return self

    def add_onesie(self):
        btn = self.wait.until(EC.element_to_be_clickable(self.ADD_ONESIE))
        btn.click()
        return self

    def go_to_cart(self):
        cart_btn = self.wait.until(
            EC.element_to_be_clickable(self.CART_CONTAINER)
        )
        cart_btn.click()
        return self
