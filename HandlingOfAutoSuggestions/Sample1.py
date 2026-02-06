import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

path = Service("C:/Users/in04065/PycharmProjects/Selenium8Nov2025/drivers/chromedriver.exe")
driver= webdriver.Chrome(service=path)

driver.get("https://www.google.com/")

driver.find_element(By.XPATH,"//textarea[@class='gLFyf']").send_keys("redmi note 14")
driver.maximize_window()
time.sleep(2)

ExpectedText="redmi note 14"
MultipleElementAddress=driver.find_elements(By.XPATH,"(//ul[@class='G43f7e'])[1]/li//div[@class='eIPGRd']")

for i in MultipleElementAddress:

#All objects print
        actualText=i.text
        if actualText == ExpectedText:   #comparing
               i.click()     #opening selected text
               break


time.sleep(20)
