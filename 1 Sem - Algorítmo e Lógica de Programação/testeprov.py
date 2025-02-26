n1 = float(input("Digite um numero"))
n2 = float(input("Digite um numero"))
n3 = float(input("Digite um numero"))
menor = n1
maior = n1
if n2 < menor:
    menor = n2
elif n2 > maior:
    maior = n2
    
if n3 < menor:
    menor = n3
elif n3 > maior:
    maior = n3

print ("o menor é:" menor)
print("o maior é:" maior)
