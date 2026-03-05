import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://www.amazon.in/?&tag=googhydrabk1-21&ref=pd_sl_5szpgfto9i_e&adgrpid=155259813593&hvpone=&hvptwo=&hvadid=674893540034&hvpos=&hvnetw=g&hvrand=13128329743480757641&hvqmt=e&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9301354&hvtargid=kwd-64107830&hydadcr=14452_2316413&gad_source=1")

time.sleep(2)
driver.maximize_window()

driver.find_element(By.XPATH,"//input[@id='twotabsearchtextbox']").send_keys("Redmi 12 5G")

driver.find_element(By.XPATH,"//input[@type='submit']").click()

getratingFromAmazon=driver.find_element(By.XPATH,"(//div[@class='a-section a-spacing-none _c2Itd_container_1AABc _c2Itd_asinContainer_2efLb _c2Itd_block_2h9ji _c2Itd_hFull_iOctn _c2Itd_wFull_1ElP1 _c2Itd_row_3iYNo']//span)[4]")
print(getratingFromAmazon)

time.sleep(2)

