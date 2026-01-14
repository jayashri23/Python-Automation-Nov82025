
from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

path = Service("C:/Users/in04065/PycharmProjects/Selenium8Nov2025/drivers/chromedriver.exe")
driver= webdriver.Chrome(service=path)
driver.get("https://www.facebook.com/")

driver.find_element(By.XPATH, "//input[@class='inputtext _55r1 _6luy']").send_keys("vishal vadde")

#given input text printed
inptext=driver.find_element(By.XPATH,"//input[@class='inputtext _55r1 _6luy']").get_attribute("value")
print(inptext)

