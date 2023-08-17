codigo =input("Digiteo codigo do produto: ")
quantidade = int(input("Digite a quantidade de produtos: "))

#codigo_item =["1","2","3","4","5"]
#preco_item = [0.20,2.55,6.23,44.2,98.0]

#preco = preco_item[codigo - 1]
#preco_total = preco * quantidade

produto = {'1' : 0.20,
           '2' : 2.55,
           '3' : 6.23,
           '4' : 44.2,
           '5' : 98.0,}
print(produto[codigo]*quantidade)
#preco_total = produto[codigo] *quantidade
#print(f"preco item {preco_total:.2f}")

