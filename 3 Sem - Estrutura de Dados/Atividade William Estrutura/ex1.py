#1. Fazer um programa em python que pergunta um valor em metros e imprime o
#correspondente em decímetros, centímetros e milímetros. ( utilize até duas casas
#decimais para apresentar os numeros)

# Solicita ao usuário um valor em metros
metros = float(input("Digite um valor em metros: "))

# Converta para outras unidades
decimetros = metros * 10
centimetros = metros * 100
milimetros = metros * 1000

# Exibe os resultados com duas casas decimais
print(f"{metros:.2f} metros equivalem a:")
print(f"{decimetros:.2f} decímetros")
print(f"{centimetros:.2f} centímetros")
print(f"{milimetros:.2f} milímetros")