lista = []
continuar = ""

while continuar.lower() != "n":
    valor = (int(input("Digite um valor: ")))
    if valor in lista:
        print("Valor já esta na lista")
    else:
        lista.append(valor)
        print("Valor adicionado com sucesso!")
    
    continuar = input("Deseja continuar? [S/N]")

print(sorted(lista))