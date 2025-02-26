lista = []
listaPar = []
listaImpar = []
continuar = ""

while continuar.lower() != "n":
    valor = (int(input("Digite um valor: ")))
    if valor in lista:
        print("Valor já esta na lista")
    else:
        lista.append(valor)
        print("Valor adicionado com sucesso!")
        if valor %2 == 0:
            listaPar.append(valor)
        else:
            listaImpar.append(valor)
    
    continuar = input("Deseja continuar? [S/N]")

print(sorted(lista))
print(sorted(listaPar))
print(sorted(listaImpar))