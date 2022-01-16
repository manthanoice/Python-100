from selenium import webdriver

chrome_driver_path = 'C:\Development\chromedriver.exe'
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get('https://youtube.com')

#Todo: find some elements using selenium :P
#Don't be lazy tomorrow :P