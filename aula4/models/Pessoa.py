
class Pessoa:
    #definição
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha

    def cadastrar(self):
        print("cadastrando pesssoa....")
    
    def sair(self):
        print("saindo do sistema....")