import unittest
import sys
import os

# Adiciona o diretório atual ao path para importar módulos
sys.path.append(os.path.dirname(__file__))

from funcoes import soma, subtracao, multiplicacao, divisao, eh_par, fatorial

class TestFuncoesMatematicas(unittest.TestCase):
    """Classe de testes para funções matemáticas"""
    
    def test_soma(self):
        """Testa a função soma"""
        self.assertEqual(soma(2, 3), 5)
        self.assertEqual(soma(-1, 1), 0)
        self.assertEqual(soma(0, 0), 0)
        self.assertEqual(soma(2.5, 3.5), 6.0)
    
    def test_subtracao(self):
        """Testa a função subtração"""
        self.assertEqual(subtracao(5, 3), 2)
        self.assertEqual(subtracao(3, 5), -2)
        self.assertEqual(subtracao(0, 0), 0)
    
    def test_multiplicacao(self):
        """Testa a função multiplicação"""
        self.assertEqual(multiplicacao(3, 4), 12)
        self.assertEqual(multiplicacao(-2, 3), -6)
        self.assertEqual(multiplicacao(0, 5), 0)
    
    def test_divisao(self):
        """Testa a função divisão"""
        self.assertEqual(divisao(10, 2), 5)
        self.assertEqual(divisao(5, 2), 2.5)
        
        # Testa divisão por zero
        with self.assertRaises(ValueError):
            divisao(10, 0)
    
    def test_eh_par(self):
        """Testa a função eh_par"""
        self.assertTrue(eh_par(2))
        self.assertTrue(eh_par(0))
        self.assertTrue(eh_par(-4))
        self.assertFalse(eh_par(3))
        self.assertFalse(eh_par(-7))
    
    def test_fatorial(self):
        """Testa a função fatorial"""
        self.assertEqual(fatorial(0), 1)
        self.assertEqual(fatorial(1), 1)
        self.assertEqual(fatorial(5), 120)
        self.assertEqual(fatorial(3), 6)
        
        # Testa fatorial de número negativo
        with self.assertRaises(ValueError):
            fatorial(-5)