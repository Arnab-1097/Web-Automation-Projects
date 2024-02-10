
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
#from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.support.select import Select

driver=webdriver.Chrome("C:/Users/88017/Desktop/Random/amazon automation/chromedriver.exe")

driver.get("https://www.amazon.com/")
time.sleep(10)
element1=driver.find_element(By.XPATH,"//form[@id='nav-search-bar-form']//div[@class='nav-left']")
element1.click()
element2=driver.find_element(By.XPATH,"//option[@value='search-alias=baby-products-intl-ship']")
time.sleep(3)
element2.click()
element3=driver.find_element(By.XPATH,"//form[@id='nav-search-bar-form']//div[@class='nav-fill']")
element3.click()
time.sleep(3)
element4=driver.find_element(By.XPATH,"//input[@id='twotabsearchtextbox']")
element4.send_keys("bag")
element5=driver.find_element(By.XPATH,"//form[@id='nav-search-bar-form']//div[@class='nav-right']")
element5.click()
time.sleep(3)
driver. close()
