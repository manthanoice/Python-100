from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

path = 'C:\Development\chromedriver.exe'
driver = webdriver.Chrome(executable_path=path)

driver.maximize_window()
driver.get(url='https://github.com/manthanoice')
while True:
    time.sleep(5)
    driver.refresh()