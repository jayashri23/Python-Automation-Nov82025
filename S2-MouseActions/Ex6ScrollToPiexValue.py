import time


from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

path = Service("C:/Users/in04065/PycharmProjects/Selenium8Nov2025/drivers/chromedriver.exe")
driver= webdriver.Chrome(service=path)

driver.get("https://www.facebook.com/")

driver.maximize_window()
time.sleep(2)

act=ActionChains(driver)

#to scroll Down (start value 0 ,end value +val)
act.scroll_by_amount(0,300).perform()
time.sleep(2)

#to scroll up (start value 0 ,end value -val)
act.scroll_by_amount(0,-200).perform()
time.sleep(2)

