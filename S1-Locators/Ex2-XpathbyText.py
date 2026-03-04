import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

path = Service("C:/Users/in04065/PycharmProjects/Selenium8Nov2025/drivers/chromedriver.exe")

driver = webdriver.Chrome(service=path)
driver.get("https://www.facebook.com/")
#2.Xpath by text=//tag name[text()=text]

#login button click
driver.find_element(By.XPATH,"//button[text()='Log in']" ).click()
#click on forgot passed button
driver.find_element(By.XPATH, "//a[text()='Forgotten password?']").click()
time.sleep(2)
