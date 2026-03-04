"""               Selenium waits(imp)
Different types of wait in selenium
implicit wait
Explicit wait
Fluent wait

Synchronization wait--matching selenium speed with browser speed

time.sleep()--static wait(wait till given time)
Selenium wait--dynamic wait(not wait sync with web element)

1.Implicit wait---
-Global wait applied to all elements(complete webpage)
-Wait for fixed time while locating elements
-Continuance early if web element appears (webpage loaded)
-Default polling =500ms

"""


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.facebook.com/")
driver.implicitly_wait(2)