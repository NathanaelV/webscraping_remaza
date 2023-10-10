import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import json

url = 'https://idfed.mpsa.com/idp/startSSO.ping?PartnerSpId=https%3A%2F%2Fcrmfcalatam.my.site.com%2Fgrow'


option = Options()
option.headless = True # Mudar para True para não ver o navegador em ação
browser = webdriver.Firefox(options=option)

browser.get(url)
time.sleep(2)

# Login

input=browser.find_element_by_id("username")
input.send_keys("De20517")

input=browser.find_element_by_id("password")
input.send_keys("Fr748596")
input.send_keys(Keys.ENTER)
time.sleep(5)
browser.maximize_window()


# Open Customer data

arquivo = open('leads_links.json', 'r')
conteudo = arquivo.read()
dados = json.loads(conteudo)['all_href']

# with open('leads_links.json', "r") as arquivo_json:
#     # Fazer o parse do JSON para um dicionário
#     dados = json.load(arquivo_json)

leads_dict = {'leads': []}

for count, dado in enumerate(dados, start=1):
  url_lead = dado['href']
  browser.get(url_lead)
  time.sleep(10)

  name_xpath = '/html/body/div[3]/div[2]/div/div/div[2]/div/div[3]/div[1]/div/div/div/section/div/div/div/div/article/div[2]/div/div[2]/div/div/div[2]/div[1]/div/div[2]/span/span'
  customer_name = browser.find_element_by_xpath(name_xpath).text

  phone_xpath = '/html/body/div[3]/div[2]/div/div/div[2]/div/div[3]/div[1]/div/div/div/section/div/div/div/div/article/div[2]/div/div[2]/div/div/div[2]/div[2]/div/div[2]/span/span'
  customer_phone = browser.find_element_by_xpath(phone_xpath).text

  email_xpath = '/html/body/div[3]/div[2]/div/div/div[2]/div/div[3]/div[1]/div/div/div/section/div/div/div/div/article/div[2]/div/div[2]/div/div/div[3]/div[1]/div/div[2]/span'
  customer_email = browser.find_element_by_xpath(email_xpath).text

  product_xpath = '/html/body/div[3]/div[2]/div/div/div[2]/div/div[3]/div[2]/div/div[3]/div/div/div/div[1]/article/div[2]/div/div/div/div/div[3]/div/div/table/tbody/tr/td[1]'
  product_name = browser.find_element_by_xpath(product_xpath).text

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
        "id": "",
        "account": "" 
      },
      "origin_url": url_lead
    },
    "crawler_id": "64077272771cf900d926aa45"
  }
  leads_dict['leads'].append(lead)
  print(f'Lead {count} of {len(dados)}')
  print('-------------------')

browser.quit()

open_file = open('leads_payload.json', 'w')
open_file.write(json.dumps(leads_dict))
open_file.close()



