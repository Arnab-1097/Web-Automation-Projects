from selenium import webdriver
import time

from selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome("C:\chrome driver\chromedriver.exe")
driver.get("https://web.whatsapp.com/")
time.sleep(10)

vertical_menu=driver.find_element_by_css_selector("span[data-testid='menu']")
vertical_menu.click()
lgout=driver.find_element_by_css_selector("div[aria-label='Log out']")
lgout.click()
