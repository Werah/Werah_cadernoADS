pessoa1 = {}
pessoa1['nome'] = str(input("Digite o Nome: "))
pessoa1['media'] = int(input("Digite a Média: "))
if pessoa1['media'] >= 6:
    pessoa1['situ'] = 'Aprovado!'
else:
    pessoa1['situ'] = 'Reprovado!'
print('Nome do Aluno: ', pessoa1['nome'])
print('Média do Aluno: ', pessoa1['media'])
print('Situação: ', pessoa1['situ'])
