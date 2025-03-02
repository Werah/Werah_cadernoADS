#1.  Pesquisa sobre Idade e Altura: 
#   A prefeitura de uma cidade fez uma pesquisa entre seus habitantes, coletando dados sobre a 
#   idade e altura. A prefeitura deseja saber:
#   a) média da idade da população;
#   b) média da altura da população;
#   c) maior idade registrada;
#   d) percentual de pessoas com altura acima de 1,80 metros.
#   O final da leitura de dados se dará com a entrada de uma idade negativa.

cont = 0
idadeCont = 0
altCont = 0
pessoaAlta = 0
while True:
    idade = int(input(f"Digite a idade da {cont+1}ª pessoa, ou um número negativo para sair: "))
    if idade < 0:
        break
    altura = float(input(f"Digite a altura da {cont+1}ª pessoa: "))
    if altura > 1.80:
        pessoaAlta += 1
    cont += 1
    print(cont)
    idadeCont += idade
    altCont += altura
if cont > 0:
    print (f"Numero de pessoas cadastradas: {cont}")
    print (f"Média de idade da população: {idadeCont/cont}")
    print (f"Média de altura da população: {altCont/cont}")
    print (f"Porcentagem da população acima de 1.80m: {(pessoaAlta/cont)*100}%")
else:
    print("Nenhuma possoa foi cadastrada.")