import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

path = Service("C:/Users/in04065/PycharmProjects/Selenium8Nov2025/drivers/chromedriver.exe")

driver = webdriver.Chrome(service=path)
driver.get("file:///C:/Users/in04065/PycharmProjects/Selenium8Nov2025/filej.html")
driver.find_element(By.NAME,"FileN").send_keys("Vedika")

driver.find_element(By.NAME,"FileN").send_keys("Vadde2")
time.sleep(2)

''''3.Name locator type
<html>

	<body>

		FN<input type='text' id='12345' Name='FileN'>  <br>
		LN<input type='text' id='12345'Name='FileN'>  <br>
 	</body>

</html>

When we cant use Name locator?
-->If name locator value duplicate
-->If name attribute is not present

'''

