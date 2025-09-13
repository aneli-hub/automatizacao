# Biblioteca de requisições 
import requests
# Responsável por tratar o retorno
from bs4 import BeautifulSoup 

# pip install requests
# pip install bs4

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
}
url = "https://g1.globo.com/"

# fazendo requisição http
resposta = requests.get(url, headers=headers)

# verificar se deu certo 
if resposta.status_code == 200:
    print("requisição bem sucedida")
# 200 -> ok    

# traduzir a resposta do site
soup = BeautifulSoup(resposta.text, "html.parser")

# recortar a informação que queremos
noticias = soup.find_all("a", class_="feed-post-link")

print("últimas notícias:")
for noticia in noticias:
    print(f'({noticia.text}) - ({noticia["href"]})')
