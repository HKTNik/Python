from selenium import webdriver
from page_calc import SlowCalculatorPage


def test_calculator():
    driver = webdriver.Chrome()
    page = SlowCalculatorPage(driver)

    driver.maximize_window()
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
    )

    page.set_delay("45")

    page.click_7() .click_plus() .click_8() .click_equals()
    page.wait_for_result("15")
    result = page.get_result_text()
    assert result == "15", f"Ошибка: ожидалось '15', но получено '{result}'"

    driver.quit()
