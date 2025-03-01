# 7. Escrever um algoritmo que lê um conjunto de 4 valores i, a, b, c, onde i é um valor inteiro e positivo
# e a, b, c são quaisquer valores reais e os escreva. A seguir:
# a) Se i=1 escrever os três valores a, b, c em ordem crescente.
# b) Se i=2 escrever os três valores a, b, c em ordem decrescente.
# c) Se i=3 escrever os três valores a, b, c de forma que o maior entre a, b, c fique dentre os dois.

i = int(input("Digite o valor de i (1 Crescente, 2 Decrescente ou 3 Maior no meio): "))
a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

print(f"Valores lidos: i = {i}, a = {a}, b = {b}, c = {c}")

if i == 1:
    val = sorted([a, b, c])
    print(f"Valores em ordem crescente: {val[0]}, {val[1]}, {val[2]}")
elif i == 2:
    val = sorted([a, b, c], reverse=True)
    print(f"Valores em ordem decrescente: {val[0]}, {val[1]}, {val[2]}")
elif i == 3:
    maior = max(a, b, c)
    menor = min(a, b, c)
    meio = (a + b + c) - maior - menor
    print(f"Valores com o maior no meio: {menor}, {maior}, {meio}")
else:
    print("Valor de i inválido! Digite 1, 2 ou 3.")