'''Exercício Intermediário
2. Crie uma matriz 3x3 com valores digitados pelo usuário. Em seguida, calcule e exiba:
- A soma de todos os elementos
- A média dos elementos
- Os valores da diagonal principal'''

matriz = []
cont = 1
for i in range(3):
    linha = []
    for j in range(3):
        valor = int(input(f"Digite o {cont}º valor: "))
        linha.append(valor)
        cont+=1
    matriz.append(linha)

for linha in matriz:
    print(linha)

print(f"Soma: {sum(sum(linha) for linha in matriz)}")

diagonal = []
for i in range(len(matriz)):
    diagonal.append(matriz[i][i])
print(f"Diagonal: {diagonal}")