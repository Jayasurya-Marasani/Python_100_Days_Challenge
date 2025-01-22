from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get(url = "https://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID, value="cookie")
money = driver.find_element(By.ID, value="money")

items = driver.find_elements(By.CSS_SELECTOR, "#store div")
items_ids = [item.get_attribute("id") for item in items]
time_out = time.time()+5
five_min = time.time() + 60*5

while True:
    cookie.click()
    if time_out > five_min:
        all_prices = driver.find_elements(By.CSS_SELECTOR, "#store b")
        prices = [price.text for price in prices]
        item_prices = []
        for price in all_prices:
            element_text = price.text
            if element_text != "":
                cost = int(element_text.split("-")[1].strip().replace(",", ""))
                item_prices.append(cost)
        
        cookie_upgrades = {}
        for n in range(len(item_prices)):
            cookie_upgrades[item_prices[n]] = items_ids[n]
        
        money_element = driver.find_element(By.ID, value="money").text
        if "," in money_element:
            money_element = money_element.replace(",", "")
        
        cookie_count = int(money_element)

        afforadable_upgrades = {}
        for cost, id in cookie_upgrades.items():
            if cookie_count>cost:
                afforadable_upgrades[cost] = id
        highest_price_affordable_upgrade = max(afforadable_upgrades)
        print(highest_price_affordable_upgrade)
        to_purchase_id = afforadable_upgrades[highest_price_affordable_upgrade]

        time_out = time.time() + 5

        if time.time() > five_min:
            cookie_per_s = driver.find_element(By.ID, value="cps").text
            print(cookie_per_s)
            break




