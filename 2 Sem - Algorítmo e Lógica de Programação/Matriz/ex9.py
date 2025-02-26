def criaMatriz(nome):
    matriz = []
    for i in range(2):
        linha = []
        for j in range(2):
            valor = (int(input(f"Digite o {j+1}º valor da {i+1}ª linha: ")))
            linha.append(valor)
        matriz.append(linha)
    
    variavel[nome] = matriz
variavel = {}

criaMatriz("matriz1")
print("\nMatriz 1: ")
for linha in variavel["matriz1"]:
    print(linha)

criaMatriz("matriz2")
print("\nMatriz 2: ")
for linha in variavel["matriz2"]:
    print(linha)

resultado = [[0, 0], [0, 0]]

for i in range(2):
    for j in range(2):
        resultado[i][j] = variavel["matriz1"][i][j] + variavel["matriz2"][i][j]

print("\nMatriz resultado:")
for linha in resultado:
    print(linha)