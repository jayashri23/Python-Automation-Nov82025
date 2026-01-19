
#is-enable method method return true or false
#if button enable then will give true or disable then will give false
import time

from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

path = Service("C:/Users/in04065/PycharmProjects/Selenium8Nov2025/drivers/chromedriver.exe")
driver= webdriver.Chrome(service=path)

driver.get("https://www.instagram.com/?flo=true")
result2=driver.find_element(By.XPATH,"//button[@type='submit']").is_enabled()
time.sleep(5)
print(result2)



#driver.get("https://www.facebook.com/")
#result=driver.find_element(By.XPATH, "//button[@value='1']").is_enabled()
#print(result)