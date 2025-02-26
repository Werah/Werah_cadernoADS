matriz = []
for i in range(3):
    linha = []
    for j in range(3):
        linha.append((int(input(f"Digite o {j+1}º valor da {i+1}ª linha: "))))
    matriz.append(linha)
for linha in matriz:
    print(linha,"")
soma = matriz[0][0] + matriz[1][1] + matriz[2][2]
print(f"Soma diagonal: {soma}")