import email
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

path = Service("C:/Users/in04065/PycharmProjects/Selenium8Nov2025/drivers/chromedriver.exe")

driver = webdriver.Chrome(service=path)
driver.get("https://www.facebook.com/")
#----4 type of XPath formula---------
#1.driver.find_element(locator type")
#driver.find _element(By.XPATH,"XPATH Expression")
driver.find_element(By.XPATH, "//input[@name='email']").send_keys("jsjankar23@gmail.com")
driver.find_element(By.XPATH, "//input[@type='password']").send_keys("jayashri@23")
driver.find_element(By.XPATH,"//button[@name='login']").click()
time.sleep(50)

#Control +shift +i   ->to open banking site inspect