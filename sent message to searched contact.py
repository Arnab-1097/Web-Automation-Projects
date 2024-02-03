from selenium import webdriver
import time

from selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome("C:\chrome driver\chromedriver.exe")
driver.get("https://web.whatsapp.com/")
time.sleep(10)
thumbnail=driver.find_element_by_xpath("//div[@role='textbox']")
thumbnail.click()
thumbnail.send_keys("01970208542")
thumbnail.send_keys(Keys.ENTER)
#thumbnail=driver.find_element_by_xpath("//body/div[@id='app']/div[@class='_1ADa8 _3Nsgw app-wrapper-web font-fix os-win']/div[@class='_1XkO3 two']/div[@class='ldL67 _2i3T7 _191H_']/div[@id='side']/div[@id='pane-side']/div/div/div[@aria-label='Chat list']/div[11]/div[1]/div[1]/div[2]")

xx = driver.find_element_by_xpath("//div[@title='Type a message']")
xx.click()
xx.send_keys("good morning <3!!!")
xx.send_keys(Keys.ENTER)