
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

path = Service("C:/Users/in04065/PycharmProjects/Selenium8Nov2025/drivers/chromedriver.exe")
driver= webdriver.Chrome(service=path)

driver.get("file:///C:/Users/in04065/PyCharmMiscProject/Table.html")
time.sleep(2)

AllRowAddress=driver.find_elements(By.XPATH,"//tr")     #[row1Address  row2Address  row3Address  row4Address]

for singleRowAddress in AllRowAddress:     #rows -->create Outer for loop
    AllColmAddress=singleRowAddress.find_elements(By.TAG_NAME,"td")    #colmadd1 colmadd2 colmadd3
    for singleColmAddress in AllColmAddress:   #coloumn -->create Outer for loop
         print(singleColmAddress.text,end="  ")    #print inner for loop data without line break
    print()                                  #call empty print() after inner for loop for next stage cursor


