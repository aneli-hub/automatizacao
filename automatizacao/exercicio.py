
import requests

from bs4 import BeautifulSoup 

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
}
url = "https://www.sohistoria.com.br/ef2/periodos/"

resposta = requests.get(url, headers=headers)

if resposta.status_code == 200:
    print("requisição bem sucedida")
# 200 -> ok    

soup = BeautifulSoup(resposta.text, "html.parser")

noticias = soup.find_all("p", class_="justificado")

print("últimas notícias:")
for noticia in noticias:
    print(f'({noticia.text})')
