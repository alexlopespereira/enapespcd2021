from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
import re


import requests

headers = {
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'x-requested-with': 'XMLHttpRequest',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36',
}

params = (
    ('infinity', 'scrolling'),
)

data = {
  'action': 'infinite_scroll',
  'page': '5',
  'currentday': '25.07.20',
  'order': 'DESC',
  'query_args[blogs]': 'augusto-nunes'
}

response = requests.post('https://veja.abril.com.br/', headers=headers, params=params, data=data)
soup = BeautifulSoup(response.json()['html'], features="lxml")
articles_text = soup.select('div[class*="card"]')[0].text
print(articles_text)

