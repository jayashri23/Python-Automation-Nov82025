import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

path = Service("C:/Users/in04065/PycharmProjects/Selenium8Nov2025/drivers/chromedriver.exe")

driver = webdriver.Chrome(service=path)
driver.get("file:///C:/Users/in04065/PycharmProjects/Selenium8Nov2025/filej.html")
driver.find_element(By.ID,"12345").send_keys("vishu")
time.sleep(2)
driver.find_element(By.ID,"12345").send_keys("vadde")
time.sleep(2)
'''
2.ID locator type
<html>

	<body>

		FN<input type='text' id='12345'>  <br>
		LN<input type='text' id='12345'>  <br>
 	</body>

when we cant use ID locator?
-->if duplicate id locator 
-->if not present id locator
</html>'''