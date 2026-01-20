import time

from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

path = Service("C:/Users/in04065/PycharmProjects/Selenium8Nov2025/drivers/chromedriver.exe")
driver= webdriver.Chrome(service=path)

driver.get("https://www.facebook.com/r.php?entry_point=login")

multiple=driver.find_element(By.XPATH, "//select[@name='birthday_month']")


s=Select(multiple)

time.sleep(2)

print(s.is_multiple)
