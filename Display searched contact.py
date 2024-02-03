from selenium import webdriver
import time

from selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome("C:\chrome driver\chromedriver.exe")
driver.get("https://web.whatsapp.com/")
time.sleep(10)
thumbnail=driver.find_element_by_xpath("//div[@role='textbox']")
thumbnail.click()
thumbnail.send_keys("01970208542")