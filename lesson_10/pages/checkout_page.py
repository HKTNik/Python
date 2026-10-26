from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage


class CheckoutPage(BasePage):
    """Страница оформления заказа (Checkout) в Sauce Labs."""

    FIRST_NAME_INPUT = (By.ID, "first-name")
    LAST_NAME_INPUT = (By.ID, "last-name")
    POSTAL_CODE_INPUT = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    TOTAL_LABEL = (By.CLASS_NAME, "summary_total_label")

    def fill_shipping_info(
        self,
        first_name: str,
        last_name: str,
        postal_code: str
    ) -> "CheckoutPage":
        """
        Заполняет форму доставки данными пользователя.
        :param first_name: Имя (тип: str)
        :param last_name: Фамилия (тип: str)
        :param postal_code: Почтовый индекс (тип: str)
        :return: Текущий экземпляр страницы (тип: CheckoutPage)
        """
        self.input_text(self.FIRST_NAME_INPUT, first_name)
        self.input_text(self.LAST_NAME_INPUT, last_name)
        self.input_text(self.POSTAL_CODE_INPUT, postal_code)
        return self

    def click_continue(self) -> None:
        """
        Нажимает кнопку продолжения оформления.
        :return: None
        """
        self.click(self.CONTINUE_BUTTON)

    def get_total_text(self) -> str:
        """
        Получает текст итоговой суммы заказа.
        :return: Текст суммы (например, "Total: $58.29") (тип: str)
        """
        element = self.wait.until(
            EC.presence_of_element_located(self.TOTAL_LABEL)
        )
        return element.text.strip()
