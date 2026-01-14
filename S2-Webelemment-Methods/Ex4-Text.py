import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

path = Service("C:/Users/in04065/PycharmProjects/Selenium8Nov2025/drivers/chromedriver.exe")
driver = webdriver.Chrome(service=path)
driver.get("https://www.facebook.com/")

#get text from webpage
textValue=driver.find_element(By.XPATH, "//a[contains(text(),'Forgotten')]").text
print(textValue)