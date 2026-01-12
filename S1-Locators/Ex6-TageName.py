import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

path = Service("C:/Users/in04065/PycharmProjects/Selenium8Nov2025/drivers/chromedriver.exe")

driver = webdriver.Chrome(service=path)
driver.get("file:///C:/Users/in04065/PycharmProjects/Selenium8Nov2025/filej.html")

#enter FN
driver.find_element("tag name","input").send_keys("PAPA")
time.sleep(2)
#enter LN
driver.find_element("tag name","input").send_keys("AAI")
time.sleep(2)
"""
#tag name
<html>
   <body>
       FN<Input='text'> <br>
       LN<Input='text'> <br>
   </body>
</html>"""

#when we cant use tagname as locator type?
#-->when tag name is duplicate

