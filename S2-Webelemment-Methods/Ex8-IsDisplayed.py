#isDisplayed
#checking element is present or not in web page


from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

path = Service("C:/Users/in04065/PycharmProjects/Selenium8Nov2025/drivers/chromedriver.exe")
driver= webdriver.Chrome(service=path)

driver.get("https://www.facebook.com/r.php?entry_point=login")


display=0    #default value assigned
try:
    display = driver.find_element(By.XPATH, "//button[text()='Sign ups']").is_displayed()

except:
    print("Exception handled")



if display:
    print("Element Present")
else:
    print("Element Not Present")