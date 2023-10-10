import time
import requests
# import pandas as pd 
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import json

url = 'https://myhonda.force.com/concessionaria/apex/myHonda_LeadBox?sfdc.tabName=01r61000000edb2'

option = Options()
option.headless = False # Mudar para True para não ver o navegador em ação
browser = webdriver.Firefox(options=option)

browser.get(url)
time.sleep(2)

# Login

input=browser.find_element_by_id("username")
input.send_keys("eprado@daitan.com.br")

input=browser.find_element_by_id("password")
input.send_keys("Edi1020+")
input.send_keys(Keys.ENTER)
time.sleep(10)


# Search for date

input=browser.find_element_by_id("startDate")
input.send_keys("02112022")

input=browser.find_element_by_id("endDate")
input.send_keys("03112022")

input=browser.find_element_by_id("j_id0:j_id46:searchBlock:j_id47:bottom")
input.send_keys(Keys.ENTER)


# driver.quit()