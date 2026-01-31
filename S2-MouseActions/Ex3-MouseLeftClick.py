import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

path = Service("C:/Users/in04065/PycharmProjects/Selenium8Nov2025/drivers/chromedriver.exe")
driver= webdriver.Chrome(service=path)

driver.get("https://www.flipkart.com/")
driver.maximize_window()

actions = ActionChains(driver)

cart=driver.find_element(By.XPATH,"//a[text()='Cart']")
time.sleep(2)

#Approvach 1
#actions.move_to_element(cart).click().perform()


#Approach 2
#actions.click(cart).perform()

#Approach 3
actions.move_to_element(cart).perform()
actions.click(cart).perform()
time.sleep(2)



