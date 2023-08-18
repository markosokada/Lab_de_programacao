print("aça um algoritmo para ler o salário de um funcionário \ne aumentá-lo em 15%. Após o aumento,")
print("desconte 8% de impostos. Imprima o salário inicial, \no salário com o aumento e o salário final.")")

salario_antigo = float(input("Entre com seu salarío atual = "))
porc_aumento = float(input("Entre com a % de aumento no salário = "))
porc_imposto = float(input("Entre com o imposto a ser descontado (%) = "))
aumento = salario_antigo * (porc_aumento/100)
print("Um aumento de R$",aumento)
salario_novo = salario_antigo + aumento
print("Seu salário com aumento de 15% é de R$", salario_novo)
desconto = salario_novo * (porc_imposto/100)
print("Foi descontado R$", desconto, "de seu salário novo")
salario_pos_desconto = salario_novo - desconto
print("Seu salário final ficou em R$", salario_pos_desconto)