import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

path = Service("C:/Users/in04065/PycharmProjects/Selenium8Nov2025/drivers/chromedriver.exe")
driver= webdriver.Chrome(service=path)

driver.get("https://flipkart.com/")
driver.maximize_window()

#step=1 identify dropdown
element=driver.find_element(By.XPATH,"//span[text()='Login']")

#step2:Create an object of ActionChain class with webdriver obj an
action=ActionChains(driver)

#step3:
action.move_to_element(element).perform()

time.sleep(2)

#click on orders link from  dropdown
driver.find_element(By.XPATH,"//li[text()='Orders']").click()

time.sleep(2)