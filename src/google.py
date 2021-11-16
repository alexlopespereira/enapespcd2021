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

driver.get("https://www.google.com.br")
input = driver.find_element_by_xpath('//input')
input.send_keys('".gov.br" inurl:play.google.com')
input.send_keys(Keys.RETURN)