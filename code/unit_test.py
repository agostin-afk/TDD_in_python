import unittest
def soma(x, y):
    return x+y

class TestCalculadora(unittest.TestCase):
    def test_soma_5_e_5_retorna_10(self):
        self.assertEqual(soma(5,5), 10)
unittest.main()