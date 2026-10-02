from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_session_storage_auth():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    cookie_user1 = {
        "name": "SESSION",
        "value": "YjNkMmVjZTUtMDBlOS00ZTA3LWJhMGEtNzVmMWExZjJjNGUx",
        "domain": "gitflic.ru"
    }
    cookie_user2 = {
        "name": "SESSION",
        "value": "ODVjMDc5NDktNTc1ZC00ZDkxLWE1NDctMDQ4Y2RmZDBhYzkw",
        "domain": "gitflic.ru",
    }

    user1_name = "username1"
    user2_name = "username2"

    driver.get("https://gitflic.ru/")
    driver.add_cookie(cookie_user1)
    driver.refresh()
    driver.get(f"https://gitflic.ru/user/{user1_name}")
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
    url_user1 = driver.current_url
    driver.delete_all_cookies()
    driver.get("https://gitflic.ru/")
    driver.add_cookie(cookie_user2)
    driver.refresh()
    driver.get(f"https://gitflic.ru/user/{user2_name}")
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
    url_user2 = driver.current_url
    assert url_user1 != url_user2, (
        f"URL одинаковы: {url_user1} == {url_user2}"
    )

    driver.quit()
