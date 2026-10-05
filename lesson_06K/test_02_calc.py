from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_calculator():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 70)

    driver.maximize_window()
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    delay_input = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#delay")))
    delay_input.clear()
    delay_input.send_keys("45")

    btn_7 = wait.until(EC.element_to_be_clickable((
        By.XPATH, '//*[@id="calculator"]/div[2]/span[1]')))
    btn_7.click()

    btn_plus = wait.until(EC.element_to_be_clickable((
        By.XPATH, '//*[@id="calculator"]/div[2]/span[4]')))
    btn_plus.click()

    btn_8 = wait.until(EC.element_to_be_clickable((
        By.XPATH, '//*[@id="calculator"]/div[2]/span[2]')))
    btn_8.click()

    btn_equals = wait.until(EC.element_to_be_clickable((
        By.XPATH, '//*[@id="calculator"]/div[2]/span[15]')))
    driver.execute_script("arguments[0].click();", btn_equals)

    wait.until(EC.text_to_be_present_in_element((
        By.CLASS_NAME, "screen"), "15"))

    result_el = driver.find_element(By.CLASS_NAME, "screen")
    result = result_el.text.strip()

    assert result == "15"

    driver.quit()
