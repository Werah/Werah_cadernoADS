pessoa1 = {}
pessoa1['nome'] = str(input("Digite o Nome: "))
pessoa1['ano'] = int(input("Digite o ano de Nascimento: "))
pessoa1 ['carteira'] = int(input("Digite a carteira de trabalho (0 não tem): "))
if pessoa1['carteira'] != 0:
    pessoa1 ['anoC'] = int(input("Digite o ano de Contratação: "))
    pessoa1 ['sala'] = int(input("Digite o Salário: "))
print('Nome: ', pessoa1['nome'])
print('Ano: ', pessoa1['ano'])
print('carteira: ', pessoa1['carteira'])
print('AnoC: ', pessoa1['anoC'])
print('Sala: ', pessoa1['sala'])

idade = 2024 - pessoa1['ano']
print(f"\nIdade: {idade}")


apos = pessoa1['anoC'] + 35
print(f"\nAno de Aposentadoria: {apos}")

sapos = apos - pessoa1['ano']
print(f"\nVai se aposentar com: {sapos} anos!")

