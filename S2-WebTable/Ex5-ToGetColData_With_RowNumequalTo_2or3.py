
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

path = Service("C:/Users/in04065/PycharmProjects/Selenium8Nov2025/drivers/chromedriver.exe")
driver= webdriver.Chrome(service=path)

driver.get("file:///C:/Users/in04065/PyCharmMiscProject/Table.html")
time.sleep(2)

multipleText=driver.find_elements(By.XPATH,"//table[@id='1234']//tr[position()=2 or position()=4]/td[2]")

#get data from col2 row num=2 and row num =3
#app-1
print(len(multipleText))
#print(multipleText[0].text)
#print(multipleText[1].text)

#app2
for element in multipleText:
    print(element.text)
time.sleep(2)