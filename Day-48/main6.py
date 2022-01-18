from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

#setting up the driver
google_driver = 'C:\Development\chromedriver.exe'
driver = webdriver.Chrome(executable_path=google_driver)

#getting the url
driver.get(url='https://secure-retreat-92358.herokuapp.com/')

#name
name = driver.find_element(By.NAME, 'fName')
name.send_keys('Manthan')

#last-name
last_name = driver.find_element(By.NAME, 'lName')
last_name.send_keys('Bosamiya')

#email
email = driver.find_element(By.NAME, 'email')
email.send_keys('mvbosamiya20@gmail.com')

#submitting
submit = driver.find_element(By.XPATH, '/html/body/form/button')
submit.send_keys(Keys.ENTER)