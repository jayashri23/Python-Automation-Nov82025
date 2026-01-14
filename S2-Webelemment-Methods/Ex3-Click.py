import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

path = Service("C:/Users/in04065/PycharmProjects/Selenium8Nov2025/drivers/chromedriver.exe")
driver = webdriver.Chrome(service=path)
driver.get("https://www.facebook.com/r.php?entry_point=login")

#click on female radio button

driver.find_element(By.XPATH,"//input[@value='1']").click()
time.sleep(2)