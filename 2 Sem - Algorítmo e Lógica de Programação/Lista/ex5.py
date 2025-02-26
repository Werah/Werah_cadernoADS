pessoa = []
cliente = []
for i in range (0,2):
    pessoa.append(str(input("Digite o nome do cliente: ")))
    pessoa.append(int(input("Digite a idade do cliente: ")))
    cliente.append(pessoa[:])
    pessoa.clear()
print(cliente)
contMenor = 0 
contMaior = 0
nome = 0
for i in cliente:
    if cliente[nome][1] < 18:
        print(f"{cliente[nome][0]} é menor de idade!")
        contMenor += 1
    else:
        print(f"{cliente[nome][0]} é maior de idade!")
        contMaior += 1
    nome += 1
print(f"Na lista tem {contMaior} maior(es), e {contMenor} menor(es) de idade")