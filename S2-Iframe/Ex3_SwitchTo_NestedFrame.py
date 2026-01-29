import time

from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

path = Service("C:/Users/in04065/PycharmProjects/Selenium8Nov2025/drivers/chromedriver.exe")
driver= webdriver.Chrome(service=path)

driver.get("https://autotestsandbox.com/examples/nested-iframes")

time.sleep(2)

#switch to outer frame

driver.switch_to.frame(driver.find_element(By.XPATH,"//iframe[@title='Outer nested frame']"))

#switch inner frame
driver.switch_to.frame(driver.find_element(By.XPATH,"//iframe[@title='Inner']"))

#get text from nested frame

value=driver.find_element(By.XPATH,"//p[text()='Inner iframe content']").text

print(value)

