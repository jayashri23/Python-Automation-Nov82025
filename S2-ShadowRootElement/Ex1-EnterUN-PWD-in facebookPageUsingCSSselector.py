import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://www.facebook.com")

time.sleep(2)
#Enter UN
driver.find_element(By.CSS_SELECTOR,"input#_R_1h6kqsqppb6amH1_").send_keys("abc")

time.sleep(2)
#Enter Pwd
driver.find_element(By.CSS_SELECTOR,"input#_R_1hmkqsqppb6amH1_").send_keys("jaya")
time.sleep(2)
