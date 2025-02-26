n = int(input("Digite um número: "))
cont = 1
fatCont = 1
fatRes = cont
for i in range (n+1):
    for i in range (cont+1):
        fatRes = cont
        fatRes = fatCont * fatRes
        fatRes += 1
    e = cont + cont/fatRes
    cont +=1
    print (f"{e} E, {cont}")
