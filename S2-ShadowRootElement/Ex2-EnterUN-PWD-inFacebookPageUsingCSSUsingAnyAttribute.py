import time


# For any attribute -
#tagName[attribute='vale']

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://www.facebook.com")

time.sleep(2)

driver.find_element(By.CSS_SELECTOR,"input[type='text']").send_keys("aaa")
time.sleep(2)

driver.find_element(By.CSS_SELECTOR,"input[type='password']").send_keys("bbbb")
time.sleep(2)
