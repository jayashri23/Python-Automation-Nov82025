
from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

path = Service("C:/Users/in04065/PycharmProjects/Selenium8Nov2025/drivers/chromedriver.exe")
driver = webdriver.Chrome(service=path)
driver.get("https://www.facebook.com/")

#to value from attribute
v=driver.find_element(By.XPATH, "//input[@id='email']").get_attribute("data-testid")
print(v)