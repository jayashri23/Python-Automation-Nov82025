import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

path = Service("C:/Users/in04065/PycharmProjects/Selenium8Nov2025/drivers/chromedriver.exe")

driver = webdriver.Chrome(service=path)
driver.get("file:///C:/Users/in04065/PycharmProjects/Selenium8Nov2025/filej.html")
driver.find_element(By.CLASS_NAME, "class2").send_keys("Jeevika")
driver.find_element(By.CLASS_NAME, "class2").send_keys("vadde")
time.sleep(2)

'''
4.Class Name locator
<html>

	<body>

		FN<input type='text' id='12345' Name='FileN' class='class2'>  <br>
		LN<input type='text' id='12345'Name='FileN' class='class2' >  <br>
 	</body>

</html>
when we can use class locator?
->if duplicate class attribute present
->if class attribute not present
'''