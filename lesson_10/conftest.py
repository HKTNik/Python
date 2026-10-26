import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="function")
def driver():
    """Фикстура для создания и закрытия браузера."""
    options = Options()

    # Разворачивает окно на весь экран при запуске
    options.add_argument("--start-maximized")

    # Создаем экземпляр драйвера с этими настройками
    browser = webdriver.Chrome(options=options)

    yield browser

    # После теста браузер закроется
    browser.quit()
