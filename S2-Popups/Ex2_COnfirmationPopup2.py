import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

path = Service("C:/Users/in04065/PycharmProjects/Selenium8Nov2025/drivers/chromedriver.exe")
driver= webdriver.Chrome(service=path)

driver.get("https://demo.guru99.com/test/delete_customer.php")
time.sleep(2)

driver.find_element(By.XPATH,"//input[@type='text']").send_keys("12345")

time.sleep(2)

driver.find_element(By.XPATH,"//input[@type='submit']").click()
time.sleep(2)

#Created object of alert used to reduse again and again using switch

alertObject=driver.switch_to.alert
print(alertObject.text)

#alertObject.accept()
time.sleep(2)

alertObject.dismiss()
time.sleep(2)