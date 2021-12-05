# Revista veja
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
import re

from src.util import wait_element

driver = webdriver.Chrome(ChromeDriverManager().install())


url = 'https://veja.abril.com.br/blog/augusto-nunes/'
driver.get(url)
xpath_next_page = '//span/button'
xpath_lista = '//section[@class="cards"]//div[@class="row"]'
lista_result = []
for p in range(100):
    wait_element(driver, by=By.XPATH, by_content=xpath_next_page)
    driver.find_element(By.XPATH, xpath_next_page).click()
    wait_element(driver, by=By.XPATH, by_content=xpath_lista)
    lista_items = driver.find_elements(By.XPATH, xpath_lista)
    for i in lista_items:
        autor = driver.find_element(By.XPATH, '')
        print(lista_items[0].text)

    # nome = p.find_element(By.XPATH, './/a[@class="title"]').text
    # descricao = p.find_element(By.XPATH, './/p[@class="description"]').text
    # urlnome = p.find_element(By.XPATH, './/a').get_attribute('href')
    # preco = float(p.find_element(By.XPATH, './/h4[@class="pull-right price"]').text[1:])
    # qtd_reviews = int(re.findall('[0-9]+', p.find_element(By.XPATH, './/p[@class="pull-right"]').text)[0])
    # result = {"Nome": nome, "Url": urlnome, "Descrição": descricao, "Preço": preco, "Reviews": qtd_reviews}
    # lista_result.append(result)

print(lista_result)

