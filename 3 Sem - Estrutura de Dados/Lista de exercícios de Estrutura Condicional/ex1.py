#1. Elaborar um algoritmo que lê 3 valores a,b,c e os escreve. 
# A seguir, encontre o maior dos 3 valores e o escreva com 
# a mensagem : "É o maior ".

valA = int(input("Digite o Primeiro Valor: "))
valB = int(input("Digite o Segundo Valor: "))
valC = int(input("Digite o Terceiro Valor: "))

print(f"Os valores são: \n1º Valor: {valA} \n2º Valor: {valB} \n3º Valor: {valC}")

maior = max(valA, valB, valC)
if maior == valA:
    pos = "1º"
elif maior == valB:
    pos = "2º"
else:
    pos = "3º"

print(f" O maior valor é o {pos}: {maior}!")