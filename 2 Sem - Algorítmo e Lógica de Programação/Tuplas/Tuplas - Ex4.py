##pega 3 valor na tupla digitado
#qtas vez tem 9
#onde tá o 1º 3
#quais foram os pares

lista = [int(input(f"Digite o {i+1} valor: ")) for i in range(3)]
contNove = 0
posTres = 0
pares = []
for i in range(len(lista)):
    if lista[i] == 9:
        contNove += 1
    if lista[i] == 3 and posTres == 0:
        posTres = i + 1
    if lista[i] %2 == 0:
        pares.append(lista[i])
tuplaLista = tuple(lista)
print(tuplaLista)
if contNove > 0 and contNove != 1:
    print(f"O 9 aparece {contNove} vezes!")
elif contNove == 1:
    print(f"O 9 aparece {contNove} vez!")
else:
    print("O 9 não foi digitado!")

if posTres != 0:
    print(f"O 3 aparece pela 1º vez na posição {posTres}!")
else:
    print("O 3 não foi digitado!")
if pares:
    print(pares)
else:
    print("Não foram digitados números pares!")
