print("Faça um algoritmo para ler o salário de todos os funcionários de uma empresa, e aplique um aumento de ")
print("15%. Após esse aumento, desconte 8% de impostos. Imprima o salário inicial, o salário com o aumento e o ")
print("salário final de cada funcionário.")

funcionarios=int(input("informe quantos funcioanários tem a empresa "))

for i in range(funcionarios):
    nome_funci =input("informe o nome dofuncionário ")
    salario_antigo = float(input("Entre com seu salarío atual = "))
    porc_aumento = float(input("Entre com a % de aumento no salário = "))
    porc_imposto = float(input("Entre com o imposto a ser descontado (%) = "))
    aumento = salario_antigo * (porc_aumento/100)
    print("O funcionário ",nome_funci," terá um aumento de R$",aumento)
    salario_novo = salario_antigo + aumento
    print("O funcionário ",nome_funci," receberá o salário com aumento de 15% é de R$", salario_novo)
    desconto = salario_novo * (porc_imposto/100)
    print("Foi descontado de ", nome_funci, "R$", desconto, "de seu salário novo")
    salario_pos_desconto = salario_novo - desconto
    print(nome_funci," seu salário final ficou em R$", salario_pos_desconto)