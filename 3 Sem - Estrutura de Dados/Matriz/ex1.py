'''Exercício Fácil
1. Crie uma matriz 2x2. Peça ao usuário para digitar os 4 valores da matriz. Ao final, exiba a matriz linha por
linha.'''

matriz = []
cont = 1
for i in range(2):
    linha = []
    for j in range(2):
        valor = int(input(f"Digite o {cont}º número: "))
        linha.append(valor)
        cont+=1
    matriz.append(linha)

for linha in matriz:
    print(linha)