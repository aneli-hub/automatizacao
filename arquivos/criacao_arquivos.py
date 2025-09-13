import csv # xlsx -> csv

# criando arquivo csv

# gerando dados 
dados = [
    ['nome', 'idade', 'cidade'],
    ['João', 25, 'São Paulo'],
    ['Maria', 30, 'Rio de Janeiro'],
    ['Pedro', 22, 'Belo Horizonte']
]

# CRIAR CSV
# nomeArquivo, WHITE, novaLinha, Codificação Br - UTF8
with open('dados.csv', 'w', newline='', encoding='utf-8') as csvarquivo:
   escritor = csv.writer(csvarquivo)
   escritor.writerows(dados) # escrever várias linhas

# LER CSV
with open('dados.csv', 'r', encoding='utf-8') as csvarquivo:
    leitor = csv.reader(csvarquivo)
    for linha in leitor:
        print(linha)
