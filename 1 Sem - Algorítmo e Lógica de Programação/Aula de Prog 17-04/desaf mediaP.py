ntrab = float(input("Digite a nota do trabalho: "))
nav = float(input("Digite a nota da avaliação: "))
nex = float(input("Digite a nota do exame: "))

media = ((ntrab*2)+(nav*3)+(nex*5))/10

if media >=8:
    conc = "A"
elif media >=7 and media <8:
    conc = "B"
elif media >=6 and media <7:
    conc = "C"
elif media >=5 and media <6:
    conc = "D"
elif media >=0 and media <5:
    conc = "E"
else:
    conc = "F"

print (f"O aluno tirou {ntrab} no trabalho, {nav} na Avaliação, e {nex} no Exame")
print (f"Ficando com uma média de {media}, \nConceito: {conc}")


