#5 times com 11 players
#idade peso altura
#qtde < 18
# media idade por time
# media altura total camp
# % de jogadores com +80 kg no camp

cont = 1
time = 1
jog = 1
contidade = 0
idademed = 0
contpeso = 0
medalt = 0
totaljog =0

while time < 3:
    while cont < 4:
        idade = int(input(f"Digite a idade do jogador {cont} do time {time}: "))
        alt = int(input(f"Digite a altura do jogador {cont} do time {time} em cm (ex: 197): "))
        peso = int(input(f"Digite o peso do jogador {cont} do time {time} em kg (ex: 80): "))
        totaljog +=1
        idademed = idademed + idade
        medalt = medalt + alt
        cont += 1
        if idade < 18:
            contidade += 1
        if peso >= 80:
            contpeso += 1
    finalid = idademed/(cont-1)
    print (f"A médida de idades dos jogadores do time {time} é de {finalid} anos de idade!")
    cont = 1
    idademed = 0
    time += 1

print (f"{contpeso}")
finalpeso = (contpeso/(totaljog*(time-1)))*100
finalt = medalt/(totaljog*(time-1))
print (f"O campeonato possui {contidade} alunos menores de idade")
print (f"A média de altura dos jogadores é: {finalt}")
print (f"A porcetagem de jogadores acima de 80kg é de: {finalpeso}%")
