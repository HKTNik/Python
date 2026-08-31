import time
from selenium import webdriver


driver = webdriver.Chrome()
driver.get("https://www.Championat.ru")


time.sleep(5)

driver.quit()
