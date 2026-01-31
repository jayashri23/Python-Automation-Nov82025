import time


from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

path = Service("C:/Users/in04065/PycharmProjects/Selenium8Nov2025/drivers/chromedriver.exe")
driver= webdriver.Chrome(service=path)

driver.get("https://demo.guru99.com/test/drag_drop.html")
driver.maximize_window()
time.sleep(5)

src=driver.find_element(By.XPATH,"(//a[@class='button button-orange'])[2]")
des=driver.find_element(By.XPATH,"(//div[@class='ui-widget-content'])[3]")

act= ActionChains(driver)
#Approach 1
act.move_to_element(src).click_and_hold().move_to_element(des).release().perform()

#Approach 2

act.drag_and_drop()

time.sleep(10)
