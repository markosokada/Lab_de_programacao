print("A imobiliária Imóbilis vende terrenos irregulares de 5 lados. \nCada de acordo com a região, o valor do metro\n quadrado altera, no centro é de R$ 130, em área nobre é \nde R$ 200, e na periferia é igual a R$ 80.\nFaça um algoritmo que calcule o preço e a área total do terreno.")

regiao = int(input("informe em qual setor se encontra o terreno\n 1) Para o centro \n 2) Para parte nobre \n 3) Para periferia "))

lateral_terreno = float(input("quantos metros tem alateral do terreno?"))
apotamo = float(input("qual o comprimento do apotamo?"))

area_pentagono = (0.5*lateral_terreno*apotamo*5)

if regiao == 1:
    print("esse terreno vale ",area_pentagono*130, "reais")
elif regiao == 2:
    print("esse terreno vale ",area_pentagono*200, "reais")
elif regiao == 3:
    print("esse terreno vale ",area_pentagono*80, "reais")
else:
    print("nao achei essa regiao")



print("area do pentagono é de ",area_pentagono,"metros quadrados")