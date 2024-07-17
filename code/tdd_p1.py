"""_TDD_
Red:
criar o teste e ver falhar

Green:
criar a função e ver passar

Refatory:
melhorar e refatorar

"""

import unittest
from bacon_com_ovos import *
class TestBaconComOvos(unittest.TestCase):
    def test_bacon_com_ovos_deve_retornar_assert_se_nao_for_int(self):
        with self.assertRaises(AssertionError):
            bacon_com_ovos('')
    def test_bacon_com_ovos_deve_retornar_bacon_com_ovos_se_n_for_divisivel_por_3_e_5(self):
        entradas = (15, 30, 45, 60)
        saida = 'Bacon com ovos'
        for entrada in entradas:
            with self.subTest(entrada=entrada, saida=saida):
                self.assertEqual(bacon_com_ovos(entrada), saida)
    def test_bacon_com_ovos_deve_retornar_passar_fome_se_n_nao_for_divisivel_por_3_e_5(self):
        entradas = (1,2,4,7,8)
        saida = 'Passar fome'
        for entrada in entradas:
            with self.subTest(entrada=entrada, saida=saida):
                self.assertEqual(bacon_com_ovos(entrada), saida)
unittest.main(verbosity=2)