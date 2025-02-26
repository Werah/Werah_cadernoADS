nome = input ('Digite o nome do aluno: ')
n1 = int(input("Digite a nota do 1º Semestre: "))
n2 = int(input("Digite a nota do 2º Semestre: "))
n3 = int(input("Digite a nota do 3º Semestre: "))
n4 = int(input("Digite a nota do 4º Semestre: "))
media = (n1+n2+n3+n4)/4
print ("A nota média de {} é: {}".format(nome, media))
