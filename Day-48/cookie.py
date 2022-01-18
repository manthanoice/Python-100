from selenium import webdriver
from selenium.webdriver.common.by import By
import time

path = 'C:\Development\chromedriver.exe'
driver = webdriver.Chrome(executable_path=path)
driver.get(url='http://orteil.dashnet.org/experiments/cookie/')

cookie = driver.find_element(By.ID, "cookie")

timeout = time.time() + 5
game_time = time.time() + 10 * 60

while True:
    cookie.click()
    if time.time() >= timeout:
        store_items = driver.find_elements(By.CSS_SELECTOR, '#store b')
        all_items = [item for item in store_items if item.text != '']
        unav_items = driver.find_elements(By.CSS_SELECTOR, '#store .grayed b')
        aval_items = [item for item in all_items if item not in unav_items]
        cost = [int(item_cost.text.split(' - ')[1]) for item_cost in aval_items]
        index_of_purchase = cost.index(max(cost))
        aval_items[index_of_purchase].click()
        timeout+=5
    
    if time.time() >= game_time:
        print(driver.find_element(By.ID, 'cps').text)
        break