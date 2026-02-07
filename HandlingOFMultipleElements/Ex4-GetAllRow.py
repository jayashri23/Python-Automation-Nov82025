
import time


from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

path = Service("C:/Users/in04065/PycharmProjects/Selenium8Nov2025/drivers/chromedriver.exe")
driver= webdriver.Chrome(service=path)

driver.get("file:///C:/Users/in04065/PyCharmMiscProject/Table.html")
time.sleep(2)

allrow=driver.find_elements(By.XPATH,"//table[@id='1234']//tr")


print(len(allrow))