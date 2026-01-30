import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

path = Service("C:/Users/in04065/PycharmProjects/Selenium8Nov2025/drivers/chromedriver.exe")
driver= webdriver.Chrome(service=path)

driver.get("https://demoqa.com/browser-windows")
driver.switch_to.window(driver.window_handles[0])

driver.implicitly_wait(10)

#click on new tab from main page
driver.find_element(By.XPATH,"//button[text()='New Tab']").click()
time.sleep(2)

#get child window ID/Address
allIds=driver.window_handles
#print(allIds[0])
#print(allIds[1])

#switch  from main page to child window
driver.switch_to.window(allIds[1])

#click on about link from child window
print(driver.title)

#to change focus of selenium from child window to main window

driver.switch_to.window(allIds[0])

#click on contact button on main page
driver.find_element(By.XPATH,"//button[text()='New Window']").click()
time.sleep(10)
