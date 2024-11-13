from sys import executable

from selenium import webdriver

driver_path = "/Users/tallevi/chromedriver/chromedriver"

driver = webdriver.Chrome(service=webdriver.chrome.service.Service(driver_path))

driver.get("https://www.google.com")

driver.quit()
