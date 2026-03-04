import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

path = Service("C:/Users/in04065/PycharmProjects/Selenium8Nov2025/drivers/chromedriver.exe")
driver= webdriver.Chrome(service=path)

driver.get("https://www.stepcampus.in/playground")

driver.implicitly_wait(5)

#opening new tab
driver.find_element(By.XPATH,"//a[text()='Open Selenium Docs in New Tab']").click()

#finding address of child window and main window
allIds=driver.window_handles
print(allIds[0])
print(allIds[1])

#to change focus of selenium from main page to child window
driver.switch_to.window(allIds[1])

driver.find_element(By.XPATH,"//a[text()='About']").click()

time.sleep(5)

time.sleep(5)




