from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

#setting up the driver
google_driver = 'C:\Development\chromedriver.exe'
driver = webdriver.Chrome(executable_path=google_driver)

#getting to the url
driver.get(url='https://en.wikipedia.org/wiki/Main_Page')

#finding the article count
article_count = driver.find_element(By.XPATH, '//*[@id="articlecount"]/a[1]')
# article_count.click()

all_portals = driver.find_element(By.LINK_TEXT, 'All portals')
# all_portals.click()

search = driver.find_element(By.NAME, 'search')
search.send_keys('FC Barcelona')
search.send_keys(Keys.ENTER)

#quitting the browser
# driver.quit()