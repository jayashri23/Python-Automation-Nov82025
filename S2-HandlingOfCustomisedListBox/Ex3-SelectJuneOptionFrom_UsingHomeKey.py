import time


from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

path = Service("C:/Users/in04065/PycharmProjects/Selenium8Nov2025/drivers/chromedriver.exe")
driver= webdriver.Chrome(service=path)

driver.get("https://www.facebook.com/r.php?entry_point=login")

driver.maximize_window()
time.sleep(2)

month=driver.find_element(By.XPATH,"//select[@name='birthday_month']")

act=ActionChains(driver)

#open list option from list options
act.click(month).perform()
time.sleep(2)

#IF SELECTED CASE DYNAMIC THEN USE HOME key
act.send_keys(Keys.HOME).perform()
time.sleep(2)

for i in range(5):
    act.send_keys(Keys.ARROW_DOWN).perform()
    time.sleep(2)

#click enter for selected option
act.send_keys(Keys.ENTER).perform()
time.sleep(2)
