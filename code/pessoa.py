import requests

class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome
        self.dados_obtidos = False
        
    def obter_todos_o_dados(self):
        resposta = requests.get('https://httpbin.org/get')
        if resposta.ok:
            self.dados_obtidos = True
            return 'CONECTADO'
        else:
            return 'ERRO 404'