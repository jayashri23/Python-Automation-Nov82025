'''1.TagName -
any keyword present after < symbol
<Input
<Id
<button

2.Attribute-any value present after =symbol right side
id=1322
id->Attribute name
1322->Attribute value

3.Text -->text coming in >< symbol is Text

>facebook<


----------------------LOCATORS----------------------------
locator used to find address of specific element present in webpage
8 -types of locators

1.Tag name             -    Tag name
2.ID                   -    Attribute
3.Name                 -    Attribute
4.ClassName            -    Attribute
5.LinkText             -    Text
6.Partial Link Text    -    text
7.CSS                  -    Expression
8.Xpath                -    Expression'''
import email
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

path = Service("C:/Users/in04065/PycharmProjects/Selenium8Nov2025/drivers/chromedriver.exe")

driver = webdriver.Chrome(service=path)
driver.get("https://www.facebook.com/")
#----4 type of XPath formula---------
#1.driver.find_element(locator type")
#driver.find _element(By.XPATH,"XPATH Expression")
driver.find_element(By.XPATH, "//input[@name='email']").send_keys("jsjankar23@gmail.com")
driver.find_element(By.XPATH, "//input[@type='password']").send_keys("jayashri@23")
driver.find_element(By.XPATH,"//button[@name='login']").click()
time.sleep(50)

#Control +shift +i   ->to open banking site inspect