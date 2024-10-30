import unittest
from .calcula_media import calcular_media
from .calcula_media_refatorado import calcular_media_refatorado


# Fase Red (Escrita dos Testes)

class TestCalcularMedia(unittest.TestCase):
    def test_todas_notas_zero(self):
        self.assertEqual(calcular_media(0, 0, 0), 0)
    
    def test_notas_maximas(self):
        self.assertEqual(calcular_media(10, 10, 10), 10)
        self.assertEqual(calcular_media(10, 5, 0), 5)
    
    def test_notas_decimais(self):
        self.assertAlmostEqual(calcular_media(7.5, 8.3, 9.2), 8.33333, places=5)
        
        
class TestCalcularMediaRefatorado(unittest.TestCase):
    def test_todas_notas_zero(self):
        self.assertEqual(calcular_media_refatorado(0, 0, 0), 0)
    
    def test_notas_maximas(self):
        self.assertEqual(calcular_media_refatorado(10, 10, 10), 10)
        self.assertEqual(calcular_media_refatorado(10, 5, 0), 5)
    
    def test_notas_decimais(self):
        self.assertAlmostEqual(calcular_media_refatorado(7.5, 8.3, 9.2), 8.33333, places=5)

    # Teste novo: notas negativas devem levantar ValueError
    def test_notas_negativas(self):
        with self.assertRaises(ValueError):
            calcular_media_refatorado(-1, 5, 6)

    # Teste novo: entradas que não são números devem levantar ValueError
    def test_notas_nao_numericas(self):
        with self.assertRaises(ValueError):
            calcular_media_refatorado('dez', 7, 8)

    # Teste novo: combinação de valores válidos e inválidos
    def test_combinacao_valores_invalidos(self):
        with self.assertRaises(ValueError):
            calcular_media_refatorado(10, -5, 'cinco')

if __name__ == '__main__':
    unittest.main()
