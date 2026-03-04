"""
Popup is small or separate window will be displayed when we perform action on any component
 present on webpage Types of popup
 Types of popup:

 1.Hidden division popup-
 features-colourful popup
 no need to switch
 we can inspect element present on popup

"""
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

path = Service("C:/Users/in04065/PycharmProjects/Selenium8Nov2025/drivers/chromedriver.exe")
driver= webdriver.Chrome(service=path)

driver.get("https://www.mobikwik.com/")
time.sleep(2)

driver.find_element(By.XPATH,"//span[text()='Login']").click()

driver.find_element(By.XPATH,"//input[@id='email']").send_keys("98765434")
time.sleep(2)

time.sleep(2)
