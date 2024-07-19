"""
class Pessoa
    __init__
        nome str
        sobrenome str
        dados_obtidos bool
        
    API:
        obter_todos_os_dados -> method
            OK
            404
"""
import unittest
from pessoa import Pessoa
from unittest.mock import patch # Cria dados falsos para testes
class TestPessoa(unittest.TestCase):
    def setUp(self):
        self.p1 = Pessoa('Agostinho', 'Ferreira')
    def test_pessoa_attr_nome_tem_o_valor_correto(self):
        self.assertEqual(self.p1.nome, 'Agostinho')
    def test_pessoa_attr_sobrenome_tem_o_valor_correto(self):
        self.assertEqual(self.p1.sobrenome, 'Ferreira')
    def test_pessoa_attr_dados_obtidos_inicia_falso(self):
        self.assertFalse(self.p1.dados_obtidos)
    def test_pessoa_attr_nome_e_str(self):
        self.assertIsInstance(self.p1.nome, str)
    def test_pessoa_attr_sobrenome_e_str(self):
        self.assertIsInstance(self.p1.nome, str)
    def test_obter_todos_os_dados_sucesso_OK(self):
        with patch('requests.get') as fake_request:
            fake_request.return_value.ok = True
            
            self.assertEqual(self.p1.obter_todos_o_dados(), 'CONECTADO')
    def test_obter_todos_os_dados_falha_404(self):
        with patch('requests.get') as fake_request:
            fake_request.return_value.ok = False
            
if __name__ == '__main__':
    unittest.main(verbosity=2)