cont = 0
contA = 1
aprov = 0
exame = 0
reprov = 0

while cont < 6:
    nota1 = float(input(f"Digite a 1ª nota do Aluno {contA}: "))
    nota2 = float(input(f"Digite a 2ª nota do Aluno {contA}: "))
    med = (nota1 + nota2)/2
    if med >= 7:
        print (f"O aluno {contA} foi Aprovado!")
        aprov += 1
    elif med >= 3 and med < 7:
        print (f"O aluno {contA} está de Exame!")
        exame += 1
    elif med < 3:
        print (f"O aluno {contA} foi Reprovado!")
        reprov += 1
    else:
        print ("algo deu errado")
    contA += 1
    cont += 1
print (f"O total de alunos aprovados foi: {aprov}")
print (f"O total de alunos de exame foi: {exame}")
print (f"O total de alunos reprovados foi: {reprov}")
    
