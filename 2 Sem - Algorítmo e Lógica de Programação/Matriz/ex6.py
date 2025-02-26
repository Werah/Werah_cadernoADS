import random
matriz = []
for i in range(4):
    linha = []
    for j in range(4):
        linha.append(random.randint(0,100))
    matriz.append(linha)
    
for linha in matriz:
    print(linha,"")