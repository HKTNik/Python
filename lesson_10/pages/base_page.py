from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver, wait_timeout=15):
        self.driver = driver
        self.wait = WebDriverWait(driver, wait_timeout)

    def _find_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def click(self, locator):
        element = self._find_element(locator)
        element.click()
        return self

    def input_text(self, locator, text: str):
        element = self._find_element(locator)
        element.clear()
        element.send_keys(text)
        return self
