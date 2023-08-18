
print("A granja Frangotech possui um controle automatizado de cada frango da sua produção. No pé direito do frango")
print("há um anel com um chip de identificação; no pé esquerdo são dois anéis para indicar o tipo de")
print("alimento que ele deve consumir. Sabendo que o anel com chip custa R$4,00 e o anel de alimento custa R$3,50,")
print("faça um algoritmo para calcular o gasto total da granja para marcar todos os seus frangos.")

galinhas = int(input("Informe quantas galinhas serão marcadas? "))
id_ring = float(input("qual o preco do anel de identificação "))
alimento_ring = float(input("Qual o preco do anel dealimento? "))

print("O custo para marcar todas as galinhas é de: R$ ", galinhas * ((2 * alimento_ring)+id_ring))