import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://books-pwakit.appspot.com/explore?q=")

driver.maximize_window()


#step 1 locate xpath of parent element
#step 2 then locate shadow element using css selector
driver.find_element(By.XPATH,"//book-app[@apptitle='BOOKS']").shadow_root.find_element(By.CSS_SELECTOR,"input[id='input']").send_keys("jayavish")
time.sleep(2)