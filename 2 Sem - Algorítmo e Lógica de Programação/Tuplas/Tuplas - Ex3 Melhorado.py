import random

#lista = [random.randint(0,100) for i in range(5)]
#maior = lista[0]
#menor = lista[0]
#for i in lista:
#    if i > maior:
#        maior = i
#    if i < menor:
#        menor = i
#tuplaLista = tuple(lista)

#print(tuplaLista)
#print(f"O maior número é: {maior}")
#print(f"O menor número é: {menor}")

tupla = ()
for i in range(0,5):
    n = random.randint(1,100)
    tupla = tupla + (n,)
print(f"Números aleatórios: {tupla}")
print(f"Menor Valor: {min(tupla)}")
print(f"Maior Valor: {max(tupla)}")
