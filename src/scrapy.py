# DEPENDÊNCIAS
# No diretorio raiz do projeto digite o comando abaixo:
# pip install -r requirements.txt
# https://chromedriver.storage.googleapis.com/index.html?path=86.0.4240.22/  *** download do webdriver do chromefrom selenium import webdriver
from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from src.util import wait_element

driver = webdriver.Chrome(ChromeDriverManager().install())
url = 'https://www.camara.leg.br/buscaProposicoesWeb/resultadoPesquisa?numero=&ano=&autor=&inteiroTeor=&emtramitacao=Todas&tipoproposicao=%5BPEC+-+Proposta+de+Emenda+%C3%A0+Constitui%C3%A7%C3%A3o%5D&data=09/12/2021&page=false'
driver.get(url)

def get_pagina(driver):
    geral = driver.find_elements(By.XPATH,'//ul[@class="infoPesquisa"]/..')
    dataset = []
    for x in geral:
        titulo = x.find_element(By.XPATH, '//span[@class="titulo"]').text
        result = {'titulo': titulo}
        nome = x.find_element(By.XPATH, './/li[@class="autor"]').text.split(':')
        result[nome[0]] = nome[1].strip()
        data = x.find_element(By.XPATH, './/li[@class="dataApres"]').text.split(':')
        result[data[0]] = data[1].strip()
        ementa = x.find_element(By.XPATH, './/li[@class="ementa"]').text.split(':')
        result[ementa[0]] = ementa[1].strip()
        try:
            situacao = x.find_element(By.XPATH, './/li[@class="situacao"]').text.split(':')
            result[situacao[0]] = situacao[1].strip()
        except (StaleElementReferenceException, NoSuchElementException) as e:
            print(e)

        proposicao = x.find_elements(By.XPATH, './/li[@class="docPropOrigem"]')

        for y in proposicao:
            lista = y.text.split(':')
            result[lista[0]] = lista[1].strip()
            dataset.append(result)
    return dataset

dataset = []
while True:
    lista_pagina = get_pagina(driver)
    driver.find_element(By.XPATH, '//li[@class="proxima"]/a').click()
    dataset = dataset + lista_pagina
    print(dataset)

