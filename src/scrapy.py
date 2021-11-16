# DEPENDÊNCIAS
# No diretorio raiz do projeto digite o comando abaixo:
# pip install -r requirements.txt
# https://chromedriver.storage.googleapis.com/index.html?path=86.0.4240.22/  *** download do webdriver do chromefrom selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
import re

from src.util import wait_element

driver = webdriver.Chrome(ChromeDriverManager().install())

# driver.get("https://www.google.com.br")
# input = driver.find_element_by_xpath('//input')
# input.send_keys('".gov.br" inurl:play.google.com')
# input.send_keys(Keys.RETURN)

def get_livro(url):
    # url = "http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"
    driver.get(url)
    titulo = driver.find_element_by_xpath('//h1').text
    preco = float(driver.find_element_by_xpath('//p[@class="price_color"]').text[1:])
    estoque = driver.find_element_by_xpath('//p[@class="instock availability"]').text
    estoque_num = int(re.findall('[0-9]+', estoque)[0])
    carregou  = wait_element(driver, '//div[@class="item active"]/img', by=By.XPATH, timeout=8, to_sleep=0)
    if carregou:
        img = driver.find_element_by_xpath('//div[@class="item active"]/img')

    result = {"titulo": titulo, "preco": preco, "estoque": estoque_num}

    return result

driver2 = webdriver.Chrome(ChromeDriverManager().install())
dataset = []

for i in range(1,51):
    driver2.get(f'http://books.toscrape.com/catalogue/page-{i}.html')
    lista_tagsa = driver2.find_elements_by_xpath('//h3/a')

    for l in lista_tagsa:
        # print(l)
        link = l.get_attribute('href')
        r = get_livro(link)
        dataset.append(r)

print(dataset)