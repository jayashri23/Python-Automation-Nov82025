#switch to main frame -use switch.defaultContent()-to navigate from any child frame to main frame

#switch to main frame-use switchto.parentframe()-to navigate from child frame to parent frame.


import time

from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

path = Service("C:/Users/in04065/PycharmProjects/Selenium8Nov2025/drivers/chromedriver.exe")
driver= webdriver.Chrome(service=path)

driver.get("https://www.w3schools.com/js/tryit.asp?filename=tryjs_myfirst")

frameAddress=driver.find_element(By.XPATH,"//iframe[@id='iframeResult']")   #address of frame

driver.switch_to.frame(frameAddress)  #frame web element

#click on date and time button

driver.find_element(By.XPATH,"//button[@type='button']").click()

#switch to main page
#Approach 1

#driver.switch_to.parent_frame()

#Approvach 2

driver.switch_to.default_content()

driver.find_element(By.XPATH,"//a[@id='menuButton']").click()
time.sleep(5)


