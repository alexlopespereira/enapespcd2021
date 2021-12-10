from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


options = Options()
options.add_experimental_option("prefs", {
  "download.default_directory": r"C:\Users\alex\temp",
  "download.prompt_for_download": False,
})
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)


url='http://tabnet.datasus.gov.br/cgi/tabcgi.exe?sih/cnv/qgbr.def'
driver.get(url)
lista_anos = driver.find_element(By.XPATH, f'//select[@id="A"]').text.split('\n')
for m in lista_anos:
    driver.get(url)
    selected_mes = driver.find_element(By.XPATH, f'//select[@id="A"]/option[@selected]')
    selected_mes.click()
    to_select_mes = driver.find_element(By.XPATH, f'//select[@id="A"]/option[contains(text(),"{m}")]')
    to_select_mes.click()
    for i in range(2, 16):
        to_select_conteudo = driver.find_element(By.XPATH, f'//select[@id="I"]/option[{i}]')
        ActionChains(driver).key_down(Keys.CONTROL).click(to_select_conteudo).key_up(Keys.CONTROL).perform()
    driver.find_element(By.XPATH, '//input[@class="mostra"]').click()
    driver.find_element(By.XPATH, '//*[contains(text(),"Copia como .CSV")]').click()

