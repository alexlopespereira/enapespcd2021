from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()
options.add_experimental_option("prefs", {
  "download.default_directory": r"C:\Users\alex\temp",
  "download.prompt_for_download": False,
})
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

url = 'http://tabnet.datasus.gov.br/cgi/tabcgi.exe?sih/cnv/qgbr.def'
driver.get(url)

driver.find_element(By.XPATH, '//input[@class="mostra"]').click()
driver.find_element(By.XPATH, '//*[contains(text(),"Copia como .CSV")]').click()
print(url)
