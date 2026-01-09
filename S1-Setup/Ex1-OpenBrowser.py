import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

path = Service("C:/Users/in04065/PycharmProjects/Selenium8Nov2025/drivers/chromedriver.exe")
driver = webdriver.Chrome(service=path)
print("---Webdriver opened----")

driver.get("http://google.com")
driver.get("https://www.gmail.com")
print("---Webdriver closed----")
driver.quit()
driver.maximize_window()
time.sleep(3)

#driver.close()     #to close current tab /window
#driver.quit()   -->to close all tab/window

#driver.minimize_window()

#driver.forward()
driver.refresh()
time.sleep(5)#wait for specific time

driver.back()
time.sleep(5)
