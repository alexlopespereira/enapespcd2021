from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def get_pagina(driver):
    lista_items = driver.find_elements(By.XPATH, '//ul[contains(@class,"listaResultadoBusca")]')
    lista_pagina = []
    for p in lista_items:
        autor = p.find_element(By.XPATH, './/li[@class="autor"]').text
        data = p.find_element(By.XPATH, './/li[@class="dataApres"]').text
        ementa = p.find_element(By.XPATH, './/li[@class="ementa"]').text
        situacao = p.find_element(By.XPATH, './/li[@class="situacao"]').text
        lista_origem_prop = p.find_elements(By.XPATH, './/li[@class="docPropOrigem"]')
        doc_prop_origem = lista_origem_prop[0].text
        numeracao_antiga = lista_origem_prop[1].text
        result = {"autor": autor, "data": data, "ementa": ementa, "situacao": situacao, "doc_prop_origem": doc_prop_origem, "numeracao_antiga": numeracao_antiga}
        lista_pagina.append(result)
    return lista_pagina


driver = webdriver.Chrome(ChromeDriverManager().install())
url = 'https://www.camara.leg.br/buscaProposicoesWeb/resultadoPesquisa?numero=&ano=&autor=&inteiroTeor=&emtramitacao=Todas&tipoproposicao=%5BPEC+-+Proposta+de+Emenda+%C3%A0+Constitui%C3%A7%C3%A3o%5D&data=05/12/2021&page=false'

dataset = []
driver.get(url)
while True:
    lista_pagina = get_pagina(driver)
    # Insira um código para clicar no link proxima (ele está no final da página próximo aos números das páginas)
    driver.find_element(By.XPATH, '//li[@class="proxima"]').click()
    dataset = dataset + lista_pagina
    print(dataset)


