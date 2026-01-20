import time

from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

path = Service("C:/Users/in04065/PycharmProjects/Selenium8Nov2025/drivers/chromedriver.exe")
driver= webdriver.Chrome(service=path)

driver.get("file:///C:/Users/in04065/PycharmProjects/Selenium8Nov2025/MultipleListBox.html")

multiple=driver.find_element(By.XPATH, "//select[@id='1234']")

s=Select(multiple)
#s.select_by_index(1)
s.select_by_index(0)
s.select_by_index(2)
s.select_by_visible_text("UK")
time.sleep(2)


