from selenium.webdriver.common.by import By
from .base_page import BasePage


class CartPage(BasePage):
    """Страница корзины."""

    CHECKOUT_BUTTON = (By.ID, "checkout")
    ITEM_COUNT_LOCATOR = (By.CLASS_NAME, "cart_item")

    def click_checkout(self) -> None:
        """
        Нажимает кнопку оформления заказа.
        :return: None
        """
        self.click(self.CHECKOUT_BUTTON)

    def get_items_count(self) -> int:
        """
        Возвращает количество товаров в корзине.
        :return: Количество элементов (тип: int)
        """
        elements = self.driver.find_elements(*self.ITEM_COUNT_LOCATOR)
        return len(elements)
