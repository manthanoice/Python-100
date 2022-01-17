from datetime import date
from selenium import webdriver
from selenium.webdriver.common.by import By

#setting up driver
chrome_driver_path = 'C:\Development\chromedriver.exe'
driver = webdriver.Chrome(executable_path=chrome_driver_path)

#getting to the url
driver.get(url='https://www.python.org/')

#finding the element we want
find = driver.find_element(By.XPATH, '//*[@id="content"]/div/section/div[2]/div[2]/div/ul')
date_event = find.text.split('\n')
# print(date_event)

#getting date and event name
date = date_event[0:len(date_event):2]
event = date_event[1:len(date_event):2]

# print(date)
# print(event)

#making empty dir to store the data in it
the_dir = {}

#adding data to dir using for loop
for i in range(len(date)):
    the_dir[i]={
        'time':date[i],
        'event':event[i]
    }

#finally printing the data we added
print(the_dir)

#quitting the drive :P
driver.quit()