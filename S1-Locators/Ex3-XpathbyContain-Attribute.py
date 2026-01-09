import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

path = Service("C:/Users/in04065/PycharmProjects/Selenium8Nov2025/drivers/chromedriver.exe")

driver = webdriver.Chrome(service=path)
driver.get("https://www.facebook.com/")

#3.Xpath by contains method
#->Attribute   //tag[contains(@AttributeName,'Partial attribute value')]
#->Text        //tag[contains(text(),'partial text value')]
#Attribute
#driver.find_element(By.XPATH, "//input[contains(@class,'55r1 _6luy')]").send_keys("jayashri")
time.sleep(2)

#driver.find_element(By.XPATH,"//input[contains(@data-testid,'-pass')]").send_keys("jayashri@23")
time.sleep(2)

#driver.find_element(By.XPATH,"//button[contains(@class,'_42ft _4jy0 _6lth _4jy6 _4jy1 selected _51sy')]").click()
time.sleep(4)
