# 10. Faça um algoritmo que leia a idade de uma pessoa expressa em dias
# e mostre-a expressa em anos, meses e dias.

idadeDia = int(input("Digite a idade em dias: "))

anos = idadeDia // 365
diaResto = idadeDia % 365
meses = diaResto // 30 
dias = diaResto % 30 

print(f"A idade em anos, meses e dias é: {anos} anos, {meses} meses e {dias} dias")