import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import json

# Leads Em Negociação
url = 'https://myhonda.my.site.com/leads/s/lead/Lead/Default?Lead-filterId=00B61000004SAJWEA4'

# # Leads Sem Atendimento
# url = 'https://myhonda.my.site.com/leads/s/lead/Lead/Default?Lead-filterId=00B4M0000055N95UAE'


option = Options()
option.headless = False # Mudar para True para não ver o navegador em ação
browser = webdriver.Firefox(options=option)

browser.get(url)
time.sleep(2)

# Login

input=browser.find_element_by_id("username")
input.send_keys("wander_silva@motoremaza.com.br")

input=browser.find_element_by_id("password")
input.send_keys("Motoremaza11*")
input.send_keys(Keys.ENTER)
browser.maximize_window()
time.sleep(10)

href_dictionary = {'all_href': []}

# Time to scroll down manually
time.sleep(60)
print('Times over')
time.sleep(10)


for i in range(1, 650):
  a_path = f"/html/body/div[3]/div[3]/div/div[2]/div/div/div/div[2]/div/div[1]/div[2]/div[2]/div[1]/div/div/table/tbody/tr[{i}]/th/span/a"
  customers_links = browser.find_element_by_xpath(a_path).get_attribute('href')
  href_dictionary['all_href'].append(customers_links)
  print(customers_links)
  print('-------------------')

open_file = open('leads_links.json', 'w')
open_file.write(json.dumps(href_dictionary))
open_file.close()

# wait_for_element
