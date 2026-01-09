import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

path = Service("C:/Users/in04065/PycharmProjects/Selenium8Nov2025/drivers/chromedriver.exe")

driver = webdriver.Chrome(service=path)
driver.get("https://www.facebook.com/")

##->Text        //tag[contains(text(),'partial text value')]

#click on forgot password
driver.find_element(By.XPATH, "//a[contains(text(),'Forgotten password?')]").click()
time.sleep(2)
driver.find_element(By.XPATH, "//a[contains(text(),'Create new account')]").click()
time.sleep(2)