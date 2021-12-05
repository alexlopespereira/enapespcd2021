# DEPENDÊNCIAS
# No diretorio raiz do projeto digite o comando abaixo:
# pip install -r requirements.txt
# https://chromedriver.storage.googleapis.com/index.html?path=86.0.4240.22/  *** download do webdriver do chromefrom selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from src.util import wait_element

driver = webdriver.Chrome(ChromeDriverManager().install())
url=""
driver.get(url)
