import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

path = Service("C:/Users/in04065/PycharmProjects/Selenium8Nov2025/drivers/chromedriver.exe")
driver= webdriver.Chrome(service=path)

driver.get("https://demo.guru99.com/test/simple_context_menu.html")
driver.maximize_window()

actions = ActionChains(driver)

double=driver.find_element(By.XPATH,"//button[text()='Double-Click Me To See Alert']")
time.sleep(2)

actions.double_click(double).perform()
time.sleep(2)


