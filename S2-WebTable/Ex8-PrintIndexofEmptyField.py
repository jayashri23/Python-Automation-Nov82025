
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

path = Service("C:/Users/in04065/PycharmProjects/Selenium8Nov2025/drivers/chromedriver.exe")
driver= webdriver.Chrome(service=path)

driver.get("file:///C:/Users/in04065/PyCharmMiscProject/Table.html")
time.sleep(2)

AllRow=driver.find_elements(By.XPATH,"//tr")

rowIndex=1
for singleRow in AllRow:
    AllCol=singleRow.find_elements(By.TAG_NAME,"td")
    colIndex=1
    for singleCol in AllCol:
        if singleCol.text =="":
            print("Row Index:",rowIndex ,"Column Index:",colIndex)
        colIndex +=1
    print()
    rowIndex +=1


