import unittest
import sys
import os
import time

# Adiciona o diretório atual ao path
sys.path.append(os.path.dirname(__file__))

from test_funcoes import TestFuncoesMatematicas

class TestRunner:
    """Runner personalizado para executar testes"""
    
    def __init__(self):
        self.loader = unittest.TestLoader()
        self.suite = unittest.TestSuite()
    
    def carregar_todos_testes(self):
        """Carrega todos os testes do módulo test_funcoes"""
        try:
            testes = self.loader.loadTestsFromTestCase(TestFuncoesMatematicas)
            self.suite.addTests(testes)  # CORREÇÃO: usar addTests em vez de addTest
            return True
        except Exception as e:
            print(f"❌ Erro ao carregar testes: {e}")
            return False
    
    def carregar_testes_especificos(self, nomes_testes):
        """Carrega testes específicos por nome"""
        try:
            for nome in nomes_testes:
                teste = TestFuncoesMatematicas(nome)
                self.suite.addTest(teste)
            return True
        except Exception as e:
            print(f"❌ Erro ao carregar testes específicos: {e}")
            return False
    
    def executar_testes(self, verbosity=2):
        """Executa os testes e retorna os resultados"""
        print("🧪 INICIANDO TESTES AUTOMATIZADOS")
        print("=" * 50)
        
        if self.suite.countTestCases() == 0:
            print("⚠️  Nenhum teste para executar!")
            return None
        
        start_time = time.time()
        runner = unittest.TextTestRunner(verbosity=verbosity)
        result = runner.run(self.suite)
        end_time = time.time()
        
        print("=" * 50)
        print(f"⏱️  Tempo de execução: {end_time - start_time:.2f} segundos")
        print(f"📊 Total de testes: {result.testsRun}")
        print(f"✅ Testes passados: {result.testsRun - len(result.failures) - len(result.errors)}")
        print(f"❌ Testes falhados: {len(result.failures)}")
        print(f"🚫 Erros: {len(result.errors)}")
        
        return result