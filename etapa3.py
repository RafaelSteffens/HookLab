from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import json  


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


data = {}

try:

    driver.get("https://www.magazineluiza.com.br/apple-iphone-16-128gb-preto-61-48mp-ios-5g/p/238720700/te/ip16/")


    time.sleep(5) 
    

    titulo = driver.find_element(By.XPATH, '//*[@id="__next"]/div/main/section[5]/div/h1').text
    data['titulo'] = titulo 


    preco = driver.find_element(By.XPATH, '//*[@id="__next"]/div/main/section[7]/div[6]/div[1]/div/div/div/p').text
    data['preco'] = preco  #

    # estoque = driver.find_element(By.XPATH, '//*[@id="__next"]/div/main/section[7]/div[6]/div[1]/div/div/div/p').text
    # data['estoque'] = estoque  # Armazena no dicionário


except Exception as e:
    print("Ocorreu um erro:", e)

finally:
    driver.quit()

json_data = json.dumps(data, ensure_ascii=False, indent=4)  
print("Dados em JSON:")
print(json_data) 
