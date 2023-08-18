print("A imobiliária Imóbilis vende apenas terrenos\n retangulares. Faça um algoritmo para ler as\n dimensões de um terreno e depois exibir a\n área do terreno.")

x_string = input("Escreva o valor de X \n")
x_float = float(x_string)
#
y_string = input("Escreva o valor de Y \n")
y_float = float(y_string)

area = x_float * y_float
print("o terreno tem ",area,"metros quadrados")