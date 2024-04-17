from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
from time import sleep
import os


driver = webdriver.Firefox()

driver.get('https://imoveisfranca.com.br/resultadoBusca/alugar&tipo=alugar')


clicar_crm = driver.find_element(By.XPATH, '//*[@id="resultado-busca"]/div/div/div[2]/div[2]/div/div[3]/div/div[2]/a/h5').text
print(clicar_crm)