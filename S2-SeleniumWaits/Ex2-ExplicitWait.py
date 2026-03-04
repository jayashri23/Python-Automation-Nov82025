"""
What is Explicit Wait?
-Wait unit a specific condition become true(require 2 para timeInSec,condition)
-if it becomes true early-->continue immediately
-if it doesn't-->throw timeout exception after X second


Important points

-uses WebDriverWait+Expected condition (EC )class
-checks every 500ms(polling time)
-Best for slow loading or dynamic element
-More reliable than time.sleep()

"""
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://www.facebook.com/")
wait = WebDriverWait(driver, 15)
element=wait.until(EC.visibility_of_element_located((By.XPATH,"//div[@role='none']")))
element.click()
time.sleep(7)
