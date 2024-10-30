from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import json  

# Inicializa o navegador
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Dicionário para armazenar os dados
data = {}

try:
    # Acessa a página do produto
    driver.get("https://www.magazineluiza.com.br/apple-iphone-16-128gb-preto-61-48mp-ios-5g/p/238720700/te/ip16/")

    # Aguarda a página carregar completamente
    time.sleep(5)  # ajuste o tempo de espera conforme necessário
    
    # Obtém o valor do primeiro XPath
    titulo = driver.find_element(By.XPATH, '//*[@id="__next"]/div/main/section[5]/div/h1').text
    data['titulo'] = titulo  # Armazena no dicionário

    # Obtém o valor do segundo XPath
    preco = driver.find_element(By.XPATH, '//*[@id="__next"]/div/main/section[7]/div[6]/div[1]/div/div/div/p').text
    data['preco'] = preco  # Armazena no dicionário

    # estoque = driver.find_element(By.XPATH, '//*[@id="__next"]/div/main/section[7]/div[6]/div[1]/div/div/div/p').text
    # data['estoque'] = estoque  # Armazena no dicionário


except Exception as e:
    print("Ocorreu um erro:", e)

finally:
    # Fecha o navegador
    driver.quit()

# Converte o dicionário para JSON
json_data = json.dumps(data, ensure_ascii=False, indent=4)  # `ensure_ascii=False` para suportar caracteres especiais
print("Dados em JSON:")
print(json_data)  # Imprime o JSON formatado
