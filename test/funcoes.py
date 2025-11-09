def soma(a, b):
    """Soma dois números"""
    return a + b

def subtracao(a, b):
    """Subtrai dois números"""
    return a - b

def multiplicacao(a, b):
    """Multiplica dois números"""
    return a * b

def divisao(a, b):
    """Divide dois números"""
    if b == 0:
        raise ValueError("Não é possível dividir por zero!")
    return a / b

def eh_par(numero):
    """Verifica se um número é par"""
    return numero % 2 == 0

def fatorial(n):
    """Calcula o fatorial de um número"""
    if n < 0:
        raise ValueError("Fatorial não definido para números negativos")
    if n == 0 or n == 1:
        return 1
    return n * fatorial(n - 1)