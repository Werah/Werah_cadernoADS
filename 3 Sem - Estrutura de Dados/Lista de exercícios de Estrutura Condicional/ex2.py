#Elaborar um algoritmo que lê 2 valores a e b e os escreve com a mensagem: 
# #"São múltiplos" ou "Não são múltiplos".

valA = int(input("Digite o Primeiro Valor: "))
valB = int(input("Digite o Segundo Valor: "))

if valA % valB == 0:
    print(f"{valA} é multiplo de {valB}")
else:
    print(f"{valA} não é multiplo de {valB}")