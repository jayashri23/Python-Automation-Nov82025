import time

#to take screenshot of full page
#driver.save_screenshot("folder path\filename.png")
#In given path screenshot stored after execution

from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

path = Service("C:/Users/in04065/PycharmProjects/Selenium8Nov2025/drivers/chromedriver.exe")
driver= webdriver.Chrome(service=path)

driver.get("https://www.facebook.com/")

driver.find_element(By.XPATH,"//img[@alt='Facebook']").screenshot("C:\\Users\\in04065\\PycharmProjects\\Selenium8Nov2025\\screenshots\\abc3.png")