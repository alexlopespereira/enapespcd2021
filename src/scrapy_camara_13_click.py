from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

url = 'https://www.camara.leg.br/buscaProposicoesWeb/pesquisaSimplificada'
driver.get(url)
driver.find_element(By.XPATH, '//input[@type="checkbox"][1]').click()
driver.find_element(By.XPATH, '//input[@id="pesquisar"]').click()