
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

path = Service("C:/Users/in04065/PycharmProjects/Selenium8Nov2025/drivers/chromedriver.exe")
driver= webdriver.Chrome(service=path)

driver.get("https://www.facebook.com")

driver.maximize_window()

allElement=driver.find_elements(By.XPATH, "//a")

print(len(allElement))

for i in allElement:
    value=i.text
    print(value)

