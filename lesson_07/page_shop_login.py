from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    USER_NAME_INPUT = (By.CSS_SELECTOR, "#user-name")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "#password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "#login-button")

    def __init__(self, driver, wait_timeout=30):
        self.driver = driver
        self.wait = WebDriverWait(driver, wait_timeout)

    def login(self, username: str, password: str):
        username_field = self.wait.until(
            EC.element_to_be_clickable(self.USER_NAME_INPUT)
        )
        username_field.clear()
        username_field.send_keys(username)

        password_field = self.wait.until(
            EC.element_to_be_clickable(self.PASSWORD_INPUT)
        )
        password_field.clear()
        password_field.send_keys(password)

        login_btn = self.wait.until(
            EC.element_to_be_clickable(self.LOGIN_BUTTON)
        )
        login_btn.click()
