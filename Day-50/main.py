from tokenize import String
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from emailPass import *

my_email = email
my_password = password

path = 'C:\Development\chromedriver.exe'
main_page = 'https://tinder.com/'
driver = webdriver.Chrome(executable_path=path)
driver.get(url=main_page)

driver.maximize_window()

time.sleep(2)
log_in = driver.find_element(By.XPATH, '//*[@id="q1323319974"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a/span')
log_in.click()

base_driver = driver.window_handles[0]
time.sleep(3)
with_facebook = driver.find_element(By.XPATH, '//*[@id="q-405061102"]/div/div/div[1]/div/div[3]/span/div[2]/button/span[2]')
with_facebook.click()

fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)
time.sleep(4)
the_email = driver.find_element(By.ID, 'email')
the_email.send_keys(email)

time.sleep(1)
the_password = driver.find_element(By.ID, 'pass')
the_password.send_keys(my_password)

the_login = driver.find_element(By.NAME, 'login')
the_login.click()

#it asks for mobile number, don't wanna do that :P