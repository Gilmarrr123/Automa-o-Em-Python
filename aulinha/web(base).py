from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
from time import sleep
import os

# Configuração do WebDriver para o firefox (certificar se o geckodriver está instalado)
driver = webdriver.Firefox()

# Abre o Site
driver.get('https://imoveisfranca.com.br/resultadoBusca/alugar&tipo=alugar')

# Clicar no botão de CRM
clicar_crm = driver.find_element(By.XPATH, '//*[@id="resultado-busca"]/div/div/div[2]/div[2]/div/div[3]/div/div[2]/a/h5').text
print(clicar_crm)
