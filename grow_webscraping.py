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
time.sleep(3)


# Search for link of leads

url_leads = 'https://crmfcalatam.my.site.com/grow/s/lead/Lead/00BA0000006AgocMAC?Lead-filterId=00BA0000006AgocMAC'
browser.get(url_leads)
time.sleep(10)

# Search for link of leads

# Dica do Marcio
a_path = "/html/body/div[3]/div[2]/div/div[2]/div/div/div/div[2]/div/div[1]/div[2]/div[2]/div[1]/div/div/table/tbody/tr/td[2]/span/a"
all_customers_links = browser.find_elements_by_xpath(a_path)


# Conseguir os hrefs
# all_customers_links[n].get_attribute('href')

# href_list = []
href_dictionary = {'all_href': []}

for element in all_customers_links:
    href_dictionary['all_href'].append({'href': element.get_attribute('href')})

browser.quit()

# breakpoint()

open_file = open('leads_links.json', 'w')
open_file.write(json.dumps(href_dictionary))
open_file.close()



# wait_for_element

# Path: /html/body/div[3]/div[2]/div/div[2]/div/div/div/div[2]/div/div[1]/div[2]/div[2]/div[1]/div/div/table/tbody/tr/td[2]/span/a

# Usar o Selenium 
