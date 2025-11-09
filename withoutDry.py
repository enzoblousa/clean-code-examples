# Código com repetição - VIOLANDO DRY
def calcular_area_quadrado(lado):
    area = lado * lado
    print(f"A área do quadrado é: {area}")
    return area

def calcular_area_retangulo(largura, altura):
    area = largura * altura
    print(f"A área do retângulo é: {area}")
    return area

def calcular_area_triangulo(base, altura):
    area = (base * altura) / 2
    print(f"A área do triângulo é: {area}")
    return area

# Usando as funções
calcular_area_quadrado(5)
calcular_area_retangulo(4, 6)
calcular_area_triangulo(3, 8)