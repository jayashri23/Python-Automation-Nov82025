import time

#to take screenshot of full page
#driver.save_screenshot("folder path\filename.png")
#In given path screen shot stored after execution

from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

path = Service("C:/Users/in04065/PycharmProjects/Selenium8Nov2025/drivers/chromedriver.exe")
driver= webdriver.Chrome(service=path)

driver.get("https://www.instagram.com/accounts/login/?hl=en")

driver.save_screenshot("C:\\Users\\in04065\\PycharmProjects\\Selenium8Nov2025\\screenshots\\abc2.png")

time.sleep(5)
