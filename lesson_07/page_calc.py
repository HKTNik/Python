from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SlowCalculatorPage:

    DELAY_INPUT = (By.CSS_SELECTOR, "#delay")
    SCREEN = (By.CLASS_NAME, "screen")

    BTN_7 = (By.XPATH, '//*[@id="calculator"]/div[2]/span[1]')
    BTN_PLUS = (By.XPATH, '//*[@id="calculator"]/div[2]/span[4]')
    BTN_8 = (By.XPATH, '//*[@id="calculator"]/div[2]/span[2]')
    BTN_EQUALS = (By.XPATH, '//*[@id="calculator"]/div[2]/span[15]')

    def __init__(self, driver, wait_timeout=90):
        self.driver = driver
        self.wait = WebDriverWait(driver, wait_timeout)

    def set_delay(self, value: str):
        element = self.wait.until(
            EC.presence_of_element_located(self.DELAY_INPUT)
        )
        element.clear()
        element.send_keys(value)
        return self

    def click_7(self):
        btn = self.wait.until(
            EC.element_to_be_clickable(self.BTN_7)
        )
        btn.click()
        return self

    def click_plus(self):
        btn = self.wait.until(
            EC.element_to_be_clickable(self.BTN_PLUS)
        )
        btn.click()
        return self

    def click_8(self):
        btn = self.wait.until(
            EC.element_to_be_clickable(self.BTN_8)
        )
        btn.click()
        return self

    def click_equals(self):
        btn = self.wait.until(
            EC.element_to_be_clickable(self.BTN_EQUALS)
        )
        self.driver.execute_script("arguments[0].click();", btn)
        return self

    def wait_for_result(self, expected_text: str):
        self.wait.until(
            EC.text_to_be_present_in_element(self.SCREEN, expected_text)
        )
        return self

    def get_result_text(self) -> str:
        element = self.wait.until(
            EC.visibility_of_element_located(self.SCREEN)
        )
        return element.text.strip()
