print("A granja Frangotech possui um controle automatizado de cada frango da sua produção. No pé direito do frango ")
print("há um anel com um chip de identificação; no pé esquerdo são dois anéis para indicar o tipo de ")
print("alimento que ele deve consumir. Sabendo que o anel com chip custa R$4,00 e o anel de alimento custa R$3,50, e ")
print("o quilo da ração é diferente para cada tipo. A diversidade de tipos de rações disponíveis depende do ")
print("fazendeiro. Cada tipo favorece um aumento de uma porcentagem do quilo do frango (exemplo: TIPO A = 20%, ")
print("TIPO B = 14%). Faça um algoritmo para calcular o gasto total da granja com ração e anéis, e quanto o ")
print("fazendeiro irá faturar com os frangos.")

galinhas = int(input("Informe quantas galinhas serão marcadas? "))
id_ring = float(input("Qual o preco do anel de identificação "))
alimento_ring = float(input("Qual o preco do anel dealimento? "))

print("O custo para marcar todas as galinhas é de: R$ ", galinhas * ((2 * alimento_ring)+id_ring))

tipo_racao = input("Informe o tipode raçao \n se tipo A,ou tipo B: ")
preco_racao=float(input("Informe o preço do kilo da ração: "))
kilo_galinha = float(input("Informe com quantos kilos essa galinha será abatida?: "))
preco_kilo = float(input("Informe o preço do kilo da galinha: "))

if tipo_racao == "A":
    print("O preço final de cada galinha é de R$: ",kilo_galinha*preco_kilo*1.20)
elif tipo_racao =="B":
    print("O preço final de cada galinha é de R$: ",kilo_galinha*preco_kilo*1.14)



