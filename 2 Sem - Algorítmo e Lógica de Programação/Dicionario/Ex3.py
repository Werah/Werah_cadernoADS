estados = []
for i in range(0, 3):
    est = {}
    est['uf'] = str(input("Digite o nome do Estado: "))
    est['sigla'] = str(input("Digite a sigla do Estado: "))
    estados.append(est)
    
for estado in estados:
    print('UF: ', estado['uf'], ' Sigla: ', estado['sigla'])

