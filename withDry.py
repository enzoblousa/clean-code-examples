# Código seguindo DRY - sem repetição

def calcular_area_quadrado(lado):
    area = lado * lado
    mostrar_resultado("quadrado", area)
    return area

def calcular_area_retangulo(largura, altura):
    area = largura * altura
    mostrar_resultado("retângulo", area)
    return area

def calcular_area_triangulo(base, altura):
    area = (base * altura) / 2
    mostrar_resultado("triângulo", area)
    return area

    #Função única para mostrar resultados
def mostrar_resultado(forma, area):
    print(f"A área do {forma} é: {area}")
    
# Usando as funções
calcular_area_quadrado(5)
calcular_area_retangulo(4, 6)
calcular_area_triangulo(3, 8)