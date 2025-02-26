import random

lista = [random.randint(0,100) for i in range(5)]
maior = lista[0]
menor = lista[0]
for i in lista:
    if i > maior:
        maior = i
    if i < menor:
        menor = i
tuplaLista = tuple(lista)

print(tuplaLista)
print(f"O maior número é: {maior}")
print(f"O menor número é: {menor}")
