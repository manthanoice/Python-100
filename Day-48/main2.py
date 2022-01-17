from selenium import webdriver
from selenium.webdriver.common.by import By

#setting up driver
chrome_driver_path = 'C:\Development\chromedriver.exe'
driver = webdriver.Chrome(executable_path=chrome_driver_path)

#getting to the url we want
driver.get(url='https://www.amazon.in/Samsung-Fully-Automatic-WA65A4002VS-TL-Technology/dp/B08GY3PZQF/ref=lp_27089563031_1_1')

#finding the price
price = driver.find_element(By.XPATH, '//*[@id="corePrice_desktop"]/div/table/tbody/tr[2]/td[2]/span[1]/span[2]')
the_price = price.text

#formatting the price
the_final_price = float(the_price.replace(',','').strip('₹'))
print(the_final_price)

#quitting the browser :P
driver.quit()