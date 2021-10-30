# DEPENDÊNCIAS
# No diretorio raiz do projeto digite o comando abaixo:
# pip install -r requirements.txt
# https://chromedriver.storage.googleapis.com/index.html?path=86.0.4240.22/  *** download do webdriver do chromefrom selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome(ChromeDriverManager().install())

url = "https://www.google.com"
driver.get(url)
# Se o selenium abrir uma janela do navegador, voce está pronto para
# fazer um webscrapy!!!  :)

