from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    USER_NAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")

    def login(self, username: str, password: str) -> "LoginPage":
        self.input_text(self.USER_NAME_INPUT, username)
        self.input_text(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)
        return self
