from selenium import webdriver
from selenium.webdriver.common.by import By

#setting up the driver
google_driver = 'C:\Development\chromedriver.exe'
driver = webdriver.Chrome(executable_path=google_driver)

#getting to the url
driver.get(url='https://en.wikipedia.org/wiki/Main_Page')

#finding the article count
article_count = driver.find_element(By.XPATH, '//*[@id="articlecount"]/a[1]')
print(article_count.text)

#quitting the browser
driver.quit()