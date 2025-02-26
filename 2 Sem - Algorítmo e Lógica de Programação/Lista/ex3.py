lista = [-1, 6, -9, -8, 4, 0, -3, 2, 7, 1, 8, -2]
listaPos = []
listaNeg = []

print(f"Lista Original: {lista}")
print(f"Lista Ordenada: {sorted(lista)}")
for i in lista:
    if i % 2 == 0:
        listaPos.append(i)
    else:
        listaNeg.append(i)
print(f"Lista Positivos: {sorted(listaPos)}")
print(f"Lista Negativos: {sorted(listaNeg)}")
