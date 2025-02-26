tupla = ()
pares = []
for i in range(0,3):
    num = int(input(f"Digite o {i+1} valor: "))
    tupla = tupla + (num,)
    if num % 2 == 0:
        pares.append(tupla[i])
print(tupla)
if 9 in tupla:
    print(f"O nove aparece {tupla.count(9)} vez(es)!")
else:
    print("O 9 não foi digitado!")
if 3 in tupla:
    print(f"O 3 aparece pela 1º vez na posição {tupla.index(3)}!")
else:
    print("O 3 não foi digitado!")
if pares:
    print(f"Os números pares são: {pares}")
else:
    print("Não foram digitados números pares!")


