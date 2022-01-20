from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

header = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36',
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

my_response = requests.get(url='https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.69219435644531%2C%22east%22%3A-122.17446364355469%2C%22south%22%3A37.703343724016136%2C%22north%22%3A37.847169233586946%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A11%7D', headers=header)

soup = BeautifulSoup(my_response.text, 'html.parser')

all_prices = soup.select('.list-card-price')
the_price = []
for i in all_prices:
    the_price.append(i.getText().replace('bd','').replace('+','').replace('/mo','').split()[0])

all_links = soup.select('.list-card-top a')
the_link = []
for i in all_links:
    the_link.append(i.get('href'))

the_address = []
all_addresses = soup.select('.list-card-addr')
for i in all_addresses:
    the_address.append(i.getText())

google_form = 'https://docs.google.com/forms/d/1bHGU6AI2li9XbqGh4db25h2ZlkBWUPnMsVeN57rP250/viewform?edit_requested=true'

path = 'C:\Development\chromedriver.exe'

driver = webdriver.Chrome(executable_path=path)

driver.maximize_window()

driver.get(url=google_form)

time.sleep(3)

for i in range(len(the_link)-1):

    what_is_address = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div[2]/textarea')
    what_is_address.click()
    what_is_address.send_keys(the_address[i])

    what_is_price = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    what_is_price.send_keys(the_price[i])

    what_is_link_to_the_property = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    what_is_link_to_the_property.click()
    what_is_link_to_the_property.send_keys(the_link[i])

    the_submit_button = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
    the_submit_button.click()

    time.sleep(2)

    another_response = driver.find_element(By.LINK_TEXT, 'Submit another response')
    another_response.click()

driver.quit()

#you can generate spreadsheet automatically too but I don't wanna mess with my gmail credentials :P