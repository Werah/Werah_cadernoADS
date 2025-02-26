cont = 0
maior = 0
menor = 0

while cont < 3:
    aluno = int(input("Digite o número do aluno: "))
    alt = int(input("Digite a altura do aluno: "))
    if alt > maior:
        nmaior = aluno
        maior = alt
    if alt < menor or menor == 0:
        nmenor = aluno
        menor = alt
    cont = cont + 1

print (f"O maior aluno é o número {nmaior}, com {maior} de altura.")
print (f"O menor aluno é o número {nmenor}, com {menor} de altura.")
