# pip install selenium
# pip install webdriver-manager
from selenium import webdriver  
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# configurar navegador
options = webdriver.ChromeOptions()

#mascarar que não somos uma automação
options.add_argument('disable-blink-features=AutomationControlled')

#mascarar o Useragent que vai acessar o site
options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (kHTML, like Gecko)')


#https://abre.ai/configuracaoagent
driver = webdriver.Chrome(options=options)

url = "https://www.webmotors.com.br/carros/sp-cotia/volkswagen/golf?topoveiculo=carros" 


#slenium acessa o site
driver.get(url)

time.sleep(5) # esperar 5 seg para carregar o site

#extrair os dados

carros = driver.find_elements(By.CLASS_NAME, "_container_70j0p_1")
for carro in carros:
    nome = carro.find_element(By.CLASS_NAME, "_web-title-medium_qtpsh_51").text
    preco = carro.find_element(By.CLASS_NAME, "_body-bold-large_qtpsh_78").text

    print(f'nome do carro: {nome}')
    print(f'preço do carro: {preco}')
   