num = int(input("Digite um número: "))
cont = 1
prim = 0
while cont < num:
    soma = num % cont
    if soma == 0:
        prim += 1
    cont +=1
if prim < 2:
    print("O número é primo!")
else:
    print("O número é não é primo!")