from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
url = 'http://tabnet.datasus.gov.br/cgi/tabcgi.exe?sih/cnv/qgbr.def'
driver.get(url)

for i in range(2, 16):
    to_select_conteudo = driver.find_element(By.XPATH, f'//select[@id="I"]/option[{i}]')
    ActionChains(driver).key_down(Keys.CONTROL).click(to_select_conteudo).key_up(Keys.CONTROL).perform()
driver.find_element(By.XPATH, '//input[@class="mostra"]').click()
driver.find_element(By.XPATH, '//*[contains(text(),"Copia como .CSV")]').click()

