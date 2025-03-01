# 5. Tendo como dados de entrada a altura e o sexo de uma pessoa ('M' masculino e 'F' feminino),
# construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
# - para homens: (72.7 * h) - 58
# - para mulheres: (62.1 * h) - 44.7

altura = float(input("Digite a altura (ex: 1.70): "))
sexo = input("Digite o sexo (M para masculino ou F para feminino): ").upper()

if sexo == 'M':
    pesoIdeal = (72.7 * altura) - 58
    print(f"O peso ideal para um homem com {altura}m é: {pesoIdeal:.2f} kg")
elif sexo == 'F':
    pesoIdeal = (62.1 * altura) - 44.7
    print(f"O peso ideal para uma mulher com {altura}m é: {pesoIdeal:.2f} kg")
else:
    print("Sexo inválido! Digite 'M' para masculino ou 'F' para feminino.")