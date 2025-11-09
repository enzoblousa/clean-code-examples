#função que calcula a área de um círculo baseado no valor da variável radius
def calculate_circle_area(radius):
    pi = 3.14
    #fórmula area de um círculo
    circle_area_formula = pi * pow(radius, 2) #multiplica pi pelo raio ao quadrado
    #pega o resultado obtido e passa para uma variável chamda resultado
    resultado = circle_area_formula
    return resultado

#função dedicada apenas para mostrar o valor da área de um circulo
def showresult(resultado):
    print(resultado)

#valor do raio
radius = 10
#a área do círculo é passada para a var circle_area
circle_area = calculate_circle_area(radius)
#mostra o resultado
showresult(circle_area)











