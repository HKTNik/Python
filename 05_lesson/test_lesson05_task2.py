from selenium import webdriver
from selenium.webdriver.common.by import By


def test_form_submission():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.qa-territory.online/forms/post")
    input_field = driver.find_element(By.NAME, "custname")
    input_field.send_keys("Nikita")
    button_submit = driver.find_element(
        By.XPATH, "//button[contains(text(), 'Submit')]")
    button_submit.click()
    assert driver.current_url != (
        "https://httpbin.qa-territory.online/forms/post")
    driver.quit()
