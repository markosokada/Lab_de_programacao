print("Escreva um programa que pergunte o depósito inicial e a taxa de juros de uma poupança. Exiba os valores mês ")
print("a mês para os 24 primeiros meses. Escreva o total ganho com juros no período.")

deposito = float(input("Deposito inicial = "))
taxa_juros = float(input("Taxa de juros (%)= "))
taxa_juros = taxa_juros/100

conta_poupanca = deposito
print("Saldo em Conta Poupança = R$ ", conta_poupanca)
ganho = 0
for i in range(1,4):
    ganho += conta_poupanca * taxa_juros
    conta_poupanca = conta_poupanca + ganho
    print("Rendimento do mês {} foi igual a R$ {:.2f}".format(i, conta_poupanca))
    novo_deposito = float(input("Qual o valor que deseja depositar? R$ "))
    conta_poupanca = conta_poupanca + novo_deposito

print("Total ganho com os juros = R$ {:.2f} ".format(ganho))
print("Saldo Conta = ", conta_poupanca)