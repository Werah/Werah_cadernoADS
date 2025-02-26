mes = ("Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro")

cont = 0
while cont < 1:
    mesDig = int(input("Digite o número de um mês, de 1 a 12: \n"))
    if mesDig <13 and mesDig>0:
        print(f"Você digitou o mês de {mes[mesDig-1]}")
        cont = 1