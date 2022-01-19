import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from emailPass import *

EXPECTED_DOWNLOAD_SPEED = 1
EXPECTED_UPLOAD_SPEED = 1

TWITTER = 'https://TWITTER.com/'
SPEEDTEST = 'https://www.speedtest.net/'

MYUSERNAME = username
MYPASSWORD = password

class InternetSpeedTwitterBot():
    '''
    The bot that will check if internet speed and will send tweet to your internet service provider if the speed is not enough :P
    '''
    def __init__(self):
        '''
        Defining variables and setting path and driver
        '''
        self.path = 'C:\Development\chromedriver.exe'
        self.driver = webdriver.Chrome(executable_path=self.path)
        self.download_speed = 0
        self.upload_speed = 0
    
    def get_internet_speed(self):
        '''
        returns download speed and upload speed
        '''
        #getting driver to the speedtest website
        self.driver.get(SPEEDTEST)
        self.go = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
        self.go.click()
        #wait for maybe 60 seconds until the speed test is done
        time.sleep(60)
        #getting the download speed
        self.down = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')
        self.download_speed = self.down.text
        #getting the upload speed
        self.up = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span')
        self.upload_speed = self.up.text
        #printing them in console
        print(self.download_speed)
        print(self.upload_speed)
    
    def tweet_at_provider(self):
        '''
        Checks if the speed is not up to expected speed, it will send tweet from your account
        '''
        #check if and only if speed is less than expected speed, execute this method
        if float(self.download_speed) > EXPECTED_DOWNLOAD_SPEED and float(self.upload_speed) > EXPECTED_UPLOAD_SPEED:
            #getting driver to one of the most toxic social media platform where everyone fights about their opinions and can't accpet others' opinions
            self.driver.get(TWITTER)
            time.sleep(1)
            #signing in
            self.sign_in = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[5]/a/div')
            self.sign_in.click()
            time.sleep(2)
            #entering username
            self.the_username_input = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[5]/label/div/div[2]/div/input')
            self.the_username_input.click()
            self.the_username_input.send_keys(MYUSERNAME)
            self.next_step = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[6]/div/span/span')
            self.next_step.click()
            time.sleep(1)
            #then entering password
            self.password_entering = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[3]/div/label/div/div[2]/div[1]/input')
            self.password_entering.send_keys(MYPASSWORD)
            self.password_entering.send_keys(Keys.ENTER)
            time.sleep(5)
            #making the tweet
            self.tweeting = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div')
            self.tweeting.click()
            self.message = '[Bot test] Hey internet service provider, why my internet speed currently is {} down and {} up when we had deal of having {} down and {} up'.format(self.download_speed, self.upload_speed, EXPECTED_DOWNLOAD_SPEED, EXPECTED_UPLOAD_SPEED)
            self.tweeting.send_keys(self.message)
            #sending the tweet
            self.send_tweet = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div/div/span/span')
            self.send_tweet.click()
            #finding my profile
            self.my_profile = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[2]/div/div/div/div/div[2]/div/div[2]/div/div/div[4]/div')
            self.my_profile.click()
            #finding log out option from my profile and then logging out
            self.log_out = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div[2]/div/div[2]/div/div/div/div/div/a[2]/div[1]/div')
            self.log_out.click()
            self.final_log_out = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div[2]/div[1]/div/span/span')
            self.final_log_out.click()
        else:
            pass