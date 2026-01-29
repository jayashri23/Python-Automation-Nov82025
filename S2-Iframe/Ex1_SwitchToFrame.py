

"""----IFRAME----
Iframe is a web page inside another frame
To perform action in iframe we need to switch from main frame to iframe with 3 diff ways:
    1.Using web element
    2.Using string ID/name
    3.Using Index
    To navigate from iframe to main frame we have 2 method parent(frame)&defaultContent()
    Parent frame()-:use to switch selenium focus from child frame to immediate parent frame
    defaultContent()-:use to switch selenium focus from parent frame to  main page
    to identify frame tag name check it is always Iframe

    """

import time
from operator import indexOf

from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


path = Service("C:/Users/in04065/PycharmProjects/Selenium8Nov2025/drivers/chromedriver.exe")
driver= webdriver.Chrome(service=path)

driver.get("https://www.w3schools.com/js/tryit.asp?filename=tryjs_myfirst")

#swtich to frame

#approach-1(using web element)

#frameAddress=driver.find_element(By.XPATH,"//iframe[@id='iframeResult']")   #address of frame

#driver.switch_to.frame(frameAddress)  #frame web element

#click on date and time button

#driver.find_element(By.XPATH,"//button[@type='button']").click()

#time.sleep(5)



#approach 2(using string id/name)

#driver.switch_to.frame("iframeResult")

#time.sleep(2)

#driver.find_element(By.XPATH,"//button[@type='button']").click()

#time.sleep(5)

#approach 3(using index)

driver.switch_to.frame(0)

driver.find_element(By.XPATH,"//button[@type='button']").click()
time.sleep(2)


