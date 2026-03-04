"""
2.Alert/Confirmation popup-
-we cannot inspect element present on popup
-these popip contain ok /cancel buttons
-sometimes these popup contains ? or ! symbols
-

"""
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

#get text from alert

text=driver.switch_to.alert.text
print(text)
time.sleep(2)

#to click on cancel button

#driver.switch_to.alert.dismiss()
#time.sleep(2)

#to click on ok button of 1st alert

driver.switch_to.alert.accept()
time.sleep(2)

#to click on ok for 2nd alert
driver.switch_to.alert.accept()
time.sleep(2)


