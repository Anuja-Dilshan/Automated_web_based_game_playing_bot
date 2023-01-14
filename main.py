from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

price_dict = {}

driver_service = Service(executable_path="C:/chrome web driver/chromedriver.exe")
driver = webdriver.Chrome(service=driver_service)
driver.get(url="http://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.CSS_SELECTOR,"#cookie")

price_of_cursor_text = driver.find_element(By.CSS_SELECTOR,"#buyCursor")
x = price_of_cursor_text.text.split('\n')
price_of_cursor = int(x[0].split('-')[1].strip(' '))
price_dict["buyCursor"] = price_of_cursor

price_of_grandma_text = driver.find_element(By.CSS_SELECTOR, "#buyGrandma")
x = price_of_grandma_text.text.split('\n')
price_of_grandma = int(x[0].split('-')[1].strip(' '))
price_dict["buyGrandma"] = price_of_grandma

price_of_factory_text = driver.find_element(By.CSS_SELECTOR, "#buyFactory")
x = price_of_factory_text.text.split('\n')
price_of_factory = int(x[0].split('-')[1].strip(' '))
price_dict["buyFactory"] = price_of_factory

price_of_mine_text = driver.find_element(By.CSS_SELECTOR, "#buyMine")
x = price_of_mine_text.text.split("\n")
price_of_mine = int("".join(x[0].split('-')[1].strip(' ').split(",")))
price_dict["buyMine"] = price_of_mine

price_of_shipment_text = driver.find_element(By.CSS_SELECTOR, "#buyShipment")
x = price_of_shipment_text.text.split("\n")
price_of_shipment = int("".join(x[0].split('-')[1].strip(' ').split(",")))
price_dict["buyShipment"] = price_of_shipment

price_of_alchemy_text = driver.find_element(By.ID, "buyAlchemy lab")
x = price_of_alchemy_text.text.split("\n")
price_of_alchemy = int("".join(x[0].split('-')[1].strip(' ').split(",")))
price_dict["buyAlchemy lab"] = price_of_alchemy

price_of_portal_text = driver.find_element(By.CSS_SELECTOR, "#buyPortal")
x = price_of_portal_text.text.split("\n")
price_of_portal = int("".join(x[0].split('-')[1].strip(' ').split(",")))
price_dict["buyPortal"] = price_of_portal

price_of_timemachine_text = driver.find_element(By.ID, "buyTime machine")
x = price_of_timemachine_text.text.split("\n")
price_of_timemachine = int("".join(x[0].split('-')[1].strip(' ').split(",")))
price_dict["buyTime machine"] = price_of_timemachine

key_list = list(price_dict.keys())
value_list = list(price_dict.values())


start = time.time()
timeout = start + 5
five_min = start + 60*5



while True:
    price_list = []
    greater_price_list = []
    highest_price_index = 0

    if time.time() < five_min:
        cookie.click()
        if time.time() > timeout:
            money =driver.find_element(By.CSS_SELECTOR, "#money").text
            if "," in money:
                temp_list = money.split(',')
                money = int("".join(temp_list))
            else:
                money = int(money)


            price_list = [value for value in price_dict.values()]
            for n in range(len(price_list)):
                if price_list[n] <= money:
                    greater_price_list.append(price_list[n])

            if len(greater_price_list) != 0:
                highest_price = max(greater_price_list)
                highest_price_index = value_list.index(highest_price)
                relevant_key = key_list[highest_price_index]
                driver.find_element(By.ID, f"{relevant_key}").click()




            timeout = time.time() + 5

    else:
        cookie_sec = driver.find_element(By.ID, 'cps')
        print(cookie_sec.text)
        break
