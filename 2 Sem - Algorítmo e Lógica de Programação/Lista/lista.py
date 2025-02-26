lista = [10, 20, 30, 40]
#        0   1   2   3
print(lista)
#[10, 20, 30, 40]

#--------------------------------------------
#Listas são mutáveis, você pode mudar os valores internos
lista[1] = 25
print(lista)
#[10, 25, 30, 40]


#--------------------------------------------
#Inserir novos valores
lista.append(50)
#Se colocar lista[4] = 50, ele vai tentar alcançar o lista[4] e vai dar erro pq n conseguiu alcançar
print(lista)
#[10, 25, 30, 40, 50]

#--------------------------------------------
#Inserir novos valores no meio da lista
lista.insert(1, 15)
print(lista)
#[10, 15, 25, 30, 40, 50]
# 0   1   2   3   4   5

#--------------------------------------------
#Remover valores da lista
lista.remove(50)
print(lista)
#[10, 15, 25, 30, 40]
# 0   1   2   3   4

#--------------------------------------------
#Valores insediros pelo usuário, e contagem de posição
valores = [] #cria uma lista vazia para o usuário preencher
for cont in range(0,5):
    valores.append(int(input("Digite um valor: ")))

for indice, valor in enumerate(valores):
    print(f"Na posição {indice} foi digitado o valor {valor}")
#A função enumerate vai pedir 2 variaveis, a primeira é a posição da lista, e a segunda é o valor referente aquela posição.