import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

path = Service("C:/Users/in04065/PycharmProjects/Selenium8Nov2025/drivers/chromedriver.exe")

#click on facebook using link text-->pass only partial text
driver = webdriver.Chrome(service=path)
driver.get("file:///C:/Users/in04065/PycharmProjects/Selenium8Nov2025/filej.html")
time.sleep(2)
driver.find_element(By.PARTIAL_LINK_TEXT,"book").click()
time.sleep(2)