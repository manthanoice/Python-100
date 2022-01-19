from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from idPass import *
import time

#ToDo - Complete the methods after eating :P

CHROME_DRIVER_PATH = 'C:\Development\chromedriver.exe'
SIMILAR_ACCOUNT = 'officialfootballcommunity'
MY_USERNAME = username
MY_PASSWORD = password

class InstaFollower():
    def __init__(self):
        '''Well gonna add something here'''
        self.driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
    
    def login(self):
        '''to log into your instagram account'''
        self.driver.get(url='https://www.instagram.com/')
        time.sleep(2)
        self.login = self.driver.find_element(By.NAME, 'username')
        self.login.send_keys(MY_USERNAME)
        self.password = self.driver.find_element(By.NAME, 'password')
        self.password.send_keys(MY_PASSWORD)
        self.password.send_keys(Keys.ENTER)
        time.sleep(5)
        self.driver.get('https://instagram.com/{}'.format(SIMILAR_ACCOUNT))
    
    def find_followers(self):
        '''To find people to follow'''
        time.sleep(4)
        self.follower = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
        self.follower.click()
    
    def follow(self):
        '''To follow the people we found'''

bot = InstaFollower()
bot.login()
bot.find_followers()