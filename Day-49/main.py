from ftplib import all_errors
import imp
from selenium import webdriver
from selenium.webdriver.common.by import By
from mail_pass import *
import time

path = 'C:\Development\chromedriver.exe'
driver = webdriver.Chrome(executable_path=path)
driver.get(url='https://www.linkedin.com/jobs/search/?f_E=1&f_JT=I&f_WT=2&keywords=python')
time.sleep(2)

the_button = driver.find_element(By.CLASS_NAME, 'nav__button-secondary')
the_button.click()

my_email = email
my_password = password

email_ = driver.find_element(By.ID, 'username')
email_.send_keys(my_email)

password_ = driver.find_element(By.ID, 'password')
password_.send_keys(my_password)

button = driver.find_element(By.XPATH, '//*[@id="organic-div"]/form/div[3]/button')
button.click()

# time.sleep(5)
# apply = driver.find_element(By.ID, 'ember249')
# apply.click()

# time.sleep(2)
# easy_apply = driver.find_element(By.XPATH, '//*[@id="ember361"]/span')
# easy_apply.click()

all_jobs = driver.find_elements(By.CSS_SELECTOR, 'job-card-container--clickable')

for job in all_jobs:
    print('called')
    job.click()
    time.sleep(4)