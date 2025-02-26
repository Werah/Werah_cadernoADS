divd = int(input("Digite o valor da dívida: "))
parc = int(input("Digite a quantidade de parcelas: "))
cont = 1
juros = 0

while cont <= parc:
    if (cont % 3 == 0 and juros == 0):
        juros = juros + 0.1
    elif (cont % 3 == 0 ):
        juros = juros + 0.05
    divdFinal = divd + divd*juros
    valorParc = divd/cont
    jurosFinal = juros*100
    print(divdFinal, " // ", jurosFinal, " // ", cont, " // ", valorParc)
    cont += 1
