
#is-enable method return true or false
#if button enable then will give true or disable then will give false
import time

from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

path = Service("C:/Users/in04065/PycharmProjects/Selenium8Nov2025/drivers/chromedriver.exe")
driver= webdriver.Chrome(service=path)

driver.get("https://www.facebook.com/r.php?entry_point=login")

select=driver.find_element(By.XPATH, "//label[text()='Custom']").is_selected()


if select:
    print("Is selected")
else:
    print("Is not selected")