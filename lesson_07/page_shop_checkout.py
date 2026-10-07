from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:
    FIRST_NAME_INPUT = (By.ID, "first-name")
    LAST_NAME_INPUT = (By.ID, "last-name")
    POSTAL_CODE_INPUT = (By.ID, "postal-code")

    CONTINUE_BUTTON = (By.ID, "continue")

    TOTAL_LABEL = (By.CLASS_NAME, "summary_total_label")

    def __init__(self, driver, wait_timeout=30):
        self.driver = driver
        self.wait = WebDriverWait(driver, wait_timeout)

    def fill_shipping_info(
        self,
        first_name: str,
        last_name: str,
        postal_code: str
    ):
        first_name_field = self.wait.until(
            EC.element_to_be_clickable(self.FIRST_NAME_INPUT)
        )
        first_name_field.clear()
        first_name_field.send_keys(first_name)

        last_name_field = self.wait.until(
            EC.element_to_be_clickable(self.LAST_NAME_INPUT)
        )
        last_name_field.clear()
        last_name_field.send_keys(last_name)

        postal_code_field = self.wait.until(
            EC.element_to_be_clickable(self.POSTAL_CODE_INPUT)
        )
        postal_code_field.clear()
        postal_code_field.send_keys(postal_code)
        return self

    def click_continue(self):
        continue_btn = self.wait.until(
            EC.element_to_be_clickable(self.CONTINUE_BUTTON)
        )
        continue_btn.click()
        return self

    def get_total_text(self):
        total_element = self.wait.until(
            EC.presence_of_element_located(self.TOTAL_LABEL)
        )
        return total_element.text.strip()
