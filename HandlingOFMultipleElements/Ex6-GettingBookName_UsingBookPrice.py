
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

path = Service("C:/Users/in04065/PycharmProjects/Selenium8Nov2025/drivers/chromedriver.exe")
driver= webdriver.Chrome(service=path)

driver.get("file:///C:/Users/in04065/PyCharmMiscProject/Table.html")
time.sleep(2)

value=driver.find_element(By.XPATH,"//table[@id='1234']//td[text()='300']//parent::tr/td[2]").text
print("Book name:",value)