
#4.Xpath by Index--multiple matching xpath expression
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

path = Service("C:/Users/in04065/PycharmProjects/Selenium8Nov2025/drivers/chromedriver.exe")

driver = webdriver.Chrome(service=path)
driver.get("https://www.facebook.com/r.php?entry_point=login")
driver.find_element(By.XPATH, "(//input[@type='text'])[1]").send_keys("jayashri")
time.sleep(2)
driver.find_element(By.XPATH, "(//input[@type='text'])[2]").send_keys("vadde")
time.sleep(2)
driver.find_element(By.XPATH,"(//input[@type=""text""])[5]").send_keys('8830340932')
time.sleep(2)


"""5.Absolute xpath
use to navigate from parent to immediate child
we can achieve absolute using /
user name-absolute xpath
example-html/body/dev(1)/input(1)
html/body/dev(2)/button

6.Relative xpath
use to navigate from parent to any child
we can achieve reative  using //
user name-relative xpath
example-//dev(1)/input(1) or //dev//input(1)
//dev(2)/button or //dev(2)//button

"""