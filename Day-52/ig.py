from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
from idPass import *
import time

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
        self.driver.maximize_window()
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
        time.sleep(4)
        page = self.driver.find_element(By.XPATH, '/html/body/div[6]/div/div/div[2]')
        for i in range(2):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", page)
            time.sleep(2)
    
    def follow(self):
        '''To follow the people we found'''
        all_buttons = self.driver.find_elements(By.CSS_SELECTOR, 'li button')
        for button in all_buttons:
            try:
                button.click()
                time.sleep(2)
                #just to be sure :P gonna print a little :PPPP
                print('followed')
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element_by_xpath("/html/body/div[7]/div/div/div/div[3]/button[2]")
                cancel_button.click()

bot = InstaFollower()
bot.login()
bot.find_followers()
bot.follow()