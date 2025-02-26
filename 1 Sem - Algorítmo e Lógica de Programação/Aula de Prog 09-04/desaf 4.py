#dado 5 numeros apresente o maior e menor

cont =0

for i in range (5):
    num = int(input("Digite um número: "))
    maior = null
    menor = null
    if num > maior:
        maior = num
    if menor < num:
        menor = num
    

print (f"O maior número é (maior), e o menor é (menor)")
