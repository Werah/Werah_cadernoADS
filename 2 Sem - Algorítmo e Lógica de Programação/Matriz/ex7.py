matriz = []
resultado = []
for i in range(5):
    linha = []
    for j in range (2):
        valor = (input(f"Digite o {j+1}º valor da {i+1}ª linha: "))
        linha.append(int(valor))
    matriz.append(linha)
    soma = linha[0] + linha [1]
    resultado.append(soma)
for i in range(len(matriz)):
    print(f"linha {i+1}: {matriz[i]}, Soma: {resultado[i]}")
somaR = 0
for i in range(len(resultado)):
    somaR = somaR + resultado[i]
print(f"Soma total: {somaR}")