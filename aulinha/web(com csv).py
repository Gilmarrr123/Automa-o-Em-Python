import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
from time import sleep
import os

# Configuração do WebDriver para o Firefox (certificar-se de que o geckodriver está instalado)
driver = webdriver.Firefox()

# Abre o Site
driver.get('https://imoveisfranca.com.br/resultadoBusca/alugar&tipo=alugar')

# Lista para armazenar os dados
data_list = []

# Extrair os dados
clicar_crm = driver.find_element(By.XPATH, '//*[@id="resultado-busca"]/div/div/div[2]/div[2]/div/div[3]/div/div[2]/a/h5').text
bairro = driver.find_element(By.XPATH, '//*[@id="resultado-busca"]/div/div/div[2]/div[2]/div/div[3]/div/div[2]/a/p').text
quartos = driver.find_element(By.XPATH, '//*[@id="resultado-busca"]/div/div/div[2]/div[2]/div/div[3]/div/div[2]/a/div[1]/div[2]/p').text
banheiros = driver.find_element(By.XPATH, '//*[@id="resultado-busca"]/div/div/div[2]/div[2]/div/div[3]/div/div[2]/a/div[1]/div[3]/p').text

# Adicionar os dados à lista
data_list.append([clicar_crm, bairro, quartos, banheiros])

# Criar ou abrir o arquivo CSV
csv_file_path = "dados_imoveis.csv"
with open(csv_file_path, 'w', newline='') as csvfile:
    # Configurar o escritor CSV
    writer = csv.writer(csvfile)
    
    # Escrever os cabeçalhos
    writer.writerow(["Clicar CRM", "Bairro", "Quartos", "Banheiros"])
    
    # Escrever os dados
    writer.writerows(data_list)

print("Dados foram salvos em", csv_file_path)

# Fechar o navegador
driver.quit()
