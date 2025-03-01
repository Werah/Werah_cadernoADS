# Um vendedor necessita de um algoritmo que calcule o preço total devido por um cliente.
# O algoritmo deve receber o código de um produto e a qtd comprada e calcular o preço total,
#usando a tabela abaixo:
#
# Código do Produto Preço unitário
# 1001              5,32
# 1324              6,45
# 6548              2,37
# 0987              5,32
# 7623              6,45

codigo = int(input("Digite o código do produto: "))

if codigo == 1001:
    prec = 5.32
elif codigo == 1324:
    prec = 6.45
elif codigo == 6548:
    prec = 2.37
elif codigo == 987:
    prec = 5.32
elif codigo == 7623:
    prec = 6.45
else:
    print("Código do produto inválido!")
print(f"Preço do produto escolhido: {prec}")
qtd = int(input("Digite a quantidade comprada: "))

precFinal = qtd * prec
print(f"Preço total a pagar: R${precFinal:.2f}")