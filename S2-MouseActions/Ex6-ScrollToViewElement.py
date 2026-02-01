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
scrollTill=driver.find_element(By.XPATH,"//a[text()='Instagram']")

act=ActionChains(driver)

#Approach=1
#act.scroll_to_element(scrollTill)
#act.perform()

#Approach=2
act.scroll_to_element(scrollTill).perform()

time.sleep(5)