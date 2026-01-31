import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

path = Service("C:/Users/in04065/PycharmProjects/Selenium8Nov2025/drivers/chromedriver.exe")
driver= webdriver.Chrome(service=path)

driver.get("https://www.flipkart.com/")
driver.maximize_window()

#right click of mouse on top right corner
#act.context_click().perform()

cart=driver.find_element(By.XPATH,"//a[text()='Cart']")
time.sleep(2)

act=ActionChains(driver)

#Approach 1

#moving cursor to and clicking on right click
#act.move_to_element(cart).perform()
#act.context_click().perform()


#Approvaach 2
#act.move_to_element(cart).context_click().perform()

#Approach 3

act.context_click(cart).perform()
time.sleep(5)




