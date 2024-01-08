import time
import requests
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
import json

arquivo = open('leads_links.json', 'r')
conteudo = arquivo.read()
urls = json.loads(conteudo)['all_href']

option = Options()
option.headless = True # Mudar para True para não ver o navegador em ação

browser = webdriver.Firefox(options=option)

login_url = 'https://myhonda.my.site.com/leads/login?ec=302&startURL=%2Fleads%2Fs%2F'
browser.get(login_url)
time.sleep(2)

# Login

input=browser.find_element_by_id("username")
input.send_keys("wander_silva@motoremaza.com.br")

input=browser.find_element_by_id("password")
input.send_keys("Motoremaza11*")
input.send_keys(Keys.ENTER)
time.sleep(2)

for count, url in enumerate(urls, start=1):
  browser.get(url)
  time.sleep(10)
  print(url)

  name_xpath = '/html/body/div[3]/div[3]/div/div[2]/div[2]/div/div/div/section/div/div/div/div/article/div[2]/div/div[1]/div/div/div[1]/div[1]/div/div[2]/span/span'
  customer_name = browser.find_element_by_xpath(name_xpath).text
  print(f'Name: {customer_name}')
  print('-------------------')

  phone_xpath = '/html/body/div[3]/div[3]/div/div[2]/div[2]/div/div/div/section/div/div/div/div/article/div[2]/div/div[6]/div/div/div[1]/div[1]/div/div[2]/span/span'
  customer_phone = browser.find_element_by_xpath(phone_xpath).text
  print(f'Phone: {customer_phone}')
  print('-------------------')

  email_xpath = '/html/body/div[3]/div[3]/div/div[2]/div[2]/div/div/div/section/div/div/div/div/article/div[2]/div/div[6]/div/div/div[1]/div[2]/div/div[2]/span/a'
  customer_email = browser.find_element_by_xpath(email_xpath).text
  print(f'Email: {customer_email}')
  print('-------------------')

  product_xpath = '/html/body/div[3]/div[3]/div/div[2]/div[2]/div/div/div/section/div/div/div/div/article/div[2]/div/div[1]/div/div/div[3]/div[1]/div/div[2]/span/span'
  product_name = browser.find_element_by_xpath(product_xpath).text
  print(f'Produto: {product_name}')
  print('-------------------')

  dealership_xpath = '/html/body/div[3]/div[3]/div/div[2]/div[2]/div/div/div/section/div/div/div/div/article/div[2]/div/div[9]/div/div/div/div[1]/div/div[2]/span/div/a'
  dealership_name = browser.find_element_by_xpath(dealership_xpath).text
  print(f'Dealership: {dealership_name}')
  print('-------------------')

  dealership_code_xpath = '/html/body/div[3]/div[3]/div/div[2]/div[2]/div/div/div/section/div/div/div/div/article/div[2]/div/div[12]/div/div/div[2]/div[2]/div/div[2]/span/span'
  dealership_code = browser.find_element_by_xpath(dealership_code_xpath).text
  print(f'Dealer: {dealership_code}')
  print('-------------------')

  type_xpath = '/html/body/div[3]/div[3]/div/div[2]/div[2]/div/div/div/section/div/div/div/div/article/div[2]/div/div[1]/div/div/div[2]/div[1]/div/div[2]/span/span'
  type_name = browser.find_element_by_xpath(type_xpath).text
  print(f'Type: {type_name}')
  print('-------------------')

  time.sleep(1)

  lead = {
      "lead": {
        "customer": {
          "name": customer_name,
          "phone": customer_phone,
          "email": customer_email
        },
        "product": {
          "name": product_name 
        },
        "dealership": {
          "id": dealership_code,
          "account": dealership_name 
        },
        "origin_url": url,
        "type": type_name
      },
      "crawler_id": "6418db35059b6800d8e07f57"
    }

  # leads_dict['leads'].append(lead)
  url_post = 'https://motoremaza.f1sales.org/public/integrations/crawlers/6418db35059b6800d8e07f57/leads'

  response = requests.post(url_post, json=lead)
  print(response.text)
  print(f'Lead {count} of {len(urls)}')
  print('-------------------')

browser.quit()
