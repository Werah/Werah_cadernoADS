# 9. Faça um algoritmo que leia a idade de uma pessoa expressa em anos, meses e dias
# e mostre-a expressa apenas em dias.

anos = int(input("Digite a quantidade de anos: "))
meses = int(input("Digite a quantidade de meses: "))
dias = int(input("Digite a quantidade de dias: "))

totalDia = (anos * 365) + (meses * 30) + dias

print(f"A idade expressa em dias é: {totalDia} dias")