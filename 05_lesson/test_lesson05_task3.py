from selenium import webdriver
from selenium.webdriver.common.by import By


def test_multiple_elements():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.qa-territory.online/links/10")
    driver.maximize_window()
    links = driver.find_elements(By.TAG_NAME, "a")
    assert len(links) == 9
    for link in links:
        assert link.is_displayed(), "Ссылка не отображается на странице"
    first_link_text = links[0].text
    assert "1" in first_link_text, "текст первой ссылки не содержит '1'"
    driver.quit()
