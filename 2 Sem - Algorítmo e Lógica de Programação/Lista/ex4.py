frase = input("Digite uma frase: ")
fraseL = list(frase)
letra = len(fraseL)-fraseL.count(' ')
maiusc = []
minusc = []
for i in fraseL:
    if i.isupper():
        maiusc.append(i)
    if i.islower():
        minusc.append(i)
print(f'Na frase: "{frase}" possuem {letra} letras!')
print(f'Na frase: "{frase}" possuem', sum(1 for i in fraseL if i.isupper()), 'letras maiúsculas!')
print(f"As letras maiúsculas são: {maiusc}")
print(f'Na frase: "{frase}" possuem', sum(1 for i in fraseL if i.islower()), 'letras minusculas!')
print(f"As letras minusculas são: {minusc}")