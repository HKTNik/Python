from selenium import webdriver
from selenium.webdriver.common.by import By


def test_navigation():
    driver = webdriver.Chrome()
    base_url = "https://httpbin.qa-territory.online"
    driver.get(base_url)
    button = driver.find_element(By.LINK_TEXT, "HTML Form")
    button.click()
    assert driver.current_url == f"{base_url}/forms/post"
    driver.back()
    assert driver.current_url in [base_url, f"{base_url}/"]
    driver.quit()
