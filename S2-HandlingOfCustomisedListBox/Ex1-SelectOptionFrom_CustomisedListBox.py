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

action=ActionChains(driver)
action.click(month).perform()

#Arrow down1
action.send_keys(Keys.ARROW_DOWN).perform()
time.sleep(2)

#Arrow down 2
action.send_keys(Keys.ARROW_UP).perform()
time.sleep(2)


