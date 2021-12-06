from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(ChromeDriverManager().install())


url='http://tabnet.datasus.gov.br/cgi/tabcgi.exe?sih/cnv/qgbr.def'

for m in range(1, 166):
    driver.get(url)
    to_select_mes = driver.find_element(By.XPATH, f'//select[@id="A"]/option[{m}]')
    if m > 1:
        driver.find_element(By.XPATH, f'//select[@id="A"]/option[{m-1}]').click()
        to_select_mes.click()

    for i in range(2, 16):
        to_select_conteudo = driver.find_element(By.XPATH, f'//select[@id="I"]/option[{i}]')
        ActionChains(driver).key_down(Keys.CONTROL).click(to_select_conteudo).key_up(Keys.CONTROL).perform()
    driver.find_element(By.XPATH, '//input[@class="mostra"]').click()
    driver.find_element(By.XPATH, '//*[contains(text(),"Copia como .CSV")]').click()
    print(to_select_mes.text)
