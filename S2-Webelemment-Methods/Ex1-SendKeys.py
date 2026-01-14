import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

path = Service("C:/Users/in04065/PycharmProjects/Selenium8Nov2025/drivers/chromedriver.exe")
driver = webdriver.Chrome(service=path)
driver.get("https://www.facebook.com/")

#both same
#driver.find_element(By.XPATH,"//input[@name='email']").send_keys("abc")
#storing web element
UN=driver.find_element(By.XPATH,"//input[@name='email']")
UN.send_keys("abc")

time.sleep(2)