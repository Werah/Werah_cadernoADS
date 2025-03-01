#Elabore um algoritmo que dada a idade de um nadador classifica-o em uma das seguintes categorias:
#infantil A =  5 -  7 anos
#infantil B =  8 - 10 anos
#juvenil  A = 11 - 13 anos
#juvenil  B = 14 - 17 anos
#adulto = maiores de 18 anos

idade = int(input("Digite sua idade: "))

if idade < 8:
    categoria = "infantil A"
elif idade <11:
    categoria = "infantil B"
elif idade <14:
    categoria = "Juvenil A"
elif idade <18:
    categoria = "Juvenil B"
else:
    categoria = "Adulto"

print(f"Você faz parto da categoria: {categoria}!")