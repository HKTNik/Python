from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.cart_page import CartPage


class AddPage(BasePage):
    ADD_BACKPACK = (By.NAME, "add-to-cart-sauce-labs-backpack")
    ADD_BOLT_TSHIRT = (By.NAME, "add-to-cart-sauce-labs-bolt-t-shirt")
    ADD_ONESIE = (By.NAME, "add-to-cart-sauce-labs-onesie")

    CART_CONTAINER = (By.ID, "shopping_cart_container")

    def add_backpack(self) -> "AddPage":
        """Добавляет рюкзак. Использует ожидание кликабельного элемента."""
        btn = self.wait.until(EC.element_to_be_clickable(self.ADD_BACKPACK))
        btn.click()
        return self

    def add_bolt_tshirt(self) -> "AddPage":
        """Добавляет футболку."""
        btn = self.wait.until(EC.element_to_be_clickable(self.ADD_BOLT_TSHIRT))
        btn.click()
        return self

    def add_onesie(self) -> "AddPage":
        """Добавляет комбинезон."""
        btn = self.wait.until(EC.element_to_be_clickable(self.ADD_ONESIE))
        btn.click()
        return self

    def go_to_cart(self) -> CartPage:
        """
        Переходит в корзину и ждёт появления хотя бы одного товара.
        Это подтверждает, что переход успешен И товары отобразились.
        """
        # 1. Ждём кнопку корзины и кликаем
        cart_btn = self.wait.until(
            EC.element_to_be_clickable(self.CART_CONTAINER)
        )
        cart_btn.click()

        # 2. Ждём появления первого товара в корзине.
        cart_items_locator = (By.CLASS_NAME, "cart_item")

        try:
            self.wait.until(
                EC.visibility_of_element_located(cart_items_locator)
            )
        except Exception as e:
            # Делаем скриншот, если не дождались товаров
            self.driver.save_screenshot("failed_cart_transition.png")
            raise TimeoutError(
                "Не удалось дождаться отображения товаров в корзине. "
                "Переход мог не сработать или страница не отрендерилась."
            ) from e

        return CartPage(self.driver, self.wait._timeout)
