cont = 1
maior = 0
menor = 9999999999
for x in range(5):
    nomeCid = input(f"Insira o nome da cidade {cont}: ")
    qtdVeic = int(input(f"Insira o número de veículos que {nomeCid} possuia em 1999: "))
    qtdAci = int(input(f"Insira o número de acidentes com vítimas que aconteceram em {nomeCid} em 1999: "))
    if qtdAci > maior and qtdAci != maior:
        maior = qtdAci
    if qtdAci < menor and qtdAci != menor:
        menor = qtdAci
    print (maior)
    print (menor)
    cont+=1