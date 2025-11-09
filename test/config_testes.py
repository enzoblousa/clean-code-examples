# salvar como: config_testes.py
class ConfigTestes:
    """Configurações para o ambiente de testes"""
    
    # Configurações de verbosidade
    VERBOSIDADE = 2  # 0 = mínimo, 1 = normal, 2 = detalhado
    
    # Timeout para testes (em segundos)
    TIMEOUT_TESTES = 30
    
    # Configurações de relatório
    GERAR_RELATORIO = True
    NOME_ARQUIVO_RELATORIO = "relatorio_testes.txt"
    
    @classmethod
    def mostrar_configuracoes(cls):
        """Mostra as configurações atuais"""
        print("\n⚙️ CONFIGURAÇÕES DO AMBIENTE DE TESTES")
        print(f"Verbosidade: {cls.VERBOSIDADE}")
        print(f"Timeout: {cls.TIMEOUT_TESTES}s")
        print(f"Gerar relatório: {cls.GERAR_RELATORIO}")