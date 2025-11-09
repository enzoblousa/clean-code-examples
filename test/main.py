import unittest
import sys
import os

# Adiciona o diretório atual ao path
sys.path.append(os.path.dirname(__file__))

def menu_principal():
    """Menu simples para testes"""
    print("\n" + "="*50)
    print("🧪 SISTEMA DE TESTES AUTOMATIZADOS")
    print("="*50)
    print("1. Executar TODOS os testes")
    print("2. Executar testes específicos")
    print("3. Sair")
    print("="*50)
    
    return input("Escolha uma opção (1-3): ")

def executar_todos_testes():
    """Executa todos os testes"""
    print("\n🚀 Executando TODOS os testes...")
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromName('test_funcoes')
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Mostrar resumo
    print(f"\n📊 RESUMO: {result.testsRun} testes executados")
    print(f"✅ Passaram: {result.testsRun - len(result.failures) - len(result.errors)}")
    print(f"❌ Falharam: {len(result.failures)}")
    print(f"🚫 Erros: {len(result.errors)}")

def executar_testes_especificos():
    """Executa testes específicos"""
    print("\n🎯 Testes disponíveis:")
    testes_disponiveis = [
        "test_soma", "test_subtracao", "test_multiplicacao",
        "test_divisao", "test_eh_par", "test_fatorial"
    ]
    
    for i, teste in enumerate(testes_disponiveis, 1):
        print(f" {i}. {teste}")
    
    try:
        opcao = input("\nDigite os números dos testes (ex: 1,3,5): ")
        numeros = [int(x.strip()) for x in opcao.split(",") if x.strip()]
        
        testes_selecionados = []
        for num in numeros:
            if 1 <= num <= len(testes_disponiveis):
                testes_selecionados.append(testes_disponiveis[num-1])
        
        if testes_selecionados:
            print(f"\n🔧 Executando: {', '.join(testes_selecionados)}")
            
            # Carregar e executar testes específicos
            loader = unittest.TestLoader()
            suite = unittest.TestSuite()
            
            for teste_nome in testes_selecionados:
                suite.addTest(loader.loadTestsFromName(f'test_funcoes.TestFuncoesMatematicas.{teste_nome}'))
            
            runner = unittest.TextTestRunner(verbosity=2)
            result = runner.run(suite)
            
            print(f"\n📊 RESUMO: {result.testsRun} testes executados")
        else:
            print("❌ Nenhum teste válido selecionado!")
            
    except ValueError:
        print("❌ Entrada inválida! Use números separados por vírgula.")

def main():
    """Função principal"""
    while True:
        opcao = menu_principal()
        
        if opcao == "1":
            executar_todos_testes()
        elif opcao == "2":
            executar_testes_especificos()
        elif opcao == "3":
            print("👋 Saindo... Até logo!")
            break
        else:
            print("❌ Opção inválida! Tente 1, 2 ou 3.")

if __name__ == "__main__":
    main()